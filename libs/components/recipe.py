from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, ObjectProperty
class Recipe(MDBoxLayout):
    ingredientName = StringProperty('')
    def __init__(self, ingredientName, **kwargs):
        super(Recipe, self).__init__(**kwargs)
        self.ingredientName = ingredientName