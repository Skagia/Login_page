import flet as ft
from utils.utils import create_app_bar
from utils.utils import msg_erro

class SignUpView:
    def __init__(self, page: ft.Page, on_signup, on_back):
        self.page = page
        self.on_signup = on_signup
        self.on_back = on_back
        self.setup_page()
        self.signup_page_ui()
        self.page.add(create_app_bar("Sign Up", on_back))


    def setup_page(self):
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width = 350
        self.page.window_height = 600
        self.page.window_resizable = True
        self.page.window_always_on_top = True
        self.page.title = 'Signup'
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def signup_page_ui(self):
        self.page.controls.clear() 
        
        lb_cadastro = ft.Text(
        "Cadastro de usuário",
        size=12,
        color=ft.colors.BLACK,
        weight=ft.FontWeight.BOLD,
        )

        tf_firstname = ft.TextField(
            height=40,
            text_size=12,
            color=ft.colors.BLACK,
            label="Nome",
        )
        tf_lastname = ft.TextField( 
            height=40,
            text_size=12,
            label='Sobrenome',
            color=ft.colors.BLACK,
        )
        tf_email = ft.TextField(
            height=40,
            text_size=12,
            label='E-mail',
            color=ft.colors.BLACK,
        )
        tf_telefone = ft.TextField(
            label='Telefone',
            height=40,
            text_size=12,
            color=ft.colors.BLACK,
        )
        tf_password = ft.TextField(
            label='Crie sua senha',
            height=40,
            text_size=12,
            color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True
        )
        tf_confirmpassword = ft.TextField(
            label='Digite sua senha novamente',
            height=40,
            text_size=12,
            color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True
        )

        bt_signup = ft.ElevatedButton(
            "Sign Up",
            on_click=lambda e: self.on_signup(tf_firstname.value, tf_lastname.value, tf_email.value,
                                              tf_telefone.value, tf_password.value, tf_confirmpassword.value),
            width=120,
            height=40
        )


        self.page.add(
                      lb_cadastro, 
                      tf_firstname, 
                      tf_lastname, 
                      tf_email, 
                      tf_telefone, 
                      tf_password, 
                      tf_confirmpassword,
                      bt_signup)
        self.page.update()



    