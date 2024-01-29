import flet as ft
from views.signup_view import SignUpView
from models.user_model import UserModel
from utils.utils import msg_erro
from db_manager import DatabaseManager


class SignUpController:
    def __init__(self, page: ft.Page, app):
        self.page = page
        self.app = app
        self.db_manager = DatabaseManager()
        self.view = SignUpView(page, self.add_user, self.on_back)
        
    def add_user(self, nome, sobrenome, email, telefone, senha, confirmasenha):
        dados_usuario = {
            'nome' : '',
            'sobrenome' : '',
            'email' : '',
            'telefone' : '',
            'password' : '',
            }
        dados_usuario['nome'] = nome
        dados_usuario['sobrenome'] = sobrenome
        dados_usuario['email'] = email
        dados_usuario['telefone'] = telefone
        dados_usuario['password'] = senha

        for val in dados_usuario.values():
            if not val:
                self.error("Todos os campos devem ser preenchidos")
                return
            if senha != confirmasenha:
                self.error("As senhas devem ser iguais")
                print("As senhas devem ser iguais")
                return
            else:
                novo_usuario = UserModel(dados_usuario, self.db_manager)
                try:
                    novo_usuario.add_userdb()
                    print("Usuário cadastrado com sucesso!")
                except ValueError as e:
                    self.error(str(e))
                break

        #ideias: criar check de senha avançado, criar confirmação de e-mail, criar () para DDD
            
    def on_back(self, event):
        # Logic to navigate back
        self.app.navigate("/")
        print("voce clicou para voltar")

    def close_error(self, e):
        self.banner.open = False
        self.banner.update()
        print('foi para a funcao close')

    def error(self, texto):
       self.banner = msg_erro(texto, True) 
       #Criei este viewer dentro do próprio controller, acredito que poderia cria-lo em outro local mais apropriado
       self.banner.actions=[
            ft.TextButton(
                content=ft.Container(
                    content=ft.Column(
                        [
                        ft.Text(value='Entendi',
                        size=10,
                        color=ft.colors.RED,
                            )                       
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=5,
                    ),
                    padding=ft.padding.all(10),
                ),
                on_click=lambda e: self.close_error(e)
            ),
        ]
       self.view.page.add(self.banner)

 

        