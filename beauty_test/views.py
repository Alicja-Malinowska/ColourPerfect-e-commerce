from django.shortcuts import render
from beauty_test.test_questions import QUESTIONS
from helpers.seasons import SEASONS
from helpers.category_brand import categories, brands
from helpers.get_products_and_colours import get_products
from products.models import Colour


# Create your views here.


def questions(request):
    '''renders all the questions'''
    context = {
        'questions': QUESTIONS,
        'categories': categories,
        'brands': brands,
    }

    return render(request, 'beauty-test.html', context)

def results(request):
    '''gets all the answers and checks which season are the majority of answers related to'''
    answers = request.POST
    result_list = []

    for question, answer in answers.items():
        try:
            result_list += QUESTIONS[question][answer] 
        except:
            pass
            
    most_occurances = max([(result_list.count(season.lower()), season) for season in SEASONS])
    result = most_occurances[1]

    products = get_products(result, '?')
    colours = Colour.objects.filter(season=result.lower()).order_by('?')[:12]
    
    context = {
        'result': result,
        'categories': categories,
        'brands': brands,
        'products': products,
        'colours': colours,
    }
    return render(request, 'test-result.html', context)
