from django.shortcuts import render
from .serializer import *
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class ProductView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        #custom Query lookup
        category =self.request.query_params.get('category')
        if category:
            #checking category_name from product which has a category foreign key related to model category 
            queryset = Product.objects.filter(category__category_name__iexact=category)
        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({'count': len(serializer.data) , 'data': serializer.data})