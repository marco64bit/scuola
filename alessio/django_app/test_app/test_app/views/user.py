from django.http import JsonResponse


def get_users(request):
    return JsonResponse(
        {
            "name": "marco",
            "age": 30
        })