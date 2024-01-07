import flet as ft
from controllers.login_controller import LoginController
from controllers.signup_controller import SignUpController

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.route_to_controller = {
            "/": LoginController,
            "/signup": SignUpController,
            # ... other routes ...
        }
        self.history = []  # Navigation history
        self.navigate("/")

    def navigate(self, route):
        if route in self.route_to_controller:
            self.history.append(route)  # Add the route to the history
            controller_class = self.route_to_controller[route]
            controller = controller_class(self.page, self)
            print(route)
        else:
            print("Route not found:", route)
        
        self.history.append(route)

    def go_back(self, event):  # Accept the event parameter
        if len(self.history) > 1:
            self.history.pop()  # Remove current page from history
            previous_route = self.history[-1]
            self.navigate(previous_route)
            
        else:
            print("No previous page in history")

def main(page: ft.Page):
    App(page)

ft.app(target=main, view=ft.AppView.FLET_APP)