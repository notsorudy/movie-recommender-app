import requests

url = "https://api.themoviedb.org/3/movie/550?api_key=fd3ff4878346c240dbe04fc1aea33b28&language=en-US"

session = requests.Session()
adapter = requests.adapters.HTTPAdapter()
session.mount("https://", adapter)

try:
    response = session.get(
        url,
        timeout=10,
        headers={"User-Agent": "Mozilla/5.0"},
        proxies={"http": None, "https": None},
    )
    response.raise_for_status()
    print("Success!")
    print(response.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
