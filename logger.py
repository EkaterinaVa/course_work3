import logging
from config import LOGGER_API_PATH


def config_logger():
    # Создаем логгер
    api_logger = logging.getLogger("api_logger")
    api_logger.setLevel("DEBUG")

    # Настраиваем обработчики
    api_logger_handler = logging.FileHandler(filename=LOGGER_API_PATH)
    api_logger_handler.setLevel("DEBUG")
    api_logger.addHandler(api_logger_handler)

    # Добавляем форматтеры
    api_logger_format = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    api_logger_handler.setFormatter(api_logger_format)

