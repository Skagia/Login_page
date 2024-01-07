import flet as ft
from views.signup_view import SignUpView

class SignUpController:
    def __init__(self, page: ft.Page, app):
        self.page = page
        self.app = app
        self.view = SignUpView(page, self.handle_signup, self.on_back)

    def handle_signup(self, username, password):
        print("voce clicou em se inscrever")

    def on_back(self, event):
        # Logic to navigate back
        self.app.navigate("/")
        print("voce clicou para voltar")
