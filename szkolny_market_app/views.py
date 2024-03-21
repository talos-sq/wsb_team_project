from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)
            login(request, user)

            user = get_user_model().objects.get(username=username)
            if user.has_perm("szkolny_market_app.student"):
                return HttpResponseRedirect('student_menu/')
            elif user.has_perm("szkolny_market_app.parent"):
                return HttpResponseRedirect('parent_menu/')
            elif user.has_perm("szkolny_market_app.worker"):
                return HttpResponseRedirect('worker_menu/')
            else:
                return render(request, "index.html")
        return render(request, "index.html")


class StudentMenuView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "szkolny_market_app.student"

    def get(self, request):
        return render(request, 'student.html')


class ParentMenuView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "szkolny_market_app.parent"

    def get(self, request):
        return render(request, 'parent.html')


class WorkerMenuView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "szkolny_market_app.worker"

    def get(self, request):
        return render(request, 'worker.html')


class ShopProductsView(View):
    def get(self, request):
        return render(request, '')
