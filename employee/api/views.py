from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Employes
from api.serializer import EmployeSerializer

#localhost:8000/cakes/ 


class EmployesView(APIView):
    def get(self,request,*args,**kw):
        qs=Employes.objects.all()
        serializer=EmployeSerializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kw):
        serializer=EmployeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors) 

class EmployeDetailsView(APIView):
    def get(self,request,*args,**kw):
        id=kw.get("id")
        qs=Employes.objects.get(id=id)
        serializer=EmployeDetailsView(qs,many=False)
        return Response(data=serializer.data)

    def put(self,request,*args,**kw):
        id=kw.get("id")
        obj=Employes.objects.get(id=id)
        serializer=EmployeSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)    

    def delete(self,request,*args,**kw):
        id=kw.get("id")
        obj=Employes.objects.get(id=id)
        obj.delete()

        return Response(data="cake delete")
               
           

