from rest_framework import serializers
from mainly.models import Objectt

class ObjSerializer(serializers.ModelSerializer):

    class Meta:
        model = Objectt
        fields = ('name',
                  )

