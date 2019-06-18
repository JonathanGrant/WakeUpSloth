import requests
import random
import fbchat
import os

msg = []

# Introduction
nicknames = [
    "beautiful", "my love", "bob", "best girlfriend in the world",
    "dorkasourus bex", "bukuh", "UNKA"
]

intro = "Good morning {}. I love you!".format(random.choice(nicknames))
msg.append(intro)

# Weather section
weather_url = "https://api.darksky.net/forecast/{}/40.682750,-73.978190".format(os.environ["WEATHER_APIKEY"])
weather_data = requests.get(weather_url).json()
weather_msg = "The weather is between {} and {}. {}".format(
    weather_data["daily"]["data"][0]["temperatureHigh"], weather_data["daily"]["data"][0]["temperatureLow"],
    weather_data["hourly"]["summary"].encode('utf-8'))
msg.append(weather_msg)

# Image section
images = []
# Dog section
dog_url = "https://dog.ceo/api/breeds/image/random"
dog_img = requests.get(dog_url).json()["message"]
images.append((dog_img, "Here is your dog of the day :)"))

# Shiba section
shiba_url = "http://shibe.online/api/shibes?count=1"
shiba_img = requests.get(shiba_url).json()[0]
images.append((shiba_img, "Here is your shiba of the day =]"))

# Choose image
img_link, img_text = random.choice(images)

# Send message
from fbchat.models import *
client = fbchat.Client(os.environ["fbemail"], os.environ["fbpwd"])
client.send(Message(text='\n'.join(msg)), thread_id=os.environ["fbgfid"], thread_type=ThreadType.USER)
client.sendRemoteImage(img_link, message=Message(text=img_text), thread_id=os.environ["fbgfid"], thread_type=ThreadType.USER)

