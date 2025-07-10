import requests

url = 'https://api.themoviedb.org/3/movie/550?api_key=fd3ff4878346c240dbe04fc1aea33b28&language=en-US'

try:
    response = requests.get(url, timeout=10, proxies={"http": None, "https": None})
    response.raise_for_status()
    print("Success!")
    print(response.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
