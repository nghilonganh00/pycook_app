from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, ObjectProperty
class IngredientInput(MDBoxLayout):
    ingredientId = StringProperty('')
    ingredientNameId = StringProperty('')
    def __init__(self, ingredientId, **kwargs):
        super(IngredientInput, self).__init__(**kwargs)
        self.ingredientId = str(ingredientId)
        self.ingredientNameId = f'ingredient_input_{ingredientId}'

    def getValueInput(self):
        return self.ids.ingredient_input.text