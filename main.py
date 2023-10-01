from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase

from libs.screens.login import Login
from libs.screens.homepage import HomePage
from libs.screens.account import Account

Window.size = (284, 604)

kv = """

"""

class Tab(MDBoxLayout, MDTabsBase):
    pass
    

class PyCook(MDApp):
    is_logged_in = False
    def build(self):
        self.load_all_kv_files()
        self.manager = ScreenManager(transition = NoTransition())
        self.manager.add_widget(Account(name = "account"))
        self.manager.add_widget(HomePage(name = "homepage"))
        self.manager.add_widget(Login(name = "login"))
        return self.manager 
        
    def load_all_kv_files(self):
        Builder.load_file("libs\\components\\ingredientCard.kv")
        
        Builder.load_file("libs\\screens\\account.kv")
        Builder.load_file("libs\\screens\\homepage.kv")
        Builder.load_file("libs\\screens\\login.kv")


if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="C:\\Users\\ASUS\\OneDrive\\Máy tính\\Social Media\\assets\\font\\Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="C:\\Users\\ASUS\\OneDrive\\Máy tính\\Social Media\\assets\\font\\Poppins-Bold.ttf")
    LabelBase.register(name="BkRoboto", fn_regular="C:\\Users\\ASUS\\OneDrive\\Máy tính\\PyCook 2\\assets\\fonts\\Roboto-Black.ttf")
    LabelBase.register(name="BRoboto", fn_regular="C:\\Users\\ASUS\\OneDrive\\Máy tính\\PyCook 2\\assets\\fonts\\Roboto-Bold.ttf")
    LabelBase.register(name="LRoboto", fn_regular="C:\\Users\\ASUS\\OneDrive\\Máy tính\\PyCook 2\\assets\\fonts\\Roboto-Light.ttf")
    LabelBase.register(name="MRoboto", fn_regular="C:\\Users\\ASUS\\OneDrive\\Máy tính\\PyCook 2\\assets\\fonts\\Roboto-Medium.ttf")
    LabelBase.register(name="RRoboto", fn_regular="C:\\Users\\ASUS\\OneDrive\\Máy tính\\PyCook 2\\assets\\fonts\\Roboto-Regular.ttf")
    LabelBase.register(name="TRoboto", fn_regular="C:\\Users\\ASUS\\OneDrive\\Máy tính\\PyCook 2\\assets\\fonts\\Roboto-Thin.ttf")
    PyCook().run()