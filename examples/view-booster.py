import os
import time
import webbrowser

url = 'https://go.twitch.tv/blizzakot'
refresh = '10'
browser = 'chrome'
count = '10'


def start():
    for i in range(0, int(count)):
        openURL()
        print("Website viewed")


def openURL():
    os.system("TASKKILL /F /IM " + browser + ".exe")
    webbrowser.open(url)
    time.sleep(int(refresh))


start()
