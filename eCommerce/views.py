from django.shortcuts import render

def home_page(request):
    # print(request.session.get("first_name", "Unknown"))
    # request.session['first_name']
    context = {
        "title":"Home",
        "content":" Welcome to the homepage.",
    }
    return render(request, "home.html", context)