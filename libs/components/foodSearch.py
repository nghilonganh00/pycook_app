from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.properties import StringProperty, ObjectProperty

class FoodSearch(MDBoxLayout):
    foodName = StringProperty("")
    foodImage = ObjectProperty(None)
    recipe = StringProperty('')
    chefAvatar = ObjectProperty(None)
    chefFullname = StringProperty("")
    