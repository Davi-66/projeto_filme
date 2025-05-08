from django import forms # importa os formularios do django.
from sistema.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario # Define qual é o model que o form representa
        fields = ['nome', 'sobrenome', 'cpf', 'telefone', 'email', 'endereco', 'imagem',] #São os campos que serão exibidos no form(HTML)
