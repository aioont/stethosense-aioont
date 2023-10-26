from django.shortcuts import render, redirect
from .models import LabUser, LabReport
from django.contrib.auth import authenticate, login

def lab_dashboard(request):
    # Assuming the user is logged in and you have access to the LabUser instance
    lab_user = request.user

    # Query the database to get all lab reports associated with the lab user
    lab_reports = LabReport.objects.filter(lab=lab_user)

    context = {
        'user': lab_user,
        'lab_reports': lab_reports,
    }

    return render(request, 'lab_dashboard.html', context)
