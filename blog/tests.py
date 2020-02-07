from django.test import TestCase
from bomberos_quilpue.forms import RegistroForm,PostForm,UserCreationForm,CommentForm
from bomberos_quilpue.models import Region, Ciudad
from django.test import SimpleTestCase

#esperando colocar pruebas
from bomberos_quilpue.forms import RegistroForm
#TestCase
class TestRegistroForm(TestCase):
   
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
        
        self.assertTrue(form.is_valid())
    
    def test_registro_sin_data(self):
        
        form = RegistroForm(data={})   

        self.assertFalse(form.is_valid())

#TestCase
class TestUserCreationForm(TestCase):

#Arrange
    def test_usuario_valido(self):
#Act
        form = UserCreationForm(data={
            'username':'sinproyecto',
            'email':"bomberosquilpueg@gmail.com",
            'password1':"hola+12345",
            'password2':"hola+12345",
        })         
        
#Assert

        self.assertTrue(form.is_valid())
#Arrange
            
    def test_usuario_sin_data(self):
#Act
                
        form = UserCreationForm(data={})   
       
#Assert
        self.assertFalse(form.is_valid())

#@TestCase

class TestPostForm(TestCase):

#Arrange
    def test_post_valido(self):
#Act
#Falla por que no tiene imagen
        form = PostForm(data={
            'author':'bomberos',
            'title':'nuevos autos',
            'imagen':'hello', 
            'text':'hello',
            'texttwo':'bye'
        })         
        
#Assert

        self.assertTrue(form.is_valid())
#Arrange
            
    def test_post_sin_data(self):
#Act
                
        form = PostForm(data={})   
       
#Assert
        self.assertFalse(form.is_valid())



class TestCommentForm(TestCase):



#Arrange
    def test_comentario_valido(self):
#Act
        form = CommentForm(data={
            'author':'none',
            'text':'hello',
            
        })         
        
#Assert

        self.assertTrue(form.is_valid())
#Arrange
            
    def test_comentario_sin_autor(self):
#Act
                
        form = RegistroForm(data={})   
       
#Assert
        self.assertFalse(form.is_valid())