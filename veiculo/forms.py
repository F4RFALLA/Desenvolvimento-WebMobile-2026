from django import forms
from veiculo.models import Veiculo


class FormularioVeiculo(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca', 'modelo', 'ano', 'cor', 'combustivel', 'foto']
        widgets = {
            'marca': forms.Select(attrs={'class': 'vehicle-form-input'}),
            'modelo': forms.TextInput(attrs={
                'class': 'vehicle-form-input',
                'placeholder': 'Digite o modelo'
            }),
            'ano': forms.NumberInput(attrs={
                'class': 'vehicle-form-input',
                'placeholder': 'Digite o ano'
            }),
            'cor': forms.Select(attrs={'class': 'vehicle-form-input'}),
            'combustivel': forms.Select(attrs={'class': 'vehicle-form-input'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'vehicle-form-file'}),
        }