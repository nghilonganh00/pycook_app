from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, ObjectProperty
class MakingInput(MDBoxLayout):
    makingId = StringProperty('')
    ingredientNameId = StringProperty('')
    def __init__(self, makingId, **kwargs):
        super(MakingInput, self).__init__(**kwargs)
        self.makingId = str(makingId)
        self.makingNameId = f'making_input_{makingId}'
