import pytest

from bp_posts.dao.comment_dao import CommentDAO


class TestCommentDAO:

    @pytest.fixture
    def comment_dao(self):
        comment_dao_instance = CommentDAO("./bp_posts/tests/comments_mock.json")
        return comment_dao_instance

    # Тестирование получения всех комментариев

    def test_get_all_comments(self, comment_dao):
        comments = comment_dao.get_comments_all()
        assert len(comments) == 5, "Получено неверное количество комментариев"

    # Тестирование получения комментариев по id

    @pytest.mark.parametrize("post_id, expected_len", [
        (1, 4),
        (2, 1),
    ])
    def test_get_comments_by_post_id(self, comment_dao, post_id, expected_len):
        comments = comment_dao.get_comments_by_post_id(post_id)
        assert len(comments) == expected_len, "Получено неверное количество комментариев по id"

