from django import forms

from .models import Abcd

class PostForm(forms.ModelForm):

    class Meta:
        model = Abcd
        fields = ('title', 'text',)