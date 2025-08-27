from django.http import request
from django.shortcuts import render
from app.views import *
from .models import *


def index(request):

    return render(request, "index.html")

    # if request.GET.get("search"):
    #     queryset = queryset.filter(receipe_name__icontains=request.GET.get("search"))
    #     context = {"receipes": queryset}


# def delete_receipe(request, id):
#     queryset = Student.objects.get(id=id)
#     queryset.delete()
#     queryset.delete()


#     queryset = Student.object.all()
#     context = {"student":queryset}
#     return render(request,"index.html",context)

# def student():
#     if request.method == "POst":
#         FirstName = request.Post.get("student")
