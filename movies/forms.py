from django.forms import ModelForm
from .models import *
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['isim', 'resim']

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mt-2'})
            