from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email='test@gmail.com', password='qazqazqaz'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    
    def test_create_user_with_email_successfull(self):
        # test creating a new user with an email is successfull
        email = "test@test.com"
        password = "guest"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password, password)
    
        
    def test_new_user_email_normalized(self):
        email = "test@TE.com"
        user = get_user_model().objects.create_user(email, 'ew')
        
        self.assertEqual(user.email, email.lower())
    
        
    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test')
    
            
    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'q@q.com', 
            'red'
        )
        self.assertTrue(user.is_superuser),
        self.assertTrue(user.is_staff)
        
        
    def test_tag_str(self):
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Meater'
        )
        self.assertEqual(str(tag), tag.name)
        
        
    def test_ingredient_str(self):
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Melon'
        )
        self.assertEqual(str(ingredient), ingredient.name)
        
    
    def test_receipe_str(self):
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Prime Rib',
            time_minutes=75,
            price=80.00
        )
        self.assertEqual(str(recipe), recipe.title)