from haystack import indexes, site
from music.models import Song


class SongIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title")
    artist = indexes.CharField(model_attr="artist__artist")
    album = indexes.CharField(model_attr="album__album")
    genre = indexes.CharField(model_attr="genre__genre")

site.register(Song, SongIndex)