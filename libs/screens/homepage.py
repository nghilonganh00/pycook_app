from kivy.app import App
from kivymd.uix.screen import MDScreen
import requests

from libs.components.ingredientCard import IngredientCard
from libs.components.hashtag import Hashtag
from libs.components.foodCard import FoodCard


class HomePage(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.first_time = True
        self.foods = []
        self.ingredient = []

    def on_enter(self):
        app = App.get_running_app()

        if self.first_time:
            self.first_time = False

            # -------- Get Ingredient list from server----------
            ingredients = []
            try:
                api_url = "http://localhost:5000/api/ingredient/getAll"
                response = requests.get(api_url)

                if response.status_code == 200:
                    self.ingredients = response.json()
                else:
                    print("Loi dang nhap")
            except Exception as e:
                print(e)

            ingredient_list_first = self.ids.ingredient_list_first
            for ingredient in self.ingredients:
                ingredient_card = IngredientCard(
                    ingredientName=ingredient["ingredientName"],
                    ingredientImage=ingredient["ingredientImage"],
                    ingredientId=ingredient["ingredientId"],
                )
                ingredient_list_first.add_widget(ingredient_card)

            # -------- Get Hashtag list from server----------
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
                hashtag_tab = Hashtag(hashtagName=hashtag["hashtagName"])
                hashtag_list.add_widget(hashtag_tab)

            # -------- Get Food list by Hashtag----------
            foods = []
            try:
                api_url = "http://localhost:5000/api/food/getAll"
                response = requests.get(api_url)

                if response.status_code == 200:
                    foods = response.json()
            except Exception as e:
                print(e)

            food_by_hashtag = self.ids.food_by_hashtag
            food_by_hashtag.clear_widgets()
            for food in foods:
                food_card = FoodCard(
                    foodId=food["foodId"],
                    foodName=food["foodName"],
                    foodImage=food["foodImage"],
                    chefAvatar=food["chef"]["avatar"],
                    chefFullname=food["chef"]["fullname"],
                    chefPycookID=food["chef"]["pycookID"],
                    heartTotal=food["heartTotal"],
                    likeTotal=food["likeTotal"],
                    deliciousTotal=food["deliciousTotal"],
                    createdDate=food["created_at"],
                )
                food_by_hashtag.add_widget(food_card)
