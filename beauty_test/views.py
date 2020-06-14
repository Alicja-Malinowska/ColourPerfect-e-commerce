from django.shortcuts import render


# Create your views here.
SEASONS = ['Spring', 'Summer', 'Autumn', 'Winter']
QUESTIONS = {
        "What is the natural colour of your hair?": {'Light to medium blond with warm undertones or light ginger': ['spring'],
                                                     'Light to medium blond with cold undertones': ['summer'], 'Brown to black with warm undertones or dark ginger': ['autumn'],
                                                     'Brown to black with cold undertones': ['winter']},

        "What is the colour of your eyes?": {'Light and vivid blue, green or amber': ['spring'],
                                             'Light and ashy blue, green or gray': ['summer'], 'Dark and warm brown or hazel': ['autumn'],
                                             'Dark and deep brown or gray': ['winter']},

        "Look at your veins, what colour are they?": {'Green': ['spring', 'autumn'], 'Blue': ['summer', 'winter']},

        "Is there a big contrast between your skin colour and your natural hair colour?": {'Yes': ['winter'],
                                                                                           'No': ['spring', 'summer', 'autumn']},

        "Do you look better in gold or silver jewellery?": {'Gold': ['spring', 'autumn'], 'Silver': ['summer', 'winter']}

    }

def questions(request):
    '''renders all the questions'''
    context = {
        'questions': QUESTIONS
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
    
    context = {
        'result': result
    }
    return render(request, 'test-result.html', context)
