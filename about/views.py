from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import About 
from .forms import CollaborationForm

# Create your views here.

def about_me(request):

    if request.method == "POST":
        collaboration_form = CollaborationForm(data=request.POST)
        if collaboration_form.is_valid():
            collaboration_form.save()
            
            messages.add_message(
                request, messages.SUCCESS, 'Collaboration request received! I endeavour to respond within 2 working days.'
            )


    about = About.objects.all().order_by("-updated_on").first()

    collaboration_form = CollaborationForm

    return render(
        request, 
        'about/about.html',
        {
            "about": about,
            "collaboration_form": collaboration_form,
        },
    )


