from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton
from kivymd.uix.screen import Screen

class MyApp(MDApp):
    def build(self):
        screen = Screen()
        btn_flat = MDIconButton(icon='android', pos_hint={'center_x':.5, 'center_y':.5})
        screen.add_widget(btn_flat)
        return screen

MyApp().run()
