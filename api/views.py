from .models import Info
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse

from rest_framework.views import APIView

class Signup(APIView):
    def post(self, request):
        data = request.data
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        register = Info(name=name,email=email,password=password)
        register.save()
        response = {
            "name": register.name,
            "email": register.email,
            "password": register.password
        }
        # return HttpResponse("Data Saved")
        return JsonResponse({"data": response})
