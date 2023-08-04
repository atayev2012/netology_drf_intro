# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor
from measurement.serializers import SensorDetailSerializer, SensorSerializer


class ListCreateAPIView(APIView):
    #Получить детальную информацию о датчике методом GET по id
    def get(self, request, pk):
        sensor_object = Sensor.objects.get(id=pk)
        serializer = SensorDetailSerializer(sensor_object)
        return Response(serializer.data)

    #Обновить данные датчика по id
    def patch(self, request, pk):
        sensor_object = Sensor.objects.get(id=pk)
        data = request.data

        sensor_object.name = data.get("name", sensor_object.name)
        sensor_object.description = data.get("description", sensor_object.description)
        sensor_object.save()

        sensor_serializer = SensorSerializer(sensor_object)
        return Response(sensor_serializer.data)


class RetrieveUpdateAPIView(APIView):
    #Внести измерение нужному датчику
    def post(self, request):
        data = request.data
        sensor_id = data.pop('sensor')
        sensor_object = Sensor.objects.get(id=sensor_id)
        sensor_object.measurements.create(temperature=data['temperature'])
        sensor_object.save()
        serializer = SensorDetailSerializer(sensor_object)
        return Response(serializer.data)

class CreateSensorAPIView(APIView):
    #Получить весь список датчиков
    def get(self, request):
        data = Sensor.objects.all()
        serializer = SensorSerializer(data, many=True)
        return Response(serializer.data)

    #Добваить новый датчик
    def post(self, request):
        ser = SensorSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(request.data)
