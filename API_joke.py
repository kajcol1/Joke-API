from pyfiglet import figlet_format 
import requests
import random
url = "https://icanhazdadjoke.com/search"


print(figlet_format("JokeJukeBox"))
print(figlet_format("by Kajcol", font = "bubble" ))



ask_joke = input("Let me tell you a joke! Give me a topic:")


response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": ask_joke}
)

data = response.json()
results = data["results"]

if data['total_jokes'] != 0:
	print(f"I've got {data['total_jokes']} about {ask_joke}. Here is one: ")
	print(f"{random.choice(results)['joke']}")
else: 
	print(f"Sorry, I don't have a joke about {ask_joke}.")


