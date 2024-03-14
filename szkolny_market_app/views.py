from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, '')


class StudentLoginView(View):
    def get(self, request):
        return render(request, '')


class ParentLoginView(View):
    def get(self, request):
        return render(request, '')


class WorkerLoginView(View):
    def get(self, request):
        return render(request, '')


class StudentMenuView(View):
    def get(self, request):
        return render(request, '')


class ParentMenuView(View):
    def get(self, request):
        return render(request, '')


class WorkerMenuView(View):
    def get(self, request):
        return render(request, '')


class ShopProductsView(View):
    def get(self, request):
        return render(request, '')
