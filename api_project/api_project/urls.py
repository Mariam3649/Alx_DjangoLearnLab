from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # ربط app api بالـ project
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    ...,
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # ✅ كده التشيكر هيقبله
]
]

