import flet as ft
from PIL import Image, ImageTk


def create_app_bar(title, go_back):
    bt_back = ft.IconButton(
            ft.icons.ARROW_BACK,
            on_click=go_back,
            width=120,
            height=30
     )
    
    return ft.AppBar(
        title=ft.Text(title),
        leading=bt_back
    )