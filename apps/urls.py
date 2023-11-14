from django.urls import path, include
from .views import redirectRoot, ApiRoot

urlpatterns = [
    path('', redirectRoot, name="redirect-root"),
    path('api', ApiRoot.as_view(), name='api-root'),
    path('api/auth/', include("apps.auth.users.urls"))
]
