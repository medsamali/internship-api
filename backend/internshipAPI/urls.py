"""
URL configuration for internshipAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from django.urls import path, include
from app.views import SectorViewSets
from app.views import SkillViewSets
from app.views import JobViewSets
from app.views import CompanyViewSets
from app.views import LocationViewSets
from app.views import UserViewSet
from app.views import GroupViewSet
from app.views import ProfileViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="ESTIAM API",
        default_version="v1"
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register(r'sectors', SectorViewSets)
router.register(r'skills', SkillViewSets)
router.register(r'jobs', JobViewSets)
router.register(r'companies', CompanyViewSets)
router.register(r'locations', LocationViewSets)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'profiles', ProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
