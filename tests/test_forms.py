from django.test import SimpleTestCase
from bomberos_quilpue.forms import RegistroForm

class TestRegistroForm(SimpleTestCase):
   
    def test_registro_valido(self):
        form = RegistroForm(data={
           'nombre':'camila',
            'apellidos':"valdivia",
            'rut':"17560732-3",
            'region':"1",
            'ciudad':"1",
            'fecha_nacimiento':"01/12/1980",
            'numero_telefono':"+569-12345678",
            'email':"camila@chile.com",
            
        })         
        
        self.assertFalse(form.is_valid())
    
    def test_registro_sin_data(self):
        
        form = RegistroForm(data={})   

        #self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 13)