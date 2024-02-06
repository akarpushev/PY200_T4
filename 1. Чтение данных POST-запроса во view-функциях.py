# В Django для работы с POST-запросами часто используются view-функции.
# Вот пример того, как можно обработать POST-запрос и прочитать отправленные данные:

from django.http import HttpResponse

def my_view(request):
    if request.method == 'POST':
        # Получаем данные из POST-запроса
        received_data = request.POST

        # Данные доступны как словарь
        some_value = received_data.get('some_key', 'default_value')

        return HttpResponse(f"Полученное значение: {some_value}")

# Аналогично, но с декоратором

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
def my_view(request):
    # Получаем данные из POST-запроса
    received_data = request.POST

    # Данные доступны как словарь
    some_value = received_data.get('some_key', 'default_value')

    return HttpResponse(f"Полученное значение: {some_value}")

# Здесь **require_http_methods** указывает, что функция должна принимать только POST-запросы.
#
# **request.POST** - это словарь, содержащий все данные, отправленные в POST-запросе.
# Метод **get** используется для извлечения конкретных значений, предоставляя возможность указать значение по умолчанию,
# если ключ отсутствует.



