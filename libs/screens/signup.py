import requests
from kivy.app import App
from kivymd.uix.screen import MDScreen


class Signup(MDScreen):
    def signup(self):
        app = App.get_running_app()
        input_username = self.ids["input_email"].text
        input_password = self.ids["input_password"].text

        try:
            api_url = "http://localhost:5000/api/auth/signup"
            request_data = {
                "username": input_username,
                "password": input_password,
                "pycookID": "",
                "avatar": "",
                "fullname": "Pycook User",
            }
            response = requests.post(api_url, json=request_data)

            if response.status_code == 201:
                self.parent.current = "account"
                app.is_logged_in = True
                app.user = response.json()
            else:
                print("Loi dang nhap")
        except Exception as e:
            print(e)
