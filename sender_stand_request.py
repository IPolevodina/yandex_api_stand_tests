import configuration
import requests
import data

def get_users_table():
    # Составление полного URL пути к данным таблицы пользователей
    # путем конкатенации базового URL сервиса и конечной точки таблицы пользователей
    # Возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


def post_products_kits(product_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=product_ids, headers=data.headers)

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


