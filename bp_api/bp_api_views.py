import logging

from flask import Blueprint, jsonify

from bp_posts.dao.comment_dao import CommentDAO
from bp_posts.dao.post_dao import PostDAO
from config import DATA_PATH, COMMENT_PATH

bp_api = Blueprint("bp_api", __name__)

post_dao = PostDAO(DATA_PATH)
comments_dao = CommentDAO(COMMENT_PATH)

api_logger = logging.getLogger("api_logger")


@bp_api.route("/api/posts/")
def api_all_posts():
    """
    Эндпоинт для всех постов
    """
    posts = post_dao.get_posts_all()
    posts_as_dict = [post.posts_dict() for post in posts]
    api_logger.debug("Запрошены все посты /api/posts")
    return jsonify(posts_as_dict), 200


@bp_api.route("/api/posts/<int:pk>/")
def api_single_posts(pk):
    """
    Эндпоинт для одного поста
    """
    post = post_dao.get_post_by_pk(pk)
    api_logger.debug(f"Запрошен пост /api/posts/{pk}")
    return jsonify(post.posts_dict()), 200



