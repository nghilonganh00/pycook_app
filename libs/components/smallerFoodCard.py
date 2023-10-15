from kivy.app import App
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, ObjectProperty, NumericProperty


class SmallerFoodCard(MDBoxLayout):
    foodId = None
    foodImage = ObjectProperty(None)
    foodName = StringProperty("")

    def __init__(self, foodId, foodName, foodImage, **kwargs):
        super(SmallerFoodCard, self).__init__(**kwargs)
        self.foodId = foodId
        self.foodName = foodName
        self.foodImage = foodImage

    def on_click_lastest_food(self):
        app = App.get_running_app()
        app.manager.current = "detailFood"
        detailFood = app.manager.get_screen("detailFood")
        detailFood.foodId = self.foodId
        detailFood.on_enter()
        print(self.foodId)
