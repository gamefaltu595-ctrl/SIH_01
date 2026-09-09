import flet as ft

def main(page: ft.Page):
    page.title = "flet project"
    text = ft.Text(value="Hello, World!", size=30)
    page.add(text)

ft.run(main)