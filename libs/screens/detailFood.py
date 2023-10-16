import requests
import json
from utils.formatTimeDifference import conver_date_fotmat

from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ObjectProperty, NumericProperty

from libs.components.recipe import Recipe
from libs.components.makingBox import MakingBox
from libs.components.comment import Comment
from libs.components.smallerFoodCard import SmallerFoodCard


class DetailFood(MDScreen):
    foodName = StringProperty("")
    foodImage = ObjectProperty(None)
    foodDescription = StringProperty('')
    foodNation = StringProperty('')
    foodTime = StringProperty('')
    servingFor = StringProperty('')
    chefAvatar = ObjectProperty(None)
    chefFullname = StringProperty('')
    chefPycookId = StringProperty('')
    createdDate = StringProperty('')
    heartTotal = StringProperty('')
    likeTotal = StringProperty('')
    deliciousTotal = StringProperty('')
    comments = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.foodId = 1
        
    def on_enter(self):
        app = App.get_running_app()

        #-------- Get Food Detail from server----------
        food = []
        recipes = []
        makings = []
        comments = []
        try:
            api_url = "http://localhost:5000/api/food/getByFoodId"
            response = requests.get(api_url, params = {'foodId': self.foodId})
            
            if response.status_code == 200:
                food = response.json()
                self.foodName = food['foodName']
                self.foodImage = food['foodImage']
                self.foodDescription = food['foodDescription']
                self.foodTime = str(food['foodTime'])
                self.servingFor = str(food['servingFor'])
                self.foodNation = food['foodNation']
                chefId = food['chef']['id']
                self.chefAvatar = food['chef']['avatar']
                self.chefFullname = food['chef']['fullname']
                self.chefPycookId = food['chef']['pycookID']
                recipes = food['recipes']
                makings = food['makings']
                self.createdDate = conver_date_fotmat(food['created_at'])
                self.heartTotal = str(food['heartTotal'])
                self.likeTotal = str(food['likeTotal'])
                self.deliciousTotal = str(food['deliciousTotal'])
                comments = food['comments']
            else:
                print("Loi dang nhap")
        except Exception as e:
            print(e)
        
        # Recipes of Food
        recipes_box = self.ids.recipes
        children = self.ids.recipes.children

        self.ids.recipes.clear_widgets()
        for recipe in recipes:
            recipe_label = Recipe(
                ingredientName=recipe
            )
            recipes_box.add_widget(recipe_label)
        
        # Making of Food
        makings_box = self.ids.makings
        children = self.ids.makings.children

        self.ids.makings.clear_widgets()
        for making in makings:
            making_box = MakingBox(
                makingOrder=making['makingOrder'],
                makingContent=making['makingContent']
            )
            makings_box.add_widget(making_box)
        
        # Comment of Food
        comments_box = self.ids.comments
        children = self.ids.comments.children

        self.ids.comments.clear_widgets()
        for comment in comments:
            print(comment['content'])
            comment_box = Comment(
                userAvatar = comment['userAvatar'],
                userFullname = comment['userFullname'],
                userPycookID = comment['userPycookId'],
                commentContent = comment['content']
            )
            comments_box.add_widget(comment_box)




        #-------- Get Chef's lastest Food from server----------
        try:
            api_url = "http://localhost:5000/api/food/getLastestByUserId"
            response = requests.get(api_url, params = {'userId': chefId})
            lastest_foods = self.ids.lastest_foods
            children = self.ids.lastest_foods.children

            self.ids.lastest_foods.clear_widgets()

            if response.status_code == 200:
                lastest_foods_res = response.json()
                for lastest_food in lastest_foods_res:
                    smaller_food_card = SmallerFoodCard(
                        foodId=lastest_food['foodId'], 
                        foodName=lastest_food['foodName'], 
                        foodImage=lastest_food['foodImage']
                    )
                    lastest_foods.add_widget(smaller_food_card)
                
            else:
                print("Loi dang nhap")
        except Exception as e:
            print(e)



    def on_like_click(self):
        try:
            api_url = "http://localhost:5000/api/food/like"
            response = requests.get(api_url, params={'foodId': self.foodId})
            
            if response.status_code == 200:
                self.likeTotal = str(response.json())
        except Exception as e:
            print(e)
    def send_comment(self):
        app = App.get_running_app()
       
        # if not app.user:
        #     self.manager.current = 'login'
        #     return
        comment_input = self.ids.comment_input
        comment_res = {
            'userId': 1,
            'foodId': self.foodId,
            'commentContent': comment_input.text
            
        }
        try:
            api_url = "http://localhost:5000/api/comment/create"
            response = requests.post(api_url, json=comment_res)
            comments = self.ids.comments
            
            if response.status_code == 201:
                comment_box = Comment(
                        userAvatar = 'assets/image/avatar/mai_ngo.png',
                        userFullname = str(self.foodId),
                        userPycookID = 'pycook_124934',
                        commentContent = comment_input.text
                    )
                comments.add_widget(comment_box)
                
        except Exception as e:
            print(e)
    