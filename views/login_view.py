import flet as ft
from utils.utils import create_app_bar

class LoginView:
    def __init__(self, page: ft.Page, on_login, on_signup, go_back):
        self.page = page
        self.on_login = on_login
        self.on_signup = on_signup
        self.on_back = go_back
        self.setup_page()
        self.login_page_ui()
        self.app_bar = create_app_bar("Login", go_back)
        #print(create_app_bar("Login", on_back))
        self.page.add(self.app_bar)

    def setup_page(self):
        self.page.controls.clear()
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width = 350
        self.page.window_height = 450
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = 'Login'
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  
        self.page.update()
        
    def login_page_ui(self):
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
            on_click=lambda e: self.on_login(tf_usuario.value, tf_senha.value),
            width=120,
            height=50
        )

        bt_criar = ft.TextButton(
            "Cadastrar-se",
            on_click=lambda _: self.on_signup(),
            width=120,
            height=50
        )

        self.page.add(lb_login, tf_usuario, tf_senha, bt_login, bt_criar)
        self.page.update()

