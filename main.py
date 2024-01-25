from colorschemes import color_schemes_colours
import random
import flet as ft

width = None
height = None
color_schemes = ["Everblush", "Catppuccin Mocha"]
current_colorscheme = None


def main(page: ft.Page):
    page.fonts = {
        "Symbols Nerd Font": "/fonts/SymbolsNerdFont-Regular.ttf",
        "Comfortaa": "/fonts/Comfortaa-Regular.ttf",
    }
    page.theme = ft.Theme(font_family="Comfortaa")

    def add_blocks():
        global width, height, current_colorscheme
        to_nones = []

        # reset
        stack_controls = []

        if not width:
            width = random.randint(0, int(page.width / 4))
            to_nones.append("width")
        if not height:
            height = random.randint(0, int(page.height / 4))
            to_nones.append("height")
        if not current_colorscheme or current_colorscheme == "Random":
            current_colorscheme = random.choice(color_schemes)
            to_nones.append("clr")

        page.bgcolor = color_schemes_colours[current_colorscheme][0]
        for color in color_schemes_colours[current_colorscheme][1:]:
            top = random.randint(0, int(page.height / 1.5))
            left = random.randint(0, int(page.width / 1.5))
            stack_controls.append(
                ft.Container(
                    bgcolor=color, width=width, height=height, top=top, left=left
                )
            )

        page.controls = [ft.SafeArea(ft.Stack(stack_controls))]
        page.update()

        for to_none in to_nones:
            if to_none == "width":
                width = None
                continue
            elif to_none == "height":
                height = None
                continue
            elif to_none == "clr":
                current_colorscheme = None
                continue

    def get_width(e):
        global width
        width = e.control.value

    def get_height(e):
        global height
        height = e.control.value

    def get_color_scheme():
        global current_colorscheme
        if not color_schemes_dropdown.value:
            current_colorscheme = random.choice(color_schemes)
        else:
            current_colorscheme = color_schemes_dropdown.value

    def on_hover(e):
        e.control.content.color = "gray" if e.data == "true" else "#ffffff"
        page.update()

    width_field = ft.TextField(on_change=get_width, width=200)
    height_field = ft.TextField(on_change=get_height, width=200)
    color_schemes_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option(color_scheme_name) for color_scheme_name in color_schemes
        ] + [ft.dropdown.Option("Random")],
        on_change=lambda _: get_color_scheme(),
        width=200,
    )

    page.appbar = ft.Container(
        ft.Row(
            [
                ft.Row(
                    [
                        ft.Row([ft.Text("Width:"), width_field]),
                        ft.Row([ft.Text("Height:"), height_field]),
                        ft.Row(
                            [
                                ft.Text("Color Scheme:"),
                                color_schemes_dropdown,
                            ]
                        ),
                        ft.IconButton(
                            icon=ft.icons.CHECK, on_click=lambda _: add_blocks()
                        ),
                    ],
                    spacing=40
                ),
                ft.Container(
                    ft.Text(value="", size=30, font_family="Symbols Nerd Font"),
                    on_click=lambda _: page.launch_url(
                        "https://github.com/taaaf11/uwu"  # todo: add github repo link
                    ),
                    on_hover=on_hover,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        margin=ft.margin.symmetric(horizontal=15),
    )

    get_color_scheme()
    page.bgcolor = color_schemes_colours[current_colorscheme][0]

    add_blocks()
    page.on_connect = lambda _: add_blocks()


ft.app(main, view=ft.WEB_BROWSER)
