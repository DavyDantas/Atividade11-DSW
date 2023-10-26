from django import forms 
from .models import Aluno

class formAluno(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'