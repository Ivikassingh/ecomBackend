from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import  APIView
from rest_framework.response import  Response
from rest_framework import status
from api.models import Category, LinkStats, LinkMapper, Product
from api.serializer import CategorySerializer, LinkMapperSerializer, ProductSerializer, LinkStatsSerializer

import random

class CategoryApiView(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer
    def get_queryset(self):
        queryset=self.queryset.filter()
        return queryset


class LinkMapperApiview(viewsets.ModelViewSet):
    queryset=LinkMapper.objects.all()
    serializer_class=LinkMapperSerializer
    def get_queryset(self):
        queryset=self.queryset.filter()
        return queryset
    def create(self, request, *args, **kwargs):
        data=self.request.data
        request.data._mutable = True
        link=data["original"]
        generated=random.randint(1,100000)
        generated="localhost:8000/"+data["source"]+"/"+str(generated)
        data["generated"]=generated
        request.data._mutable = False
        serializer=ProductSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    

class ProductApiview(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def get_queryset(self):
        queryset=self.queryset.filter()
        return queryset
    
    def create(self, request, *args, **kwargs):
        data=self.request.data
        request.data._mutable = True
        link=data["link"]
        generated=random.randint(1,100000)
        generated="localhost:8000/"+data["source"]+"/"+str(generated)
        obj=LinkMapper(original=link,source="Product",generated=generated)
        obj.save()
        linkObj=LinkMapper.objects.get(generated=obj)
        data["linkId"]=linkObj.id
        data["link"]=linkObj.generated
        request.data._mutable = False
        serializer=ProductSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class LinkStatsApiview(viewsets.ModelViewSet):
    queryset=LinkStats.objects.all()
    serializer_class=LinkStatsSerializer
    def get_queryset(self):
        queryset=self.queryset.filter()
        return queryset


def update_stats(id):
    stats_queryset=LinkStats.objects.all()
    stats_data=stats_queryset.filter(linkname=id).values()
    print(stats_data)
    if list(stats_data)==[]:
        queryset=LinkMapper.objects.all()
        data=queryset.filter(id=id)
        obj=LinkStats(linkname=data[0],visitCount=0)
        obj.save()
    else:
        stats_data=list(stats_data)
        stats_data=stats_data[0]

        visit_count=stats_data["visitCount"]
        id=stats_data["id"]
        stats_queryset.filter(id=id).update(visitCount=visit_count+1)



def find_link(id):
    queryset=LinkMapper.objects.all()
    data=queryset.filter(id=id).values()
    update_stats(id)
    return data[0]["original"]

def find_link_by_generated(link):
    queryset=LinkMapper.objects.all()
    data=queryset.filter(id=id).values()
    id=data[0]["id"]
    update_stats(id)
    return data[0]["original"]

def visitproduct(request):
    linkid=request.GET.get("linkid")
    original_path=find_link(linkid)
    html = '''<html><body><div style='margin:0 auto;text-align:center'>Redirecting.....<script> 
    window.location.replace("{link}")</script></body></html>'''
    html=html.format(link=original_path)
    return HttpResponse(html)


def social_links(request):
    link=request.GET.get("link")
    linkid=request.GET.get("linkid")
    original_path=find_link_by_generated(linkid)
    html = '''<html><body><div style='margin:0 auto;text-align:center'>Redirecting.....<script> 
    window.location.replace("{link}")</script></body></html>'''
    html=html.format(link=original_path)
    return HttpResponse(html)

