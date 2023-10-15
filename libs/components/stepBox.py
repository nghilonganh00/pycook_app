from kivymd.uix.boxlayout import MDBoxLayout

from kivy.properties import StringProperty, ObjectProperty
class StepBox(MDBoxLayout):
    ingredientName = StringProperty("")
    ingredientImage = ObjectProperty(None)
    def __init__(self, ingredientName, ingredientImage, **kwargs):
        super(StepBox, self).__init__(**kwargs)
        self.ingredientName = ingredientName
        self.ingredientImage =  ingredientImage