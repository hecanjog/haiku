import os
import subprocess
import requests
from bs4 import BeautifulSoup
from pippi import dsp
from hcj import fx

api_key = os.environ.get('FMA_API_KEY')
endpoint = 'http://freemusicarchive.org/api/get/tracks.json'
maxtrack_id = 116020 # thanks ross!

numsections = 10

out = ''

for section in range(numsections):
    tracks = []
    foundtracks = 0
    numtracks = dsp.randint(3, 10) 

    while foundtracks <= numtracks:
        track_id = dsp.randint(1, maxtrack_id)
        params = {'api_key': api_key, 'track_id': track_id}
        track = requests.get(endpoint, params=params)
        try:
            track = track.json()
            track_license = track['dataset'][0]['license_title']

            if len(track['errors']) == 0 and not 'Deriv' in track_license:

                track_url = track['dataset'][0]['track_url']
                track_name = track['dataset'][0]['track_title']
                track_artist = track['dataset'][0]['artist_name']

                dsp.log('%s by %s. %s' % (track_name, track_artist, track_license))

                track_page = requests.get(track_url)
                html = BeautifulSoup(track_page.text)
                track_url = html.find_all('a', class_='icn-arrow')[0].get('href')

                with open('%s.mp3' % track_id, 'wb') as track_data:
                    r = requests.get(track_url)

                    if r.ok:
                        track_data.write(r.content)

                cmd = 'sox %s.mp3 %s.wav trim 0 5' % (track_id, track_id)
                p = subprocess.Popen(cmd, shell=True)
                p.wait()

                snd = dsp.read('%s.wav' % track_id).data

                tracks += [ dsp.amp(snd, 0.25) ]
                
                os.remove('%s.mp3' % track_id)
                os.remove('%s.wav' % track_id)

                foundtracks += 1

        except Exception:
            pass
    
    out += dsp.mix([ fx.spider(track, dsp.randint(5, 20), dsp.randint(10, 50), dsp.rand(30, 50), (dsp.rand(5, 50), dsp.rand(200, 1500)), dsp.randchoose([True, False])) for track in tracks ])

dsp.write(out, 'fmape')
