import os
import subprocess
import requests
from bs4 import BeautifulSoup
from pippi import dsp
from hcj import fx

api_key = os.environ.get('FMA_API_KEY')
endpoint = 'http://freemusicarchive.org/api/get/tracks.json'
maxtrack_id = 116020 # thanks ross!

numtracks = 10
numsections = 10

out = ''

for section in range(numsections):
    tracks = []
    foundtracks = 0
    while foundtracks <= numtracks:
        track_id = dsp.randint(1, maxtrack_id)
        params = {'api_key': api_key, 'track_id': track_id}
        track = requests.get(endpoint, params=params)
        try:
            track = track.json()

            if len(track['errors']) == 0:

                track_url = track['dataset'][0]['track_url']

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

                tracks += [ snd ]
                
                os.remove('%s.mp3' % track_id)
                os.remove('%s.wav' % track_id)

                foundtracks += 1

        except Exception:
            pass
    
    for track in tracks:
        out += fx.spider(track)

dsp.write(out, 'fmape')
