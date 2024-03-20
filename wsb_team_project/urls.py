"""
URL configuration for wsb_team_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from szkolny_market_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    path('student_menu/', StudentMenuView.as_view(), name='student_menu'),
    path('parent_menu/', ParentMenuView.as_view(), name='parent_menu'),
    path('worker_menu/', WorkerMenuView.as_view(), name='worker_menu'),

    path('student_menu/shop_products', ShopProductsView.as_view(), name='shop_products'),
    path('student_menu/history', ShopProductsView.as_view(), name='shop_products'),
    path('parent_menu/', ParentMenuView.as_view(), name='parent_menu'),
    path('worker_menu/', WorkerMenuView.as_view(), name='worker_menu'),

    path('shop_products/', ShopProductsView.as_view(), name='worker_menu'),


]
