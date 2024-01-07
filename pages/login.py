import flet as ft
import sqlite3


class Login:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate
        self.setup_page()
        self.loginPage()

    def setup_page(self):
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width = 350
        self.page.window_height = 450
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = 'Login'
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def __entrar(self, e, usuario, senha):
        if usuario == "" or senha == "":
            print("As informações de login e senha devem ser preenchidas")
        else:
            # Fazer verificações do banco de dados
            pass

    def cadastrarUsuario(self, e):
       self.navigate("/signup")

        
    def loginPage(self):
        self.page.controls.clear()

        lb_login = ft.Text(
            "Autenticação de usuário",
            size=12,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD,
        )

        tf_usuario = ft.TextField(
            label='Usuário',
            hint_text='Usuário',
            text_size=12,
            color=ft.colors.BLACK,
        )

        tf_senha = ft.TextField(
            label='Senha',
            hint_text='Senha',
            text_size=12,
            color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True
        )

        bt_login = ft.ElevatedButton(
            "Login",
            on_click=lambda e: self.__entrar(e, tf_usuario.value, tf_senha.value),
            width=120,
            height=50
        )

        bt_criar = ft.TextButton(
            "Cadastrar-se",
            on_click=lambda e: self.cadastrarUsuario(e),
            width=120,
            height=50
        )

        self.page.add(lb_login, tf_usuario, tf_senha, bt_login, bt_criar)
        self.page.update()