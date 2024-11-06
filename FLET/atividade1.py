import flet as ft

def main(page: ft.Page):

    page.title = "Formulário de Contato"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    nome_field = ft.TextField(label="Nome", autofocus=True, width=300)
    email_field = ft.TextField(label="Email", keyboard_type=ft.KeyboardType.EMAIL, width=300)
    mensagem_field = ft.TextField(label="Mensagem", multiline=True, width=300, height=150)

    # Criando o botão de envio
    def on_submit(e):

        if nome_field.value and email_field.value and mensagem_field.value:

            confirmation_text.value = "Formulário enviado com sucesso!"
            page.update()
        else:
            confirmation_text.value = "Por favor, preencha todos os campos."
            page.update()

    submit_button = ft.ElevatedButton("Enviar", on_click=on_submit)


    confirmation_text = ft.Text("", size=20, color=ft.colors.GREEN)


    page.add(
        nome_field,
        email_field,
        mensagem_field,
        submit_button,
        confirmation_text
    )


ft.app(target=main)
