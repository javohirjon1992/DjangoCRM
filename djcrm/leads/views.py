from django.shortcuts import render



def home_page(request):
    context = {
        "name":"Jonata",
        "age": 23
    }
    return render(request, 'second.html', context)