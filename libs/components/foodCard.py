from utils.formatTimeDifference import format_time_difference

from kivy.app import App
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, ObjectProperty, NumericProperty

class FoodCard(MDBoxLayout):
    foodName = StringProperty("")
    foodImage = ObjectProperty(None)
    chefAvatar = ObjectProperty(None)
    chefFullname = StringProperty("")
    chefPycookID = StringProperty("")
    heartTotal = StringProperty()
    likeTotal = StringProperty()
    deliciousTotal = StringProperty("")
    createdDate = StringProperty("")

    def __init__(self, foodId, foodName, foodImage, chefAvatar, chefFullname, chefPycookID, heartTotal, likeTotal, deliciousTotal, createdDate, **kwargs):
        super(FoodCard, self).__init__(**kwargs)
        self.foodId = foodId
        self.foodName = foodName
        self.foodImage = foodImage
        self.chefAvatar = chefAvatar
        self.chefFullname = chefFullname
        self.chefPycookID = chefPycookID
        self.heartTotal = str(heartTotal)
        self.likeTotal = str(likeTotal)
        self.deliciousTotal = str(deliciousTotal)
        self.createdDate = format_time_difference(createdDate)
    
    def on_click_food(self):
        app = App.get_running_app()
        
        app.root.current = 'detailFood'
        detailFood = app.manager.get_screen('detailFood')
        detailFood.foodId = self.foodId