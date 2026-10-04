from django import forms


from .models import car

class carForm(forms.ModelForm):
    class Meta:
        model = car
        fields = '__all__'
