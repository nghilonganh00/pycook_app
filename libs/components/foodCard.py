from utils.formatTimeDifference import format_time_difference


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

    def __init__(self, foodName, foodImage, chefAvatar, chefFullname, chefPycookID, heartTotal, likeTotal, deliciousTotal, createdDate, **kwargs):
        super(FoodCard, self).__init__(**kwargs)
        self.foodName = foodName
        self.foodImage = foodImage
        self.chefAvatar = chefAvatar
        self.chefFullname = chefFullname
        self.chefPycookID = chefPycookID
        self.heartTotal = str(heartTotal)
        self.likeTotal = str(likeTotal)
        self.deliciousTotal = str(deliciousTotal)
        self.createdDate = format_time_difference(createdDate)