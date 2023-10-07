'''
To-do List
V2
'''

import tkinter as tk
from tkinter import messagebox

task_number = 1

# Adicionar novas tarefas
def adicionar_task():
    global task_number
    task = task_entry.get()
    with open("todo.txt", "a") as f:
        f.write(str(task_number) + ". " + task + "\n")
        task_number += 1
    task_entry.delete(0, tk.END)

# Exibir tarefas existentes
def mostrar_tasks():
    with open("todo.txt", "r") as f:
        tasks = f.readlines()
    tasks_window = tk.Toplevel(root)
    tasks_window.title("Tarefas Existente")
    task_list = tk.Listbox(tasks_window)
    for task in tasks:
        task_list.insert(tk.END, task.strip())
    task_list.pack()
    

# Editar tarefas
def editar_tasks():
    with open("todo.txt", "r") as f:
      tasks = f.readlines()
    editar_window = tk.Toplevel(root)
    editar_window.title("Editar Tarefas")
    task_list = tk.Listbox(editar_window)
  
    for task in tasks:
      task_list.insert(tk.END, task.strip())
    task_list.pack()

  # Função interna para salvar task editada
    def salvar_task():
      selection = task_list.curselection()
      if not selection:
        return
      task_index = selection[0]
      task = tasks[task_index].strip()
      nova_task = editar_entry.get()
      tasks[task_index] = str(task_index+1) + ". " + nova_task + "\n"
      with open("todo.txt", "w") as f:
        f.writelines(tasks)
      messagebox.showinfo("Editar tarefa", "A tarefa foi editada")
      editar_window.destroy()


    editar_entry = tk.Entry(editar_window)
    editar_entry.pack()

  # Botão de salvar task editada
    editar_button = tk.Button(editar_window, text="Salva edição", command=salvar_task)
    editar_button.pack()


# Remover tarefas, função geral
def remover_tasks():
  # Abre arquivo de texto
    with open("todo.txt", "r") as f:
        tasks = f.readlines()
      # Verifica se o arquivo está vazio
    if not tasks:
        messagebox.showinfo("Remover Tarefa", "Não há tarefas a serem removidas.")
        return
      
  # Janela de seleção para remover tarefas
    remove_window = tk.Toplevel(root)
    remove_window.title("Remover Tarefa")
  
    task_list = tk.Listbox(remove_window)
    for task in tasks:
        task_list.insert(tk.END, task.strip())
    task_list.pack()

  # Função interna, pega a task selecionada, remove da lista e mostra mensagem de remoçõa
    def remover_task():
        selection = task_list.curselection()
        if not selection:
            return
        task_index = selection[0]
        task = tasks[task_index].strip()
        tasks.remove(tasks[task_index])
        with open("todo.txt", "w") as f:
            f.writelines(tasks)
        messagebox.showinfo("Remover Tarefa", f"A tarefa '{task}' foi removida.")
        task_list.delete(tk.ACTIVE)

  # Butão de remover task selecionada
    remove_button = tk.Button(remove_window, text="Remover Selecionada", command=remover_task)
    remove_button.pack()


# Cria janela do aplicativo
root = tk.Tk()
root.title("Lista de Tarefas")


# Entrada de texto
task_entry = tk.Entry(root)
task_entry.pack()

  ## Cria botões e associa as respectivas funções a eles
add_button = tk.Button(root, text="Adicionar Tarefa", command=adicionar_task)
add_button.pack()

show_button = tk.Button(root, text="Exibir Tarefas", command=mostrar_tasks)
show_button.pack()

edit_button = tk.Button(root, text="Editar Tarefa", command=editar_tasks)
edit_button.pack()

remove_button = tk.Button(root, text="Remover Tarefa", command=remover_tasks)
remove_button.pack()

root.mainloop()
