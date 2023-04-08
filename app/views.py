from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework import  status
from .serializers import CartItemSerializer
from .models import CartItem


# Create your views here.
class CartItemViews(APIView):
    def post(self,request):
        serializers=CartItemSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"status":"sucess","data":serializers.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializers.data},status=status.HTTP_400_BAD_REQUEST)



