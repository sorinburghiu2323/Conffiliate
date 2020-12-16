from django.http import JsonResponse
from django.shortcuts import render
from affiliate_mvp.models import PreRegisterUser


def index(request):

    if request.POST.get('action') == "post":

        email = request.POST.get('email')

        if "@" not in email:
            return JsonResponse({"update": "ERROR: Email field cannot be empty."})
        if PreRegisterUser.objects.filter(email=email).exists():
            return JsonResponse({"update": "ERROR: There is already an account using this email."})

        new_pre = PreRegisterUser.objects.create(email=email)
        new_pre.save()
        return JsonResponse({"update": "SUCCESS: Thank you for pre-registering."})

    return render(request, 'index.html')
