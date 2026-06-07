from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Coupon
from .serializers import CouponSerializer
from .services import apply_coupon

@api_view(['POST'])
def create_coupon(request):
    serializer = CouponSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Coupon created successfully",
            "coupon": serializer.data
        })
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def list_coupons(request):
    coupons = Coupon.objects.all()
    serializer = CouponSerializer(coupons, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def apply_coupon_view(request):
    code = request.data.get("code")
    cart_value = request.data.get("cartValue")
    result = apply_coupon(code, cart_value)
    return Response(result)


@api_view(['PATCH'])
def disable_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
    except Coupon.DoesNotExist:
        return Response({"message": "Coupon not found"}, status=404)

    coupon.isActive = False
    coupon.save()

    return Response({"message": "Coupon disabled successfully"}, status=200)