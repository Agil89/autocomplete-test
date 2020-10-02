from rest_framework.views import APIView
from mainly.models import Objectt
from mainly.api.serializers import ObjSerializer
from rest_framework.response import Response

class MainSearchAPIView(APIView):
    
     def get(self,request):
        input_value = self.request.GET.get('inputValue')
        obj_query = Objectt.objects.filter(name__startswith=input_value)[:5]
        # будет предложен : вариантов но можно увеличить количество

        object_serializer = ObjSerializer(obj_query, many=True,context={'request':request})

        data = {
            "data_obj":object_serializer.data,
        }
        print(data)
        return Response(data)