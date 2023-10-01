import requests
from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Builder.load_file("libs\screens\homepage.kv")
class Login(MDScreen):
    def login(self):
        app = App.get_running_app()
        input_email = app.manager.get_screen('login').ids['input_email'].text
        input_password = app.manager.get_screen('login').ids['input_password'].text
        
        self.loginApi(input_email, input_password)
    
    def loginApi(self, username, password):
        app = App.get_running_app()
        try:
            api_url = "http://localhost:5000/api/auth/login"
            request_data = {"username": username, "password": password}
            response = requests.post(api_url, json=request_data)
            
            print(request_data)
            if response.status_code == 200:
                self.parent.current = "homepage"
                app.is_logged_in = True
                # bottom_navigation.remove_widget(self.ids.account)
            else:
                print("Loi dang nhap")
        except Exception as e:
            print(e)
        