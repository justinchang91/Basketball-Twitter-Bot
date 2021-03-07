import requests
from noob import poo
print("TEST 1: Response1, the google API")
response = requests.get("https://google.com/")  # requests.get(url, params={key: value}, args)

if response:  # true if response was between 200 and 400
    print("The request was successful")
else:
    print("The request was unsuccessful")

# '''
words = 30
paragraphs = 1
formats = 'json'

print("\nTEST 2: Response2, the dino ipsum API")
response2 = requests.get(
    f"https://alexnormand-dino-ipsum.p.rapidapi.com/?format={formats}&words={words}&paragraphs={paragraphs}",
    headers={
        "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
        "X-RapidAPI-Key": poo
    }
    )

# '''

'''
params = {"words": 30, "paragraphs": 1, "formats": "json"}

response2 = requests.get(f"https://alexnormand-dino-ipsum.p.rapidapi.com/",
                         params=params,
                         headers={
                             "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
                             "X-RapidAPI-Key": poo
                         }
                         )
'''


# You need the f"......{}" for formatting string literals. Basically allows you to put the variables into the string
# instead of doing something like print("Hello " var1 + " my name is " + var2)

print(type(response2))
print(response2.status_code)
derp = response2.json()
print(derp)

print("\nTEST 3: Response 3, the reddit API")
response3 = requests.get("https://www.reddit.com/r/all/.json", headers={'User-agent': 'your bot 0.1'})
container = response3.json()
print(container)
print(type(container))
print(container["data"]["children"][0])  # OH so basically each post is a dictionary in the list, children
print()

for post in container["data"]["children"]:
    post_data = post["data"]
    subreddit = post_data["subreddit"]
    title = post_data["title"]
    score = post_data["score"]
    print(f"Title: {title} \nSubreddit: {subreddit} \nScore: {score}\n")
