from django import forms
from dados.models import Eleicao

class FormularioCadastro(forms.ModelForm):
    class Meta:
        model = Eleicao
        fields = ["eleicao_nome","eleicao_data_fim"]