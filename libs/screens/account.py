import requests

from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ObjectProperty, NumericProperty

from libs.components.smallFoodCard import SmallFoodCard
class Account(MDScreen):
    fullname = StringProperty('')
    avatar = ObjectProperty(None)
    pycookID = StringProperty('')

    def on_enter(self):
        app = App.get_running_app()
        if app.user:
            self.fullname = app.user.get('fullname', '')
            self.avatar = app.user['avatar']
            self.pycookID = app.user['pycookID']

            my_food = self.ids.my_food
            my_food_total = self.ids.my_food_total

            my_food_total.text = 'Món ăn của tôi (' + str(len(app.user['foods'])) + ')'
            my_food.clear_widgets()
            for food in app.user['foods']:
                small_food_card = SmallFoodCard(
                    foodId=food['foodId'], 
                    foodName=food['foodName'], 
                    foodImage=food['foodImage'], 
                    deliciousTotal=food['deliciousTotal'],
                    heartTotal=food['heartTotal'],
                    likeTotal=food['likeTotal'],
                )
                my_food.add_widget(small_food_card)