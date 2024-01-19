import flet as ft


def main(page: ft.Page):
    page.title = "Hello World"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(ft.Text("Hello Tekle!"))
    page.bgcolor = ft.colors.BLUE_GREY_100
    

ft.app(main)
