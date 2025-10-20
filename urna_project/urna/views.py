from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.db import transaction
from django.utils import timezone
from .forms import FuncionarioLoginForm  # ATENÇÃO: O form também precisa ser atualizado
from .models import Funcionario, Candidate, Vote # MUDOU: Importa Funcionario
from django.contrib import messages

def get_client_ip(request):
    xff = request.META.get('HTTP_X_FORWARDED_FOR')
    if xff:
        return xff.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')

@require_http_methods(["GET", "POST"])
def funcionario_login(request): # MUDOU: Nome da view para clareza
    # Você precisará criar/atualizar este form em forms.py
    form = FuncionarioLoginForm(request.POST or None) 
    
    if form.is_valid():
        cpf = form.cleaned_data['cpf']
        # MUDOU: O campo agora é 're'
        re_funcionario = form.cleaned_data['re'] 
        
        try:
            # MUDOU: Busca no modelo Funcionario usando 're'
            funcionario = Funcionario.objects.get(cpf=cpf, re=re_funcionario)
        except Funcionario.DoesNotExist: # MUDOU
            messages.error(request, "Funcionário não encontrado ou dados inválidos.")
            return render(request, 'urna/login.html', {'form': form})

        # REMOVIDO: O campo 'allowed' não existe mais no seu novo modelo.

        if funcionario.has_voted: # MUDOU: Usa a variável 'funcionario'
            messages.error(request, "Este funcionário já votou.")
            return render(request, 'urna/login.html', {'form': form})

        # MUDOU: A chave da sessão agora é 'funcionario_id'
        request.session['funcionario_id'] = funcionario.id 
        return redirect('urna:vote_screen')
        
    return render(request, 'urna/login.html', {'form': form})

@require_http_methods(["GET", "POST"])
def vote_screen(request):
    # MUDOU: Busca a chave 'funcionario_id' na sessão
    funcionario_id = request.session.get('funcionario_id') 
    if not funcionario_id:
        # MUDOU: Redireciona para a nova view de login
        return redirect('urna:funcionario_login') 

    # MUDOU: Busca um objeto Funcionario
    funcionario = get_object_or_404(Funcionario, id=funcionario_id) 
    candidates = Candidate.objects.order_by('number')

    if request.method == 'POST':
        candidate_id = request.POST.get('candidate_id')
        candidate = get_object_or_404(Candidate, id=candidate_id)

        with transaction.atomic():
            # MUDOU: Faz o lock na tabela Funcionario para segurança
            funcionario_db = Funcionario.objects.select_for_update().get(id=funcionario.id)
            
            if funcionario_db.has_voted:
                messages.error(request, "Voto não computado: funcionário já votou.")
                return redirect('urna:funcionario_login')

            vote = Vote.objects.create(
                # MUDOU: O campo 'voter' do modelo Vote agora recebe o objeto 'funcionario_db'
                voter=funcionario_db, 
                candidate=candidate,
                created_at=timezone.now(),
                ip_address=get_client_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT', '')[:255]
            )
            
            funcionario_db.has_voted = True
            funcionario_db.last_voted_at = timezone.now()
            funcionario_db.save()

        request.session['last_vote_id'] = vote.id
        return redirect('urna:receipt')
    
    # MUDOU: Passa o objeto 'funcionario' para o template
    return render(request, 'urna/vote_screen.html', {'funcionario': funcionario, 'candidates': candidates})

def receipt(request):
    vote_id = request.session.get('last_vote_id')
    if not vote_id:
        return redirect('urna:funcionario_login') # MUDOU
    
    vote = get_object_or_404(Vote, id=vote_id)
    return render(request, 'urna/receipt.html', {'vote': vote})