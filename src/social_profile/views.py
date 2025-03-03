from django.shortcuts import render
from .models import SocialProfile
from .forms import SocialProfileModalForm
from django.shortcuts import render

# Create your views here.
def myprofile_view(request):
    profile = SocialProfile.objects.get(user=request.user)
    form = SocialProfileModalForm(
        request.POST or None, 
        request.FILES or None, 
        instance=profile,
    )
    confirm = False

    if request.method == "POST":
        if form.is_valid():
            form.save()
            confirm = True

    data = {
        'profile': profile,
        'form': form,
        'confirm': confirm
    }

    return render(request, 'social_profile/myprofile.html', data)