# Todo List Web App
Este é um simples aplicativo de lista de tarefas desenvolvido com Django. O objetivo deste projeto é gerenciar tarefas de forma simples e eficaz, permitindo que os usuários visualizem, criem, editem e excluam tarefas.

## Tecnologias Utilizadas
Python 3.x
Django 4.x
SQLite (banco de dados padrão do Django)

## Funcionalidades
Listar tarefas: Visualize todas as tarefas cadastradas.

Visualizar detalhes: Veja os detalhes de uma tarefa específica.

Criar tarefas: Adicione novas tarefas à sua lista.

Editar tarefas: Edite uma tarefa existente.

Status das tarefas: Marque as tarefas como Pendente ou Concluída.

Prioridade das tarefas: Classifique as tarefas por prioridade de 1 a 5.

## Instalação

### Pré-requisitos
Certifique-se de ter o Python 3.x e o pip instalados no seu sistema.

### Passos para rodar o projeto localmente
1. Clone o repositório:
   ```bash
   git clone https://github.com/GabrielFSantana/todo-simpler.git
   cd todo-simpler
2. Crie e ative um ambiente virtual:
   ```bash
      python -m venv venv
      .\venv\Scripts\activate
3. Instale as dependências:
   ```bash
      pip install -r requirements.txt
4. Realize as migrações do banco de dados:
   ```bash
      python manage.py migrate
5. Crie um superusuário para acessar o painel administrativo (opcional):
   ```bash
   python manage.py createsuperuser
6. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
7. Acesse o aplicativo:
Abra seu navegador e vá para http://127.0.0.1:8000/ para visualizar a lista de tarefas.
Para acessar o painel administrativo do Django, vá para http://127.0.0.1:8000/admin e faça login com o superusuário criado.
