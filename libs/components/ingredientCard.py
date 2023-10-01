from kivymd.uix.card import MDCard

from kivy.properties import StringProperty, ObjectProperty
class IngredientCard(MDCard):
    ingredientName = StringProperty("")
    ingredientImage = ObjectProperty(None)
    def __init__(self, ingredientName, ingredientImage, **kwargs):
        super(IngredientCard, self).__init__(**kwargs)
        self.ingredientName = ingredientName
        self.ingredientImage =  f"data:image/png;base64,{ingredientImage}"