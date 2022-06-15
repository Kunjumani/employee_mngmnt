from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


# Create your views here.
# fn based view and class based view

#  1. fn based view
# def index(request):
#     return HttpResponse("<h1> hello world </h1>")
# def login(request):
#     return render(request, "login.html")
#     # return HttpResponse("<h1> LOGIN </h1>")
# def registration(request):
#     return render(request, "reg.html")
#     # return HttpResponse("<h1> REGISTRATION </h1>")

# 2 class based view

class IndexView(View):
    def get(self,request):
        return render(request, "index.html")

class LoginView(View):
    def get(self,request):
        return render(request, "login.html")
    def post(self,request):
        print(request.POST.get("u_name"))
        print(request.POST.get("pw"))
        return render(request, "login.html")


class RegView(View):
    def get(self, request):
        return render(request, "reg.html")
    def post(self,request):
        print(request.POST.get("f"))
        print(request.POST.get("l"))
        print(request.POST.get("e"))
        print(request.POST.get("u"))
        print(request.POST.get("p"))
        return render(request, "reg.html")




























