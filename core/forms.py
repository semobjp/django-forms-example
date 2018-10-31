from django import forms
from core.models import Funcionario


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        exclude = []

    def __init__(self, *args, **kwargs):
        self.setor = kwargs.pop('setor')
        super(FuncionarioForm, self).__init__(*args, **kwargs)

        if self.setor:
            del self.fields['setor']

    def clean(self, *args, **kwargs):
        '''Valida o formulário'''
        if self.instance:
            # Atribuimos o setor a instância do form
            self.instance.setor = self.setor
        return super(FuncionarioForm, self).clean(*args, **kwargs)