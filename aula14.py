import datetime
import flet as ft


class Cliente:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email


class Quarto:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.disponivel = True


class Reserva:
    def __init__(self, cliente, quarto, data_entrada, data_saida):
        self.cliente = cliente
        self.quarto = quarto
        self.data_entrada = data_entrada
        self.data_saida = data_saida


class GerenciadorDeReservas:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        self.reservas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def fazer_reserva(self, cliente, quarto, data_entrada, data_saida):
        if quarto.disponivel:
            reserva = Reserva(cliente, quarto, data_entrada, data_saida)
            self.reservas.append(reserva)
            quarto.disponivel = False
            return True
        return False

    def cancelar_reserva(self, reserva):
        self.reservas.remove(reserva)
        reserva.quarto.disponivel = True


def main(page: ft.Page):
    page.bgcolor = ft.colors.OUTLINE_VARIANT
    gerenciador = GerenciadorDeReservas()

    def button_clicked_cliente(e):
        cliente = Cliente(nome.value, cpf.value, email.value)
        gerenciador.adicionar_cliente(cliente)

        dropdown_clientes.options.append(ft.dropdown.Option(cliente.nome + f" (CPF: {cliente.cpf})"))
        page.update()

        nome.value = ""
        cpf.value = ""
        email.value = ""
        page.update()

    def button_clicked_quarto(e):
        tipo_quarto = dropdown_tipo_quarto.value
        room_number = dropdown_quartos_reserva.value
        quarto = Quarto(room_number, tipo_quarto)
        gerenciador.adicionar_quarto(quarto)

        texto_quarto.value = f"Número do quarto: '{room_number}', Tipo de quarto: '{tipo_quarto}'."
        page.update()

    def button_clicked_reserva(e):
        selected_cliente = dropdown_clientes.value
        quarto_num = dropdown_quartos_reserva.value

        cliente_info = next((c for c in gerenciador.clientes if f"{c.nome} (CPF: {c.cpf})" == selected_cliente), None)
        quarto = next((q for q in gerenciador.quartos if q.numero == quarto_num), None)

        if selected_cliente and data_entrada.value and data_saida.value and cliente_info and quarto:
            if gerenciador.fazer_reserva(cliente_info, quarto, data_entrada.value, data_saida.value):
                update_reserva_table()
                texto_quarto.value = "Reserva registrada com sucesso."
            else:
                texto_quarto.value = "Quarto não disponível."
        else:
            texto_quarto.value = "Por favor, preencha todos os campos."

        page.update()

    def update_reserva_table():
        data_table.rows.clear()
        for reserva in gerenciador.reservas:
            data_table.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(reserva.cliente.nome)),
                ft.DataCell(ft.Text(reserva.cliente.cpf)),
                ft.DataCell(ft.Text(reserva.cliente.email)),
                ft.DataCell(ft.Text(reserva.data_entrada)),
                ft.DataCell(ft.Text(reserva.data_saida)),
                ft.DataCell(ft.Text(reserva.quarto.tipo)),
                ft.DataCell(ft.Text(reserva.quarto.numero)),
                ft.DataCell(ft.IconButton(ft.icons.DELETE, on_click=lambda e, r=reserva: cancel_reserva(r))),
            ]))
        page.update()

    def cancel_reserva(reserva):
        gerenciador.cancelar_reserva(reserva)
        update_reserva_table()
        texto_quarto.value = "Reserva cancelada com sucesso."
        page.update()

    def open_date_picker_entrada(e):
        page.open(
        ft.DatePicker(
            first_date=datetime.datetime(day=1, month=1, year=2001),
            last_date=datetime.datetime(day=31, month=12, year=2030),
            on_change=date_selected_entrada,
        )
    )

    def date_selected_entrada(e):
        if e.control.value:
            data_entrada.value = e.control.value.strftime('%d-%m-%Y')
            page.update()

    def open_date_picker_saida(e):
        page.open(
            ft.DatePicker(
                first_date=datetime.datetime(day=1, month=1, year=2001),
                last_date=datetime.datetime(day=31, month=12, year=2030),
                on_change=date_selected_saida,
            )
        )

    def date_selected_saida(e):
        if e.control.value:
            data_saida.value = e.control.value.strftime('%d-%m-%Y')
            page.update()


    nome = ft.TextField(label="Nome", border_color=ft.colors.CYAN_ACCENT_700, hint_text="Insira aqui", bgcolor=ft.colors.ON_TERTIARY, color=ft.colors.TERTIARY)
    cpf = ft.TextField(label="CPF", border_color=ft.colors.CYAN_ACCENT_700, hint_text="Insira aqui", bgcolor=ft.colors.ON_TERTIARY, color=ft.colors.TERTIARY)
    email = ft.TextField(label="E-mail", border_color=ft.colors.CYAN_ACCENT_700, hint_text="Insira aqui", icon=ft.icons.EMAIL, bgcolor=ft.colors.ON_TERTIARY, color=ft.colors.TERTIARY)

    botao_cliente = ft.ElevatedButton(text="Cadastrar Cliente", bgcolor=ft.colors.CYAN_ACCENT_700, color=ft.colors.WHITE, on_click=button_clicked_cliente, style=ft.ButtonStyle(
        text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)))

    dropdown_tipo_quarto = ft.Dropdown(
        label="Tipo de Quarto",
        options=[
            ft.dropdown.Option("Standard"),
            ft.dropdown.Option("Luxo"),
            ft.dropdown.Option("Simples"),
        ],
        bgcolor=ft.colors.ON_TERTIARY,
        color=ft.colors.TERTIARY
    )

    dropdown_quartos_reserva = ft.Dropdown(
        label="Número do Quarto",
        options=[
            ft.dropdown.Option("101"),
            ft.dropdown.Option("201"),
            ft.dropdown.Option("301"),
            ft.dropdown.Option("401"),
        ],
        bgcolor=ft.colors.ON_TERTIARY,
        color=ft.colors.TERTIARY
    )

    botao_quarto = ft.ElevatedButton(text="Adicionar Quarto", bgcolor=ft.colors.CYAN_ACCENT_700, color=ft.colors.WHITE, on_click=button_clicked_quarto, style=ft.ButtonStyle(
        text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)))
    texto_quarto = ft.Text()

    tab_clientes = ft.Tab(
        text="Clientes",
        content=ft.Container(
            content=ft.Column(
                controls=[nome, cpf, email, botao_cliente],
                alignment=ft.MainAxisAlignment.START
            ),
            padding=20
        ),
    )

    tab_quartos = ft.Tab(
        text="Quartos",
        content=ft.Container(
            content=ft.Column(
                controls=[dropdown_tipo_quarto, dropdown_quartos_reserva, botao_quarto, texto_quarto],
                alignment=ft.MainAxisAlignment.START
            ),
            padding=20
        ),
    )

    dropdown_clientes = ft.Dropdown(
        label="Selecionar Cliente",
        options=[],
        bgcolor=ft.colors.ON_TERTIARY,
        color=ft.colors.TERTIARY
    )

    data_entrada = ft.TextField(label="Data de Entrada", hint_text="Clique para selecionar", bgcolor=ft.colors.ON_TERTIARY, color=ft.colors.TERTIARY, read_only=True)
    data_saida = ft.TextField(label="Data de Saída", hint_text="Clique para selecionar", bgcolor=ft.colors.ON_TERTIARY, color=ft.colors.TERTIARY, read_only=True)

    botao_reserva = ft.ElevatedButton(text="Registrar Reserva", bgcolor=ft.colors.CYAN_ACCENT_700, color=ft.colors.WHITE, on_click=button_clicked_reserva, style=ft.ButtonStyle(
        text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)))

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Cliente")),
            ft.DataColumn(ft.Text("CPF")),
            ft.DataColumn(ft.Text("E-mail")),
            ft.DataColumn(ft.Text("Data de Entrada")),
            ft.DataColumn(ft.Text("Data de Saída")),
            ft.DataColumn(ft.Text("Tipo de Quarto")),
            ft.DataColumn(ft.Text("Número do Quarto")),
            ft.DataColumn(ft.Text("Ação")),
        ],
        rows=[],
    )

    tab_reservas = ft.Tab(
        text="Reservas",
        content=ft.Container(
            content=ft.Column(
                controls=[
                    dropdown_clientes,
                    ft.Row(controls=[data_entrada, ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=open_date_picker_entrada)]),
                    ft.Row(controls=[data_saida, ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=open_date_picker_saida)]),
                    botao_reserva,
                    texto_quarto,
                    data_table
                ],
                alignment=ft.MainAxisAlignment.START
            ),
            padding=20
        ),
    )
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[tab_clientes, tab_quartos, tab_reservas],
        expand=1,
    )

    page.add(tabs)


ft.app(main)
