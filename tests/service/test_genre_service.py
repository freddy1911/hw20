import pytest

from service.genre import GenreService


class TestGenreService:
	@pytest.fixture(autouse=True)
	def genre_service(self, genre_dao):
		self.genre_service = GenreService(dao=genre_dao)

	def test_get_one(self):
		genre = self.genre_service.get_one(1)

		assert genre is not None
		assert genre.id is not None

	def test_get_all(self):
		genres = self.genre_service.get_all()

		assert len(genres) > 1

	def test_create(self):
		data = {
			"name": "Test"
		}
		genre = self.genre_service.create(data)
		assert genre.id is not None

	def test_update(self):
		data = {
			"name": "TestTest"
		}
		self.genre_service.update(data)

	def test_delete(self):
		self.genre_service.delete(1)