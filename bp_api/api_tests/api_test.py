import pytest
import main


class TestApi:

    correct_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    @pytest.fixture
    def app_instance(self):
        app = main.app
        test_client = app.test_client()
        return test_client

    # Тестируем эндпоинт api/posts

    def test_api_all_posts_has_correct_status(self, app_instance):
        response = app_instance.get("/api/posts", follow_redirects=True)
        assert response.status_code == 200

    def test_api_all_posts_has_correct_type(self, app_instance):
        response = app_instance.get("/api/posts", follow_redirects=True)
        assert type(response.json) == list

    def test_api_all_posts_has_correct_keys(self, app_instance):
        response = app_instance.get("/api/posts", follow_redirects=True)
        posts = response.get_json()

        for post in posts:
            assert post.keys() == self.correct_keys, "Неверные ключи"

    # Тестируем эндпоинт api/posts/<pk>

    def test_api_single_posts_has_correct_status(self, app_instance):
        response = app_instance.get("/api/posts/1", follow_redirects=True)
        assert response.status_code == 200

    def test_api_single_posts_has_correct_type(self, app_instance):
        response = app_instance.get("/api/posts/1", follow_redirects=True)
        assert type(response.json) == dict

    def test_api_single_posts_has_correct_keys(self, app_instance):
        response = app_instance.get("/api/posts/3", follow_redirects=True)
        post = response.get_json()
        post_keys = set(post.keys())
        assert post_keys == self.correct_keys

