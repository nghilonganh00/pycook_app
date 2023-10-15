from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, ObjectProperty, NumericProperty

from kivy.app import App
class SmallFoodCard(MDBoxLayout):
    foodId = 0
    foodName = StringProperty('')
    foodImage = ObjectProperty(None)
    deliciousTotal = StringProperty('')
    heartTotal = StringProperty('')
    likeTotal = StringProperty('')
    def __init__(self, foodId, foodName, foodImage, deliciousTotal, heartTotal, likeTotal,**kwargs):
        super(SmallFoodCard, self).__init__(**kwargs)
        self.foodId = foodId
        self.foodName = foodName
        self.foodImage = foodImage
        self.deliciousTotal = str(deliciousTotal)
        self.heartTotal = str(heartTotal)
        self.likeTotal = str(likeTotal)
    
    def on_click_food(self):
        app = App.get_running_app()
        app.manager.current = 'detailFood'
        detailFood = app.manager.get_screen('detailFood')
        detailFood.foodId = self.foodId