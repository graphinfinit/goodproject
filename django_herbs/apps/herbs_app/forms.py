from .models import Herb_article
from django.forms import ModelForm

class Herb_articleForm(ModelForm):
    class Meta:
        model = Herb_article
        fields = ('herb_name', 'herb_text')

