from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
# from kivymd.uix.tab import 

from libs.components.ingredientCard import IngredientCard
import requests

class HomePage(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.first_time = True # Kiem tra day co phai lan dau truy cap vao Homepage

    def on_enter(self):
        app = App.get_running_app()

        if self.first_time:
            self.first_time = False

            #-------- Get Ingredient list from server----------
            ingredient_list = []
            try:
                api_url = "http://localhost:5000/api/ingredient/getAll"
                response = requests.get(api_url)
                
                if response.status_code == 200:
                    ingredient_list = response.json()
                else:
                    print("Loi dang nhap")
            except Exception as e:
                print(e)
            
            ingredient_list_first = self.ids.ingredient_list_first
            for ingredient in ingredient_list:
                ingredient_card = IngredientCard(ingredientName = ingredient['ingredientName'], ingredientImage=ingredient['blobImage'])
                ingredient_list_first.add_widget(ingredient_card)
            
            #-------- Get Tabs list from server----------
            try:
                api_url = "http://localhost:5000/api/tab/getAll"
                response = requests.get(api_url)
                
                if response.status_code == 200:
                    tab_list = response.json()
            except Exception as e:
                print(e)

            tabs = self.ids.tabs
            for tab in tab_list:
                tab_card = MDTab(ingredientName = ingredient['ingredientName'], ingredientImage=ingredient['blobImage'])
                ingredient_list_first.add_widget(ingredient_card)
            


        # Account bottom nav item
        if app.is_logged_in:
            bottom_navigation = self.ids.bottom_navigation
            bottom_navigation.remove_widget(self.ids.account_item)

            icon_button = MDIconButton(
                id='account',
                pos_hint={'center_x': .9, 'center_y': 0.5},
                icon='facebook',
                theme_text_color='Custom',
                color=(1, 1, 1, 1),  # Màu trắng
                font_size=36
            )
            avatar = Image(
                source = "assets/image/avatar/mai_ngo.png"
            )
            icon_button.add_widget(avatar)
            bottom_navigation.add_widget(icon_button)

