from unicodedata import category
from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CategorySerializer, LectureSerializer
from .models import Category, Lectures
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'CategoryList': '/ctlist/',
        'VideosList': '/leclist/',
        'CategoryDetails': '/ctdetails/<str:pk>/',
        'VideoDetails': '/lecdetails/<str:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def categorylist(request):
    cats = Category.objects.all()
    serializer = CategorySerializer(cats, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def categoryDetails(request, pk):
    cats = Category.objects.get(id=pk)
    nc = cats.title
    print(nc)
    serializer = CategorySerializer(cats, many=False)
    lecs = Lectures.objects.filter(category__title__exact=nc)
    ls = []

    for i in lecs:
        lecd = {}
        lecd["id"] = i.id
        lecd["title"] = i.title
        lecd["date_created"] = i.date_created
        lecd["link"] = i.link
        lecd["duration"] = i.duration
        ls.append(lecd)

    ctdetails = {
        "id": cats.id,
        "title": cats.title,
        "short_description": cats.short_description,
        "date_created": cats.date_created,
        "lectures": ls
    }
    return Response(ctdetails)


@api_view(['GET'])
def lecturelist(request):
    cats = Lectures.objects.all()
    serializer = LectureSerializer(cats, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lectureDetails(request, pk):
    cats = Lectures.objects.get(id=pk)
    serializer = LectureSerializer(cats, many=False)
    return Response(serializer.data)
