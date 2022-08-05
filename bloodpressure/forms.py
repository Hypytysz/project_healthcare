from django import forms
from . models import Bloodpressure

class BloodpressureForm(forms.ModelForm):

    class Meta:
        model = Bloodpressure
        fields = "__all__"