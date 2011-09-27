from django.forms import ModelForm
from dj.models import DjShow


class ShowForm(ModelForm):
    class Meta:
        model = DjShow
        fields = ('show_name', 'description')

    def __init__(self, *args, **kwargs):
        super(ShowForm, self).__init__(*args, **kwargs)
        self.fields['show_name'].widget.attrs['style'] = "height: 20px;"
