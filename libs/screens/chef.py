import requests
from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ObjectProperty

from libs.components.smallFoodCard import SmallFoodCard


class Chef(MDScreen):
    chefId = 1
    fullname = StringProperty("")
    avatar = ObjectProperty(None)
    pycookID = StringProperty("")
    followedByTotal = StringProperty("")
    followersTotal = StringProperty("")

    def on_enter(self):
        chef_info = None
        try:
            api_url = "http://localhost:5000/api/user/getById"
            response = requests.get(api_url, params={"userId": self.chefId})
            if response.status_code == 200:
                chef_info = response.json()
        except Exception as e:
            print(e)

        if chef_info:
            self.fullname = chef_info.get("fullname", "")
            self.avatar = chef_info.get("avatar")
            print("avatar: ", self.avatar)
            self.pycookID = chef_info.get("pycookID", "")
            self.followedByTotal = str(chef_info.get("followedByTotal", "0"))
            self.followersTotal = str(chef_info.get("followersTotal", "0"))
            # My food
            my_food = self.ids.my_food
            my_food_total = self.ids.my_food_total

            my_food_total.text = (
                "Món ăn của "
                + chef_info["fullname"]
                + " ("
                + str(len(chef_info["foods"]))
                + ")"
            )
            my_food.clear_widgets()
            for food in chef_info.get("foods"):
                small_food_card = SmallFoodCard(
                    foodId=food["foodId"],
                    foodName=food["foodName"],
                    foodImage=food["foodImage"],
                    deliciousTotal=food["deliciousTotal"],
                    heartTotal=food["heartTotal"],
                    likeTotal=food["likeTotal"],
                )
                my_food.add_widget(small_food_card)

        # Follow chef
        follow_button = self.ids.follow_button
        userId = App.get_running_app().user['userId']
        if(userId == self.chefId):
            self.remove_widget(follow_button)
        try:
            api_url = "http://localhost:5000/api/follower/hasFollow"
            response = requests.get(
                api_url,
                params={
                    "followedId": self.chefId,
                    "followerId": App.get_running_app().user['userId'],
                },
            )

            if response.status_code == 200:
                follow_button.text = "Bạn bếp"
            else:
                follow_button.text = "Kết bạn bếp"
        except Exception as e:
            print(e)

    def on_follow_chef(self):
        follow_button = self.ids.follow_button
        try:
            api_url = "http://localhost:5000/api/follower/create"
            response = requests.get(
                api_url,
                params={
                    "followedId": self.chefId,
                    "followerId": App.get_running_app().user['userId'],
                },
            )
            
            if response.status_code == 201:
                follow_button.text = "Bạn bếp"
            else:
                follow_button.text = "Kết bạn bếp"
        except Exception as e:
            print(e)
