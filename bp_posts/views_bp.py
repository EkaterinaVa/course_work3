from flask import Blueprint, render_template, request, current_app
from werkzeug.exceptions import abort

from bp_posts.dao.comment_dao import CommentDAO
from bp_posts.dao.post_dao import PostDAO

from config import DATA_PATH, COMMENT_PATH

# Создаем блупринт, выбираем для него имя
blueprint_posts = Blueprint('blueprint_posts', __name__, template_folder="templates")

# Создаем объекты доступа к данным
post_dao = PostDAO(DATA_PATH)
comments_dao = CommentDAO(COMMENT_PATH)


@blueprint_posts.route("/")
def main_page():
    """ Вьюшка для главной страницы"""
    all_posts = post_dao.get_posts_all()
    return render_template("index.html", posts=all_posts)


@blueprint_posts.route("/posts/<int:pk>/")
def single_post(pk):
    """ Вьюшка для одного поста"""
    post = post_dao.get_post_by_pk(pk)
    comments = comments_dao.get_comments_by_post_id(pk)

    if post is None:
        abort(404)

    return render_template("post.html", post=post, comments=comments)


@blueprint_posts.route("/search/")
def posts_search():
    """ Возвращает результаты поиска"""
    query = request.args.get("s", "")

    if query == "":
        posts = []
    else:
        posts = post_dao.search_for_posts(query)

    return render_template("search.html",
                           posts=posts,
                           query=query,
                           posts_len=len(posts)
                           )


@blueprint_posts.route("/users/<user_name>/")
def user_post(user_name):
    """ Вьюшка для постов определённого пользователя"""
    posts = post_dao.get_posts_by_user(user_name)

    return render_template("user-feed.html",
                           posts=posts,
                           user_name=user_name)



