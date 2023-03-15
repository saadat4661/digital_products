import random
import uuid

from django.core.cache import cache

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Device

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        is_staff = request.data.get('is_staff')
        is_active = request.data.get('is_active')

        if not phone_number:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try: 
            user = User.objects.get(
                phone_number=phone_number,
            )
            return Response({'detail': 'Phone number already registered'}, status=status.HTTP_400_BAD_REQUEST)
        
        except User.DoesNotExist:
            user = User.objects.create_user(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
                phone_number=phone_number,
                password=password,
                # is_staff = is_staff, 
                # is_active = is_active,
                )
        
        device_uuid = request.data.get('device_uuid')
        notify_token = request.data.get('notify_token')
        device_type = request.data.get('device_type')
        device_os = request.data.get('device_os')
        device_model = request.data.get('device_model')
        app_version = request.data.get('app_version')

        # device = Device.objects.create(
        #     user = user,
        #     device_uuid = device_uuid,
        #     notify_token = notify_token,
        #     device_type = device_type,
        #     device_os = device_os,
        #     device_model = device_model,
        #     app_version = app_version,
        # )

        code = random.randint(10000,99999)

        cache.set(str(phone_number), code, 2 * 60) # code will be held in cache for 2 minutes

        """ 

        send "code" to the user (SMS or email)

        """

        return Response({'code':code})
    
class GetTokenView(APIView):
    
    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')
        cached_code = cache.get(str(phone_number))

        if code != cached_code:
            return Response(status=status.HTTP_403_FORBIDDEN)
            
        token = str(uuid.uuid4()) # use JWT instead of uuid

        return Response({'token': token})
    