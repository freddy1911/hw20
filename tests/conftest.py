from unittest.mock import MagicMock
import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    director1 = Director(id=1, name='Иван')
    director2 = Director(id=2, name='Петр')
    director3 = Director(id=3, name='Тест')

    director_dao.get_one = MagicMock(return_value=director1)
    director_dao.get_all = MagicMock(return_value=[director1, director2, director3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(None)

    genre1 = Genre(id=1, name='Комедия')
    genre2 = Genre(id=2, name='Ужасытестирования')
    genre3 = Genre(id=3, name='Тест')

    genre_dao.get_one = MagicMock(return_value=genre1)
    genre_dao.get_all = MagicMock(return_value=[genre1, genre2, genre3])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(None)

    movie1 = Movie(id=1, title="Оч странные дела", description="Сериал такой, интересный",
                   trailer="www.kinopoisk.org/343464564", year=2017,
                   rating="R")
    movie2 = Movie(id=2, title="Бэтмэн", description="Фильм про мышь",
                   trailer="www.kinopoisk.org/34323233564", year=2011,
                   rating="R")
    movie3 = Movie(id=3, title="Бэтмэн 2", description="Фильм про мышь опять",
                   trailer="www.kinopoisk.org/343232335642", year=2012,
                   rating="R")
    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao
