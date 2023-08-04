from django.urls import path

from measurement.views import CreateSensorAPIView, ListCreateAPIView, RetrieveUpdateAPIView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/<int:pk>/', ListCreateAPIView.as_view()),
    path('sensors/', CreateSensorAPIView.as_view()),
    path('measurements/', RetrieveUpdateAPIView.as_view()),

]
