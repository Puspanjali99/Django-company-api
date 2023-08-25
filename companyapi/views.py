from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("home page requested")
    friends=[
        'Sita',
        'Gita',
        'Rita',
        'Somy'
    ]
    return  JsonResponse(friends,safe=False)