from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . import forms
from .models import Login
import json
from django.views.generic import CreateView,UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.generics import CreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.response import Response
from .serializers import LoginSerializers, EmployeeSerializers, CompanySerializers


class ListLogin(ListAPIView):
    serializer_class = LoginSerializers
    model = serializer_class.Meta.model
    queryset = model.objects.order_by('name')


class TeamMembers(ListAPIView):
    serializer_class = EmployeeSerializers
    model = serializer_class.Meta.model

    def get_queryset(self):
        manager = self.request.query_params.get('manager', None)
        employee = self.request.query_params.get('employee', None)
        if manager is not None:
            manager_id = self.model.objects.only('id').filter(employee_name=manager)
            return self.model.objects.filter(employee_manager=manager_id)
        elif employee is not None:
            return self.model.objects.filter(employee_name=employee)
        else:
            return self.model.objects.all()


class Managers(ListAPIView):
    serializer_class_employee = EmployeeSerializers
    serializer_class_company = CompanySerializers
    model_emp = serializer_class_employee.Meta.model
    model_comp = serializer_class_company.Meta.model

    def get_queryset(self):
        company = self.request.query_params.get('company', None)
        if company is not None:
            company_id = self.model_comp.objects.only('id').filter(company_name=company)
            manager_ids = list(self.model_empl.objects.only('employee_manager').filter(employee_company=company_id).distinct())
            return self.model_emp.objects.only('employee_name').filter(id__in=manager_ids)


class Employees(ListAPIView):
    serializer_class_employee = EmployeeSerializers
    serializer_class_company = CompanySerializers
    model_emp = serializer_class_employee.Meta.model
    model_comp = serializer_class_company.Meta.model

    def get_queryset(self):
        company = self.request.query_params.get('company', None)
        if company is not None:
            company_id = self.model_comp.objects.only('id').filter(company_name=company)
            return self.model_emp.objects.only('employee_name').filter(employee_company=company_id)



# Create your views here.
class LoginCreate(CreateAPIView):

    def create(self, request, *args, **kwargs):

        login_name = request.data.get('name')
        login_email = request.data.get('email')
        if login_email in Login.objects.values_list('email',flat=True):
            f =Login.objects.values_list('email','name')
            print('-------------------------------',f)
            return Response ('Email already exist')
        login_pass = request.data.get('password')
        Login.objects.create(name=login_name, email=login_email, password=login_pass)
        return  Response('Record Created Successfuly')

class GetAllLogin(RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        if 'name' in request.query_params:
            logins = Login.objects.filter(name=request.query_params.get('name'))
        else:
            logins = Login.objects.all()

        logins_dict = {'logins':[{'name':login.name, 'email': login.email, 'password': login.password} for login in logins]}
        return Response(logins_dict)







def home(request):
    name = 'Komal'

    return redirect('contact')


def login(request):
    return render(request, 'firstapp\login.html')


def form_view(request):

    form = forms.Loginform
    return render(request, 'firstapp\\form.html', {'form': form})
@csrf_exempt
def about(request):
    logins = Login.objects.all()
    login_dict ={'objects':[{'login_name':login.name,'login_email':login.email} for login in logins]}
    login_json = json.dumps(login_dict)
    print('-------------------------------_',login_json)
    if request.method == "POST":
        data= request.POST.dict()
        login = Login.objects.create(name=data.get('name'),email= data.get('email'), password = data.get('password'))
        return HttpResponse('Record created successfully')
    return HttpResponse(login_json)


def contact(request):
    return HttpResponse("This is contact page")
