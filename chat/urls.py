from django.urls import path,include
from chat import views
from rest_framework.routers import DefaultRouter
from chat.views import(
    RegisterUserAPIView,
)

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'message',views.MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/',RegisterUserAPIView.as_view()),
]
