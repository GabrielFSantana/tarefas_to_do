import sqlite3
from datetime import datetime

# CONECTA NO BD
def init_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority INTEGER,
            due_date TEXT,
            status TEXT DEFAULT 'Pendente'
        )
    ''')
    conn.commit()
    conn.close()

# AQUI CRIAAAA
def add_task(title, description, priority, due_date):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, priority, due_date) 
        VALUES (?, ?, ?, ?)
    ''', (title, description, priority, due_date))
    conn.commit()
    conn.close()
    print("Tarefa adicionada com sucesso!")

# LISTA TUDO
def list_tasks(status_filter=None):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    query = 'SELECT * FROM tasks'
    if status_filter:
        query += ' WHERE status = ?'
        cursor.execute(query, (status_filter,))
    else:
        cursor.execute(query)
    tasks = cursor.fetchall()
    conn.close()

    print("\n--- Lista de Tarefas ---")
    for task in tasks:
        print(f"ID: {task[0]}, Título: {task[1]}, Status: {task[5]}")
        print(f"Descrição: {task[2]}, Prioridade: {task[3]}, Prazo: {task[4]}")
        print("-" * 30)

# ATUALIZARR
def update_task_status(task_id, new_status):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tasks
        SET status = ?
        WHERE id = ?
    ''', (new_status, task_id))
    conn.commit()
    conn.close()
    print("Status atualizado com sucesso!")

# EXCLUIR 
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM tasks
        WHERE id = ?
    ''', (task_id,))
    conn.commit()
    conn.close()
    print("Tarefa excluída com sucesso!")

# INICIAL
def menu():
    init_db()
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Atualizar Status")
        print("4. Excluir Tarefa")
        print("5. Sair")
        option = input("Escolha uma opção: ")

        if option == '1':
            title = input("Título: ")
            description = input("Descrição: ")
            priority = int(input("Prioridade (1-5): "))
            due_date = input("Prazo (YYYY-MM-DD): ")
            add_task(title, description, priority, due_date)
        elif option == '2':
            status_filter = input("Filtrar por status (Pendente/Concluído/Enter para todos): ")
            list_tasks(status_filter if status_filter else None)
        elif option == '3':
            task_id = int(input("ID da tarefa: "))
            new_status = input("Novo status (Pendente/Concluído): ")
            update_task_status(task_id, new_status)
        elif option == '4':
            task_id = int(input("ID da tarefa: "))
            delete_task(task_id)
        elif option == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
