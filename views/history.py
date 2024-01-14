import flet as ft
from flet_route import Params,Basket

class HistoryView:
    def __init__(self):
        ...

    def view(self,page:ft.page,params:Params,basket:Basket):
        print(params)
        print(basket)

        return ft.View(
            "/history/:my_id",
            controls=[
                # ft.Text("This Is Next View"),
                # ft.ElevatedButton("Go Index View", on_click=lambda _: page.go("/")),
                ft.Container(
                    height=750, width=800,
                    bgcolor="#27374D",
                    padding=20,
                    content=ft.Column(
                        horizontal_alignment="center",
                        controls=[
                            ft.Text("History", color="white", size=25),
                            ft.Container(
                                ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(text="Home", on_click=lambda _: page.go("/")),
                                    ft.PopupMenuItem(text="Civics", on_click=lambda _: page.go("/civics/10")),
                                ]
                            )
                               
                            ),
                            
                            ft.Container(
                                width=600,
                                height=250,
                                bgcolor='#526D82',
                                padding=10,
                                margin=10,
                                border_radius=6,
                                content=ft.Column(
                                    horizontal_alignment="center",
                                    controls=[
                                        ft.Text("Question:", color="white", size=20),
                                        ft.Container(
                                            padding=10,
                                            height=240,
                                            content=ft.Text("Content Displayed Here", color="white", size=20,),
                                        ),
                                        
                                    ]
                                )
                            ),

                            ft.Container(
                                content=(
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            ft.ElevatedButton(text="Next Question", color="white", width=160, bgcolor="#00818A"),
                                            ft.ElevatedButton(text="Display Answer", color="white", width=160, bgcolor="#00818A"),
                                        ]
                                    )
                                )
                            ),

                            ft.Container(
                                width=600,
                                height=250,
                                bgcolor='#526D82',
                                padding=10,
                                margin=10,
                                border_radius=6,
                                content=ft.Column(
                                    horizontal_alignment="center",
                                    controls=[
                                        ft.Text("Answer:", color="white", size=20),
                                        ft.Container(
                                            padding=10,
                                            height=240,
                                            content=ft.Text("Content Displayed Here", color="white", size=20,),
                                        ),
                                        
                                    ]
                                )
                            ),

                        ]
                    )
                )
            ]
        )
