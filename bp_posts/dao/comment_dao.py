import json
from bp_posts.dao.comment import Comment


class CommentDAO:

    def __init__(self, comment_path):
        self.comment_path = comment_path

    def get_comments_all(self):
        """
        Возвращает все комментарии
        """
        with open(self.comment_path, "r", encoding="utf-8") as file:
            comments_data = json.load(file)
            comments = []

            for comment in comments_data:
                comments.append(Comment(
                    comment["post_id"],
                    comment["commenter_name"],
                    comment["comment"],
                    comment["pk"],
                ))
        return comments

    def get_comments_by_post_id(self, post_id):
        """
        Возвращает комментарии определённого поста
        """
        comments_found = []
        comments = self.get_comments_all()

        try:
            for comment in comments:
                if comment.post_id == post_id:
                    comments_found.append(comment)

        except ValueError:
            print("Такого поста нет")

        return comments_found


