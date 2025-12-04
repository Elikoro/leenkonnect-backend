from rest_framework import serializers
from .models import Client, ClientContact, ClientAddress


class ClientContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContact
        fields = "__all__"
        read_only_fields = ["client"]


class ClientAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAddress
        fields = "__all__"
        read_only_fields = ["client"]


class ClientSerializer(serializers.ModelSerializer):
    contacts = ClientContactSerializer(many=True, read_only=True)
    addresses = ClientAddressSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ["organization"]
