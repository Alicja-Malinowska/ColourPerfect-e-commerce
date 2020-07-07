from django.shortcuts import render, redirect, reverse

# Create your views here.
def about_us(request):
    ''' render about-us page '''

    return render(request, 'about-us.html')

def delivery_returns(request):
    ''' take user to the delivery and return section of the about us page '''

    return redirect(reverse('about_us') + '#delivery-returns')