import flet as ft
from utils.utils import create_app_bar
class SignUpView:
    def __init__(self, page: ft.Page, on_signup, go_back):
        self.page = page
        self.on_signup = on_signup
        self.on_back = go_back
        self.page.window_resizable=False
        self.setup_page()
        self.signup_page_ui()
        self.page.add(create_app_bar("Sign Up", go_back))

    def setup_page(self):
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width = 350
        self.page.window_height = 450
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = 'Signup'
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def signup_page_ui(self):
        self.page.controls.clear() 
        
        lb_login = ft.Text(
        "Autenticação de usuário testeee",
        size=12,
        color=ft.colors.BLACK,
        weight=ft.FontWeight.BOLD,
        )

        tf_usuario = ft.TextField(
            label='Usuário',
            hint_text= 'Usuário',
            text_size=12,
            color=ft.colors.BLACK,
        )

        tf_senha = ft.TextField(

            label='Senha',
            hint_text = 'Senha',
            text_size=12,
            color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True
        )

        bt_signup = ft.ElevatedButton(
            "Sign Up",
            on_click=lambda e: self.on_signup(tf_usuario.value, tf_senha.value),
            width=120,
            height=50
        )


        self.page.add(lb_login, tf_usuario, tf_senha, bt_signup)
        self.page.update()


