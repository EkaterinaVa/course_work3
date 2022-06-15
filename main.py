from flask import Flask

from bp_api.bp_api_views import bp_api
from bp_posts.views_bp import blueprint_posts
from exceptions.exceptions import DataSourceBrokenException

import logger


app = Flask(__name__)

# Регистрируем блупринты
app.register_blueprint(blueprint_posts)
app.register_blueprint(bp_api)

# Добавляем логгер
logger.config_logger()


# Добавляем обработчики ошибок
@app.errorhandler(404)
def page_not_found(error):
    return "Страница не найдена", 404


@app.errorhandler(500)
def server_error_500(error):
    return f"Ошибка на сервере - {error}", 500


@app.errorhandler(DataSourceBrokenException)
def data_source_error(error):
    return f"Ошибка, проблема с данными - {error} ", 500


if __name__ == "__main__":
    app.run(debug=True)
