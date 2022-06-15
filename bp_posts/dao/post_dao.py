import json
from json import JSONDecodeError

from bp_posts.dao.post import Post
from exceptions.exceptions import DataSourceBrokenException


class PostDAO:

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """
        Загружает данные из JSON файла
        """
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceBrokenException("Файл с данными поврежден")
        return data

    def _load_posts(self):
        """
        Возвращает список экземпляров Post
        """
        posts_data = self._load_data()
        list_of_posts = [Post(**post_data) for post_data in posts_data]

        return list_of_posts

    def get_posts_all(self):
        """
        Возвращает все посты
        """
        posts = self._load_posts()
        return posts

    def get_posts_by_user(self, user_name):
        """
        Возвращает посты определённого пользователя
        """

        if type(user_name) != str:
            raise TypeError("Имя должно быть str")

        posts_found = []
        posts = self._load_posts()

        try:
            for post in posts:
                if post.poster_name.lower() == user_name.lower():
                    posts_found.append(post)
        except ValueError:
            print("Такого пользователя нет")
        return posts_found

    def search_for_posts(self, query):
        """
        Возвращает список постов по ключевому слову
        """

        if type(query) != str:
            raise TypeError("query должно быть str")

        posts = self._load_posts()
        posts_found = []

        for post in posts:
            if query.lower() in post.content.lower():
                posts_found.append(post)

        return posts_found

    def get_post_by_pk(self, pk):
        """
        Возвращает пост по pk
        """
        if type(pk) != int:
            raise TypeError("pk должно быть int")

        posts = self._load_posts()
        for post in posts:
            if post.pk == pk:
                return post

