from django.shortcuts import render, redirect, reverse

# Create your views here.
def about_us(request):

    return render(request, 'about-us.html')

def delivery_returns(request):

    return redirect(reverse('about_us') + '#delivery-returns')