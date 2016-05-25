# TODO: Need comments
# Need to organize code better beyond trial stages
# Need to allow user to enter movie name



import math
import data
import requests

movie_title = "Sesame Street"
response = requests.get("http://www.omdbapi.com/?t=" + movie_title + "&y=&plot=short+r=json")
movie_genres = response.json()["Genre"].split(", ")

wine_vector = [0] * len(data.genres)
for genre in movie_genres:
    wine_vector[data.genres.index(genre)] = 1

def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

top_wine = ["", 0]
for entry in data.wine_dict.items():
    print(entry[0])
    print(cosine_similarity(entry[1], wine_vector))
    if cosine_similarity(entry[1], wine_vector) > top_wine[1]:
        top_wine[0] = entry[0]
        top_wine[1] = cosine_similarity(entry[1], wine_vector)

print(top_wine)
