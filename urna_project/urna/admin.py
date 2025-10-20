from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Candidate, Vote, Funcionario

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'party')
    search_fields = ('name', 'number', 'party')

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'voter', 'candidate', 'created_at', 'ip_address')
    search_fields = ('voter__cpf', 'candidate__name')
    readonly_fields = ('created_at',)
    
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 're', 'has_voted')
    search_fields = ('nome', 'cpf', 're')
    
    def save_model(self, request, obj, form, change):
        # Pega o CPF digitado no admin
        cpf = obj.cpf
        # Limpa para ter apenas os números
        numeros_cpf = "".join(filter(str.isdigit, cpf))
        
        # Se for válido, formata e salva
        if len(numeros_cpf) == 11:
            obj.cpf = f"{numeros_cpf[0:3]}.{numeros_cpf[3:6]}.{numeros_cpf[6:9]}-{numeros_cpf[9:11]}"
        
        # Continua o processo de salvamento
        super().save_model(request, obj, form, change)