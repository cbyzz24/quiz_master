import flet as ft
from flet_route import Params,Basket

class HomeView:
    def __init__(self):
        ...

    def view(self,page:ft.page,params:Params,basket:Basket):
        print(params)
        print(basket)

        return ft.View(
            "/",
            controls=[
                ft.Container(
                    height=750, width=800,
                    bgcolor="#27374D",
                    # padding=200,
                    content=ft.Row(
                        alignment = ft.MainAxisAlignment.CENTER,
                        vertical_alignment = ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("WELCOME!", size=26, color='white'),
                            ft.Text("Choose A Subject", size=18, color="white"),
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(text="Civics", on_click=lambda _: page.go("/civics/10")),
                                    ft.PopupMenuItem(text="History", on_click=lambda _: page.go("/history/11")),
                                ]
                            )
                            # ft.ElevatedButton("Go Next View", on_click=lambda _: page.go("/next_view/10")),
                        ]
                    )
                )
            ]
        )
