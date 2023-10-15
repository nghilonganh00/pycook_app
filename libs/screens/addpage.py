import requests
from kivy.app import App
from kivymd.uix.screen import MDScreen

from libs.components.ingredientInput import IngredientInput
from libs.components.makingInput import MakingInput

from utils.converImage import converImageToBase64
class AddPage(MDScreen):
    ingredientTotal = 1
    makingTotal = 1
    def submit_food(self):
        app = App.get_running_app()
        userId = app.user['userId'] if app.user else None
        foodName = self.ids.food_name_input.text
        foodImage = converImageToBase64(app.manager.get_screen('addpage').ids.file_chooser_box.added_image_path)
        foodDescription = self.ids.food_description_input.text
        foodNation = self.ids.food_nation_input.text
        foodTime = self.ids.food_time_input.text
        servingFor = self.ids.serving_for_input.text

        recipes = [children.ids['ingredient_input'].text for children in self.ids['ingredient_input_list'].children]
        makings = [{
            'content':children.ids['making_input'].text, 
            'image': ''
        } for children in self.ids['making_input_list'].children]

        if userId and foodName and foodImage:
            try:
                api_url = "http://localhost:5000/api/food/create"
                request_data = {
                    "userId": userId, 
                    "foodName": foodName,
                    'foodImage': foodImage,
                    'foodDescription': foodDescription,
                    'foodNation': foodNation,
                    'foodTime': foodTime,
                    'servingFor': servingFor,
                    'recipes': recipes,
                    'makings': makings
                }
                response = requests.post(api_url, json=request_data)
                
                if response.status_code == 201:

                    app.root.current = 'detailFood'
                    detailFood = app.manager.get_screen('detailFood')
                    detailFood.foodId = response.json().foodId
                else:
                    print("Loi dang nhap")
            except Exception as e:
                print(e)

    def add_ingredient_input(self):
        ingredient_input_list = self.ids.ingredient_input_list
        ingredient_input_list.add_widget(IngredientInput(ingredientId=self.ingredientTotal))
        self.ingredientTotal += 1

    def add_making_input(self):
        making_input_list = self.ids.making_input_list
        making_input_list.add_widget(MakingInput(makingId=self.makingTotal))
        self.makingTotal += 1
