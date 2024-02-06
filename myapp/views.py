from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def my_view(request):
    if request.method == 'POST':
        # Получаем данные из POST-запроса
        received_data = request.POST

        # Данные доступны как словарь
        some_value = received_data.get('key', 'Ключ не найден')

        #return HttpResponse(f"Полученное значение: {some_value}"
        return JsonResponse(request.POST)
    return HttpResponse(f"Был GET запрос")
