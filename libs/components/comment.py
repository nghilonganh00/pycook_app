from utils.formatTimeDifference import format_time_difference


from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, ObjectProperty, NumericProperty

class Comment(MDBoxLayout):
    userAvatar = ObjectProperty(None)
    userFullname = StringProperty("")
    userPycookID = StringProperty("")
    commentContent = StringProperty("")
