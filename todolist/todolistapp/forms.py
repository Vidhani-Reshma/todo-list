from django import forms 

from todolistapp import models


class noteform(forms.ModelForm):
    class Meta:
        model = models.note
        fields = "__all__"  
        exclude = ('user',)