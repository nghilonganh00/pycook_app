from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivymd.uix.button import MDIconButton
import requests

from libs.components.ingredientCard import IngredientCard
from libs.components.hashtag import Hashtag
from libs.components.foodCard import FoodCard

class HomePage(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.first_time = True

    def on_enter(self):
        app = App.get_running_app()

        if self.first_time:
            self.first_time = False

            #-------- Get Ingredient list from server----------
            ingredients = []
            try:
                api_url = "http://localhost:5000/api/ingredient/getAll"
                response = requests.get(api_url)
                
                if response.status_code == 200:
                    ingredients = response.json()
                else:
                    print("Loi dang nhap")
            except Exception as e:
                print(e)
            
            ingredient_list_first = self.ids.ingredient_list_first
            for ingredient in ingredients:
                ingredient_card = IngredientCard(ingredientName = ingredient['ingredientName'], ingredientImage=ingredient['ingredientImage'])
                ingredient_list_first.add_widget(ingredient_card)
            
            #-------- Get Hashtag list from server----------
            hashtags = []
            try:
                api_url = "http://localhost:5000/api/hashtag/getAll"
                response = requests.get(api_url)
                
                if response.status_code == 200:
                    hashtags = response.json()
            except Exception as e:
                print(e)

            hashtag_list = self.ids.hashtag_list
            for hashtag in hashtags:
                hashtag_tab = Hashtag(hashtagName=hashtag['hashtagName'])
                hashtag_list.add_widget(hashtag_tab)
            
            #-------- Get Food list by Hashtag----------
            foods = []
            try:
                api_url = "http://localhost:5000/api/food/getAll"
                response = requests.get(api_url)
                
                if response.status_code == 200:
                    foods = response.json()
            except Exception as e:
                print(e)

            food_by_hashtag = self.ids.food_by_hashtag
            for food in foods:
                food_card = FoodCard(foodName=food['foodName'], foodImage=food['foodImage'], chefAvatar=food['chef']['avatar'], chefFullname=food['chef']['fullname'], chefPycookID=food['chef']['pycookID'], heartTotal=food['heartTotal'], likeTotal=food['likeTotal'], deliciousTotal=food['deliciousTotal'], createdDate=food['created_at'])
                food_by_hashtag.add_widget(food_card)


        # Account bottom nav item
        if app.is_logged_in:
            bottom_navigation = self.ids.bottom_navigation
            bottom_navigation.remove_widget(self.ids.account_item)

            icon_button = MDIconButton(
                id='account',
                pos_hint={'center_x': .9, 'center_y': 0.5},
                icon='facebook',
                theme_text_color='Custom',
                font_size=36
            )
            avatar = Image(
                source = app.user['avatar']
            )
            icon_button.add_widget(avatar)
            bottom_navigation.add_widget(icon_button)
