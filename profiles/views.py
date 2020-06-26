from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from profiles.models import Profile
from profiles.forms import ProfileForm

# Create your views here.
def profile(request):
    
    profile = get_object_or_404(Profile, owner=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your details have been saved'))
        else:
            messages.error(request, ('An error occured, please check your form.'))
                           
    else:
        form = ProfileForm(instance=profile)

    orders = profile.orders.all()

    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, 'profile.html', context)