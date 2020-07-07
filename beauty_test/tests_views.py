from django.test import TestCase

# Create your tests here.

class TestBeautyTestViews(TestCase):

    def test_get_test_questions_page(self):

        response = self.client.get("/test/questions")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "beauty-test.html")
    
    def test_get_test_result_page(self):

        response = self.client.get("/test/results")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "test-result.html")
    
    def test_get_correct_test_result(self):

        response = self.client.post("/test/results", {
            'What is the natural colour of your hair?': ['Light to medium blond with warm undertones or light ginger'], 
            'What is the colour of your eyes?': ['Light and vivid blue, green or amber'], 
            'Look at your veins, what colour are they?': ['Green'], 
            'Is there a big contrast between your skin colour and your natural hair colour?': ['Yes'], 
            'Do you look better in gold or silver jewellery?': ['Gold']})
        
        self.assertEqual(response.context['result'], 'Spring')
    
    def test_gest_suggested_products(self):

        response = self.client.post("/test/results", {
            'What is the natural colour of your hair?': ['Light to medium blond with warm undertones or light ginger'], 
            'What is the colour of your eyes?': ['Light and vivid blue, green or amber'], 
            'Look at your veins, what colour are they?': ['Green'], 
            'Is there a big contrast between your skin colour and your natural hair colour?': ['Yes'], 
            'Do you look better in gold or silver jewellery?': ['Gold']})

        
        self.assertEqual(type(response.context['products']), list)

        