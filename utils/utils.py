import flet as ft

def create_app_bar(title, go_back):
    bt_back = ft.IconButton(
            icon=ft.icons.ARROW_BACK,
            on_click=go_back,
            width=120,
            height=50
     )
    

    return ft.AppBar(
        title=ft.Text(title),
        leading=bt_back
    )