import mutagen
import commands
import json
import pyechonest
from pyechonest import artist
import slumber
import urllib, urllib2

#data = commands.getoutput("echoprint-codegen " + song + " 10 30")
#j = json.loads(data)
#d = j[0]['metadata']

class SongInfo(object):

    def __init__(self, song):
        self.song = song
        data = commands.getoutput("echoprint-codegen " + song + " 10 30")
        j = json.loads(data)
        self.meta = j[0]['metadata']

    def get_artist(self, artist_id):
       self.artist_id = artist_id
       a = artist.Artist(artist_id)
       return self.a
       
if __name__ == '__main__':
    crap = SongInfo('/home/alan/coding/shoutcast-web/server/song.mp3')
    code = crap.code
    meta = crap.meta

    print meta['artist']
    print meta['title']
