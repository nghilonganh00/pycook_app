from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
class MakingBox(MDBoxLayout):
    makingOrder = StringProperty('')
    makingContent = StringProperty('')
    def __init__(self, makingOrder, makingContent, **kwargs):
        super(MakingBox, self).__init__(**kwargs)
        self.makingOrder = str(makingOrder)
        self.makingContent = makingContent