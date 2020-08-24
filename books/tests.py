from django.test import client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from . models import Book, Review
# Create your tests here.

class BookTest(TestCase):

    def setUp(self):

        self.user= get_user_model().objects.create(
            username='reviewuser',
            email='reviewuser@email.com',
            password = 'Ikea@sachin14',

        )


        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25',
        )

        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            review='An excellent review',
        )

    def test_book_listing(self):
        self.assertEqual(self.book.title,'Harry Potter')
        self.assertEqual(self.book.author,'JK Rowling')
        self.assertEqual(self.book.price,'25')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Harry Potter')
        self.assertTemplateUsed(response,'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/book/12345')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'Harry Potter')
        self.assertContains(response,'An excellent review')
        self.assertTemplateUsed(response,'books/book_detail.html')



        
