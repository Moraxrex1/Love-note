import random
import time

love_messages = [
    "You're the peanut butter to my jelly. ❤️",
    "Life is better with you in it. 💫",
    "Every moment with you is my favorite. 🌟",
    "You're my sunshine on a cloudy day. ☀️",
    "I love you more than coffee... and that’s saying a lot! ☕️❤️",
    "You make my heart smile. 😊",
    "I’m so lucky to have you in my life. 🍀",
    "You + Me = Forever 💞"
]

def show_love():
    print("\n💌 Welcome to Your Personalized Love Generator 💌\n")
    name = input("What's your name, sweetheart? ")
    print(f"\nHi {name}, here's a message just for you:\n")

    time.sleep(1)
    message = random.choice(love_messages)
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("\n\n💖 Have a lovely day! 💖")

if __name__ == "__main__":
    show_love()
