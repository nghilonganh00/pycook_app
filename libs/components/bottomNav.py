from kivymd.uix.floatlayout import MDFloatLayout
from kivy.app import App


class BottomNav(MDFloatLayout):
    def on_click_account(self):
        app = App.get_running_app()
        if app.user:
            app.root.current = 'account'
        else:
            app.root.current = 'login'

