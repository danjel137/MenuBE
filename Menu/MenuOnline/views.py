# Create your views here.
from rest_framework import status

from .models import Menu, Customer
from .serializers import MenuSerializer, CustomerSerializer, BillSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['POST'])
def addMenuItemList(request):
    serializerNewData = MenuSerializer(data=request.data)
    if serializerNewData.is_valid():
        added_Item_menu = serializerNewData.save()
        return Response(data={"message": f"Object with id={added_Item_menu.id} added"}, status=status.HTTP_201_CREATED)
    else:
        return Response(data={"message": f"Object did not found"})

@api_view(['GET'])
def getMenuList(request):
    menu = Menu.objects.all()
    serializer = MenuSerializer(menu, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCustomerList(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addCustomer(request):
    serializerNewData = CustomerSerializer(data=request.data)
    if serializerNewData.is_valid():
        added_customer = serializerNewData.save()
        return Response(data={"message": f"Object with id={added_customer.id} added"}, status=status.HTTP_201_CREATED)
    else:
        return Response(data={"message": f"Object did not found"})


@api_view(['POST'])
def addBill(request):
    serializerNewData = BillSerializer(data=request.data)
    if serializerNewData.is_valid():
        added_bill = serializerNewData.save()
        return Response(data={"message": f"Object with id={added_bill.id} added"}, status=status.HTTP_201_CREATED)
    else:
        return Response(data={"message": f"Object did not found"})
