from omdb import OMDBClient


OMDB_API_KEY = "6b01423e"

client = OMDBClient(apikey=OMDB_API_KEY)


class Movie(object):
    def __init__(
        self,
        title: str = "",
        year: str = "",
        imdb_id: str = "",
        type: str = "",
        poster: str = "",
    ):
        self.title = title
        self.year = year
        self.imdb_id = imdb_id
        self.type = type
        self.poster = poster

    def from_dict(self, movie: dict):
        self.title = movie["title"]
        self.year = movie["year"]
        self.imdb_id = movie["imdb_id"]
        self.type = movie["type"]
        self.poster = movie["poster"]
        return self


def search_movie_by_title(title: str) -> list[Movie]:
    results = client.search(title, media_type="movie")
    movies = [Movie().from_dict(movie) for movie in results]
    
    return movies
