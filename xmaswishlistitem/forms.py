from django import forms
from .models import xmaswishlistitem

class xmaswishlistitemForm(forms.ModelForm):
    class Meta:
        model = xmaswishlistitem
        fields = ('name', 'done')
