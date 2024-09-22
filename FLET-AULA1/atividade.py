import flet as ft

def main(page):
    page.title = "Lista de Tarefas"

    tarefa_input = ft.TextField(label="Digite sua tarefa", width=300)

    tarefas_list = ft.Column()

    def adicionar_tarefa(e):
        if tarefa_input.value:  
            tarefas_list.controls.append(ft.Text(tarefa_input.value))
            tarefa_input.value = ""  
            page.update()  

    adicionar_button = ft.ElevatedButton("Adicionar Tarefa", on_click=adicionar_tarefa)

    page.add(tarefa_input, adicionar_button, tarefas_list)

ft.app(target=main)
