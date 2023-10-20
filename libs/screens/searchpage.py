from kivy.app import App
import requests
from kivy.properties import StringProperty

from kivymd.uix.screen import MDScreen
from libs.components.foodSearch import FoodSearch


class SearchPage(MDScreen):
    result_total = StringProperty("")

    def search_name(self):
        search_input = self.ids.search_input
        if search_input.text:
            try:
                api_url = "http://localhost:5000/api/food/getFoodByName"
                response = requests.get(
                    api_url, params={"searchName": search_input.text}
                )
                if response.status_code == 200:
                    result_foods = response.json()
                    result_food_box = self.ids.result_food_box
                    self.result_total = str(len(result_foods))
                    for food in result_foods:
                        food_box = FoodSearch(
                            foodId=food['foodId'],
                            foodName=food["foodName"],
                            foodImage=food["foodImage"],
                            recipes=food["recipes"],
                            chefAvatar=food["chef"]["avatar"],
                            chefFullname=food["chef"]["fullname"],
                        )
                        result_food_box.add_widget(food_box)
            except Exception as e:
                print("Lỗi: ", e)
