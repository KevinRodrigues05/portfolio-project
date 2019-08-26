from django.shortcuts import render

from .models import Job


def home(request):

    jobs = Job.objects
    # print(jobs)
    return render(request, 'jobs/home.html', {'jobs': jobs})
