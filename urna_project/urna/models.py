from django.db import models
from django.utils import timezone
#from django.core.validators import RegexValidator
# Não vamos mais usar o RegexValidator aqui, a validação será no form

# Validador para garantir que o CPF tenha apenas 11 números
#cpf_validator = RegexValidator(r'^\d{11}$', 'CPF deve conter 11 dígitos numéricos (sem pontuação).')

# ✨ MODELO PRINCIPAL PARA O ELEITOR ✨
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    # MUDANÇA: Aumentamos o tamanho para 14 para caber '123.456.789-00'
    cpf = models.CharField(
        max_length=14, 
        unique=True,
        help_text="O CPF será salvo no formato 123.456.789-00"
    )
    re = models.CharField(max_length=10, unique=True)
    has_voted = models.BooleanField(default=False)
    last_voted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

class Candidate(models.Model):
    name = models.CharField(max_length=120)
    number = models.PositiveIntegerField(unique=True)
    party = models.CharField(max_length=60, blank=True)
    photo = models.ImageField(upload_to='candidates/', blank=True, null=True)

    def __str__(self):
        return f"{self.number} - {self.name}"

class Vote(models.Model):
    # ✨ ATUALIZADO: Agora o voto é ligado diretamente ao Funcionario
    voter = models.ForeignKey(Funcionario, on_delete=models.PROTECT, related_name='votes')
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Voto de {self.voter.nome} para {self.candidate.name}"

# O modelo 'Voter' foi removido para evitar duplicidade.