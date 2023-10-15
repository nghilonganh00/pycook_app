
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, ObjectProperty, NumericProperty

class AvatarIcon(MDBoxLayout):
    avatar = ObjectProperty(None)
    def __init__(self, avatar, **kwargs):
        super(AvatarIcon, self).__init__(**kwargs)
        self.avatar = avatar