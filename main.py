import flet as ft
from urllib.parse import urlparse
import sqlite3

from pages.login import Login
from pages.criarUsuario import SignUp

def main(page: ft.Page):

    def navigate(route):
        page.controls.clear()
        if route == "/signup":
            SignUp(page, navigate)
            
        else:  # Default to login page
            Login(page, navigate)

    navigate("/")

ft.app(target=main, view=ft.AppView.WEB_BROWSER)