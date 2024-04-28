import sys

from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, TemplateView

from szkolny_market_app.models import *


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


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect("/")


class StudentMenuView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "szkolny_market_app.student"

    def get(self, request):
        student = Student.objects.get(user=request.user.id)
        products = Product.objects.all()

        context = {"user": request.user, "student": student, "products": products}

        return render(request, 'student.html', context)


class ParentMenuView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "szkolny_market_app.parent"

    def get(self, request):
        context = {"user": request.user}

        return render(request, 'parent.html', context)


class ParentChildBalanceView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "szkolny_market_app.parent"

    def get(self, request):
        parent = Parent.objects.get(user=request.user)
        context = {"user": request.user, "child": parent.child}

        return render(request, 'parent_child_balance.html', context)


class ParentChildAddFundsView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "szkolny_market_app.parent"

    def get(self, request):
        context = {"user": request.user}

        return render(request, 'parent_child_add_funds.html', context)

    def post(self, request):
        amount = int(request.POST["amount"])

        if amount > 0:
            parent = Parent.objects.get(user=request.user)
            parent.child.balance += amount
            parent.child.save()
            context = {"user": request.user, "child": parent.child}

            return render(request, 'parent_child_balance.html', context)
        else:
            context = {"user": request.user}

            return render(request, 'parent_child_add_funds.html', context)


class ParentChildHistoryView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "szkolny_market_app.parent"

    def get(self, request):
        context = {"user": request.user}

        return render(request, 'parent_child_history.html', context)


class WorkerMenuView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "szkolny_market_app.worker"

    def get(self, request):
        return render(request, 'worker.html')


class WorkerMenuSellView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "szkolny_market_app.worker"

    def get(self, request):
        return render(request, 'worker_sell.html')

    def post(self, request):
        product_id = int(request.POST["product_id"])
        amount = int(request.POST["amount"])
        student_id = int(request.POST["student_id"])

        product = Product.objects.get(id=product_id)
        product_price = product.price

        student = Student.objects.get(id=student_id)
        student.balance -= product_price * amount
        student.save()

        product.quantity -= amount
        product.save()

        return render(request, 'worker_sell.html')


class WorkerMenuWarehouseView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "szkolny_market_app.worker"

    def get(self, request):
        food = Product.objects.filter(category=0)
        drinks = Product.objects.filter(category=1)
        snacks = Product.objects.filter(category=2)

        context = {"food": food, "drinks": drinks, "snacks": snacks}

        return render(request, 'worker_warehouse.html', context)
