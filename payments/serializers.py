from .models import Gateway, Payment

from rest_framework import serializers

class GatewaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gateway
        fields = ('id','title','description','avatar','is_enable')

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('user', 'package', 'gateway', 'price', 'status', 'device_uuid', 'token', 'phone_number', 'consumed_code')