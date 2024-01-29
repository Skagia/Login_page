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

def msg_erro(msg, open):
    banner = ft.Banner(
        open=open,
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(
            ft.icons.DANGEROUS_SHARP,
            color=ft.colors.RED_400,
            size=40
            ),
        content=ft.Text(msg,
                        color=ft.colors.BLACK,
                        size=10
                ),
        )
    return banner

