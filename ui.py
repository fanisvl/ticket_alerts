import requests
from pick import pick

url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhYjc1NTc1NThkYzk4ZWQ0YzcxYmFkNGYzMTFiN2ZlMyIsInN1YiI6IjY0ZWRmYjVkYzYxM2NlMDBhYzQzMzllYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.6vxxa1o8uge85qcUqMpTwsONg0_A_28s0PXR0xfL1mo"
}

response = requests.get(url, headers=headers)

data = response.json()

movies = data["results"]

titles = []

for movie in movies:
    titles.append(movie["original_title"])

selected = pick(titles)
