from kivymd.uix.screen import MDScreen

from compontents.online_friend import OnlineAvatarImage


class HomePage(MDScreen):
    profile_pic=""

    def on_enter(self):
self.load_online_friends()

def load_online_friends(self):
    eith open("assets/")
    data=json.load(f)
    for friend in  data:
        self.ids.online_fiends.add_widget()
        avatar=

    {
        "friend_2":{}
        "avatar":
    }
     {
        "friend_3":{}
        "avatar":
    }
     {
        "friend_4":{}
        "avatar":
    }


def list_stories(self):
    with open("/assets")as f:
        data=json.load(f)
        for friend name in data:
            self.ids.stories.add_widget(StoryWidget)
            name=friend_name,
            image=data[friend_name]['image']
            avatar=data[friend_name]['avatar']
            post=data(friendname)
            }}
def list_posts(self):
    with open("asses/posts_data.json"
    data- json.load(f)
    self.ids.stories.add_whidget















