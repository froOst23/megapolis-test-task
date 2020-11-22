from django.shortcuts import render
from .models import *

def index(request):
    current_user = request.user.id
    subsidiary_model = Subsidiary.objects.filter(user=current_user)
    subcontractor_model = Subcontractor.objects.filter(user=current_user)
    contract_model = Contract.objects.all()
    return render(
        request,
        'main/index.html',
        {
            'subsidiary_model': subsidiary_model,
            'subcontractor_model': subcontractor_model
        }
    )


def profile(request):
    return render(request, 'main/profile.html')
