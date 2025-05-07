import random

jokes = [
    {"setup": "Why don't Indians ever play hide and seek?", "punchline": "Because good luck hiding when aunty already knows everything!"},
    {"setup": "What did the Indian dosa say to the pizza?", "punchline": "You're just a flatter version of me with identity issues."},
    {"setup": "Why did the chai get promoted?", "punchline": "Because it was always brewing new ideas!"},
    {"setup": "How does an Indian mom measure time?", "punchline": "I told you 5 minutes ago, 10 minutes back!"},
    {"setup": "Why don't Indian uncles ever get lost?", "punchline": "Because GPS is no match for their confidence and wrong turns!"},
    {"setup": "What's an Indian engineer's favorite workout?", "punchline": "Debugging under pressure!"},
    {"setup": "Why did the student bring laddoos to the exam hall?", "punchline": "Because the question said: 'Explain with sweets!'"},
]


def Random_jokes():
    joke = random.choice(jokes)
    print(f"{joke['setup']}\n{joke['punchline']}")

Random_jokes()

######  (others way code) extra code

# import requests

# def Random_Jokes():
#     url = "https://official-joke-api.appspot.com/random_joke"
#     response = requests.get(url)
#     if response.status_code == 200:
#         joke = response.json()
#         print(f"SETUP-->{joke['setup']}\n ANS-->{joke['punchline']}")
#     else:
#         print("Try again later!")

# Random_Jokes()
