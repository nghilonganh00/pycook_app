import requests
from libs.components.foodCard import FoodCard
from kivy.app import App

from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, ObjectProperty
class IngredientCard(MDCard):
    ingredientId = 0
    ingredientName = StringProperty("")
    ingredientImage = ObjectProperty(None)
    clicked = False


    def __init__(self, ingredientName, ingredientImage, ingredientId, **kwargs):
        super(IngredientCard, self).__init__(**kwargs)
        self.ingredientId = ingredientId
        self.ingredientName = ingredientName
        self.ingredientImage =  ingredientImage
    
    def on_click_ingredient(self):
        app = App.get_running_app()
        homepage = app.manager.get_screen('homepage')
        ingredient_list_first = homepage.ids.ingredient_list_first
        for ingredient in ingredient_list_first.children:
            if ingredient == self:
                # Nếu đây là box được nhấp chuột
                if not self.clicked:
                    self.md_bg_color = (236/255, 111/255, 44/255, 1)
                    self.clicked = True
                    #-------- Get Food list by Hashtag----------
                    foods = []
                    try:
                        api_url = "http://localhost:5000/api/food/getByIngredientName"
                        response = requests.get(api_url, params={'ingredientName': self.ingredientName})
                        
                        if response.status_code == 200:
                            foods = response.json()
                    except Exception as e:
                        print(e)

                    food_by_hashtag =  homepage.ids.food_by_hashtag
                    food_by_hashtag.clear_widgets()
                    for food in foods:
                        food_card = FoodCard(foodId=food['foodId'], foodName=food['foodName'], foodImage=food['foodImage'], chefAvatar=food['chef']['avatar'], chefFullname=food['chef']['fullname'], chefPycookID=food['chef']['pycookID'], heartTotal=food['heartTotal'], likeTotal=food['likeTotal'], deliciousTotal=food['deliciousTotal'], createdDate=food['created_at'])
                        food_by_hashtag.add_widget(food_card)
            else:
                ingredient.md_bg_color = (119/255,120/255,115/255,255/255)
                ingredient.clicked = False
            
        