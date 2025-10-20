Urna Eletrônica com Django
📄 Sobre o Projeto
Este projeto é um simulador de uma Urna Eletrônica brasileira, desenvolvido com o framework Python Django. O sistema foi criado com foco em simular eleições internas de comissões, como a CIPA (Comissão Interna de Prevenção de Acidentes e de Assédio), utilizando uma interface moderna e com temática de segurança do trabalho.

O design da interface de votação foi pensado para ser totalmente responsivo, com o objetivo de ser utilizado em tablets para simular a experiência real de uma cabine de votação.

✨ Funcionalidades Principais
Interface de Votação Realista: A tela de votação simula a urna eletrônica brasileira, com teclado numérico e exibição da foto e dados do candidato.

Design Responsivo (Tablet First): O layout se adapta perfeitamente a diferentes tamanhos de tela. Em dispositivos menores (como tablets na vertical), o teclado se posiciona abaixo da tela, e em telas maiores (tablets na horizontal e desktops), fica ao lado, otimizando a experiência de uso.

Processo de Voto Completo: Permite a digitação do número do candidato, voto em branco, correção do voto e confirmação.

Comprovante de Votação Térmico: Após a confirmação do voto, o sistema gera um comprovante de votação estilizado para se assemelhar a um recibo de impressora térmica.

Responsividade do Comprovante: O comprovante também é responsivo, garantindo uma boa visualização tanto em dispositivos móveis quanto em desktops antes da impressão.

Painel de Administração: Utiliza o painel de administração nativo do Django para um gerenciamento fácil de candidatos e eleitores.

🎨 Tema Visual
A interface adota uma paleta de cores em tons de verde, remetendo à CIPA e à segurança do trabalho, criando uma identidade visual coesa e profissional para o propósito da aplicação.

💻 Tecnologias Utilizadas
Backend: Python 3, Django

Frontend: HTML5, CSS3 (com Flexbox e Media Queries para responsividade), JavaScript

Banco de Dados: SQLite (padrão do Django, pode ser facilmente alterado)

🚀 Como Executar o Projeto Localmente
Clone o repositório:

Bash

git clone https://github.com/seu-usuario/urna-eletronica-django.git
cd urna-eletronica-django
Crie e ative um ambiente virtual:

Bash

python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
Instale as dependências:

Bash

pip install -r requirements.txt
Aplique as migrações do banco de dados:

Bash

python manage.py migrate
Crie um superusuário para acessar o painel de admin:

Bash

python manage.py createsuperuser
Execute o servidor de desenvolvimento:

Bash

python manage.py runserver
Acesse http://127.0.0.1:8000 em seu navegador.
