from django import forms
from .models import Images


# Create your forms here.
class ImageForm(forms.ModelForm):

    class Meta:
        model = Images
        fields = ['image']