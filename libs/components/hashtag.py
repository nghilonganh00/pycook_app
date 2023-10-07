from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase

from kivy.properties import StringProperty
class Hashtag(MDBoxLayout, MDTabsBase):
    hashtagName = StringProperty("")
    def __init__(self, hashtagName="All", **kwargs):
        super(Hashtag, self).__init__(**kwargs)
        self.hashtagName = hashtagName