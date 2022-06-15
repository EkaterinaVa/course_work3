import pytest

from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO


def check_fields(post):
    fields = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]

    for field in fields:
        assert hasattr(post, field), f"Нет поля {field}"


class TestPostDAO:

    @pytest.fixture
    def post_dao(self):
        post_dao_instance = PostDAO("./bp_posts/tests/data_mock.json")
        return post_dao_instance

    # Тестирование получения всех постов
    def test_get_all_types(self, post_dao):
        posts = post_dao.get_posts_all()
        assert type(posts) == list, "Некорректный тип данных"

        post = post_dao.get_posts_all()[0]
        assert type(post) == Post, "Некорректный тип данных для одного поста"

    def test_get_all_fields(self, post_dao):
        posts = post_dao.get_posts_all()
        post = post_dao.get_posts_all()[0]
        check_fields(post)

    def test_get_all_correct_id(self, post_dao):
        posts = post_dao.get_posts_all()

        correct_pk = {1, 2, 3}
        pk = set([post.pk for post in posts])
        assert pk == correct_pk, "Не совпадают полученные pk"

    # Тестирование получения одного поста по pk
    @pytest.mark.parametrize("pk", [1, 2, 3])
    def test_get_by_correct_pk(self, post_dao, pk):
        post = post_dao.get_post_by_pk(pk)
        assert post.pk == pk, "Некорректный pk"

    # Тестирование получения постов по ключевому слову

    def test_search_for_posts_types(self, post_dao):
        posts = post_dao.search_for_posts("ага")
        assert type(posts) == list, "Некорректный тип данных"
        post = post_dao.get_posts_all()[0]
        assert type(post) == Post, "Некорректный тип данных для одного поста"

    def test_search_for_posts_fields(self, post_dao):
        posts = post_dao.search_for_posts("ага")
        post = post_dao.get_posts_all()[0]
        check_fields(post)

    def test_posts_not_found(self, post_dao):
        posts = post_dao.search_for_posts("0000000")
        assert posts == [], "Должен быть пустой список []"

    @pytest.mark.parametrize("query, expected_pks", [
        ("еда", {1}),
        ("днем", {2}),
        ("машин", {3}),
    ])
    def test_search_for_posts_results(self, post_dao, query, expected_pks):
        posts = post_dao.search_for_posts(query)
        pks = set([post.pk for post in posts])
        assert pks == expected_pks, f"Некорректный результат поиска {query}"

    # Тестирование получения постов по имени пользователя

    @pytest.mark.parametrize("poster_name, expected_pk", [
        ("leo", {1}),
        ("johnny", {2}),
        ("hank", {3}),
    ])
    def test_search_for_posts_results(self, post_dao, poster_name, expected_pk):
        posts = post_dao.get_posts_by_user(poster_name)
        pks = set([post.pk for post in posts])
        assert pks == expected_pk, f"Некорректный результат поиска по имени {poster_name}"


