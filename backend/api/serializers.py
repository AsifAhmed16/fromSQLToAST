from rest_framework import serializers

from .models import SQLToAST


class SQLToASTSerializer(serializers.ModelSerializer):
    class Meta:
        model = SQLToAST
        fields = '__all__'
