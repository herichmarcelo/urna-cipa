# urna/forms.py

from django import forms
from .models import Candidate

class FuncionarioLoginForm(forms.Form):
    cpf = forms.CharField(label='CPF', max_length=14)
    re = forms.CharField(label='Registro (RE)', max_length=10)

    # ✨ LÓGICA INVERTIDA: AGORA NÓS FORMATAMOS ✨
    def clean_cpf(self):
        # 1. Pega o valor digitado pelo usuário
        cpf = self.cleaned_data.get('cpf')
        
        # 2. Limpa qualquer formatação que o usuário tenha digitado para ter a base crua
        numeros_cpf = "".join(filter(str.isdigit, cpf))

        # 3. Valida se a base crua tem 11 dígitos
        if len(numeros_cpf) != 11:
            raise forms.ValidationError("CPF inválido. Deve conter 11 dígitos.")

        # 4. Aplica a formatação oficial e retorna ELA
        formatado = f"{numeros_cpf[0:3]}.{numeros_cpf[3:6]}.{numeros_cpf[6:9]}-{numeros_cpf[9:11]}"
        return formatado

class VoteForm(forms.Form):
    # Este formulário está correto, mas note que a sua view 'vote_screen'
    # atualmente pega o ID do candidato diretamente do request.POST.
    # Usar este form na view seria uma melhoria futura para validação extra.
    candidate = forms.ModelChoiceField(
        queryset=Candidate.objects.all(), 
        widget=forms.HiddenInput()
    )