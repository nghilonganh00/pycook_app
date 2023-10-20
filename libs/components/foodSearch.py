from kivymd.uix.card import MDCard
from kivy.core.image import Image as CoreImage
from kivy.properties import StringProperty, ObjectProperty


class FoodSearch(MDCard):
    foodName = StringProperty("")
    foodImage = ObjectProperty(None)
    recipes = StringProperty("")
    chefAvatar = ObjectProperty(None)
    chefFullname = StringProperty("")

    def __init__(self, foodId, foodName, foodImage, recipes, chefAvatar, chefFullname, **kwargs):
        super(FoodSearch, self).__init__(**kwargs)
        self.foodId = foodId
        self.foodName = foodName
        self.foodImage = foodImage
        self.recipes = ', '.join(recipes)[:50]
        self.chefAvatar = chefAvatar
        self.chefFullname = chefFullname