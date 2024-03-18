import requests as req


class RAPIDAPI:
    def __init__(self, url: str, host: str, key: str, title=None):
        self.title = title
        self.URL = url
        self.HEADERS = {
            "X-RapidAPI-Host": host,
            "X-RapidAPI-Key": key
        }
    
    def request(self, query: str) -> dict:
        response = req.get(self.URL, headers=self.HEADERS, params={"query":query})
        content: dict = response.json()

        if content['status']:
            return content['message'], content['data']
        return f"sorry, {queries} not found! :(", False

    def __str__(self):
        return f"title: {self.title}\nurl: {self.URL}"
    
