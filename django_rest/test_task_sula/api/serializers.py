from rest_framework import serializers
from .models import Status, Record


class RecordListSerializer(serializers.ModelSerializer):
    user_id = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Record
        fields = '__all__'

class StatusListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'
