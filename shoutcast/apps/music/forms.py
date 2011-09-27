from django.forms import ModelForm
from music.models import Upload


class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('song_file',)
