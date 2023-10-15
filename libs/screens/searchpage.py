from kivy.app import App
import requests
from kivy.properties import StringProperty

from kivymd.uix.screen import MDScreen
from libs.components.foodSearch import FoodSearch

class SearchPage(MDScreen):
    result_total = StringProperty('')

    def search_name(self):
        search_input = self.ids.search_input
        result_food = []
        if search_input.text:
            try:
                api_url = "http://localhost:5000/api/food/getFoodByName"
                response = requests.get(api_url, params={'searchName': search_input.text})
                result_box = self.ids.result_food
                
                if response.status_code == 200:
                    result_food = response.json()
                    self.result_total = str(len(result_food))
                    for food in result_food:
                        food_box = FoodSearch(
                            foodName = food['foodName'],
                            foodImage = food['foodImage'],
                            recipe = food['recipe'],
                            chefAvatar = food['chef']['avatar'],
                            chefFullname = food['chef']['fullname']
                        )
                        result_box.add_widget(food_box)
            except Exception as e:
                print(e)