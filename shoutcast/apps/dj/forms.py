from django.forms import ModelForm
from dj.models import DjShow


class ShowForm(ModelForm):
    class Meta:
        model = DjShow
        fields = ('show_name', 'description')
