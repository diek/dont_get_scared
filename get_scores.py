#Python 2.7
''' Requests is already installed for Python 3 but not for python 2.7 you need
to install requests; for linux or mac users, the easiest method is to install
using python's package manager pip, so: $ sudo pip install requests
for windows install see the accepted answer:
http://stackoverflow.com/questions/21493784/python-importerror-no-module-named-requests
'''
import requests
resp = requests.get('http://worldcup.sfg.io/matches')
for jogo in resp.json():
    if jogo['status'] == 'completed':
        print jogo['home_team']['country'], jogo['home_team']['goals'], 'x', jogo['away_team']['country'], jogo['away_team']['goals']

# Python 3
# import urllib.request
# import json
# resp = urllib.request.urlopen('http://worldcup.sfg.io/matches').read()
# for jogo in json.loads(resp.decode('utf-8')):
#     if jogo['status'] == 'completed':

sudo mv git-credential-osxkeychain \
"$(dirname $(which git))/git-credential-osxkeychain"
# Move the helper to the path where git is installed
# Password:

