from django.test import TestCase, RequestFactory, Client
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from datetime import datetime, date
from .models import Booking, Menu
from django.urls import reverse
from .views import MenuItemsView


class BookingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.booking = Booking.objects.create(
            first_name = "Subash",
            no_of_guests = 4,
            reservation_date =date.today() #"2024-02-15"
        )
    
    def test_fields(self):
        self.assertIsInstance(self.booking.first_name, str)

    def test_times_stamps(self):
        self.assertIsInstance(self.booking.reservation_date, date)

class MenuModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.menu = Menu.objects.create(
            title = "Flafel",
            price = 3.25,
            inventory =10
        )
    
    def test_fields(self):
        self.assertIsInstance(self.menu.title, str)
        self.assertIsInstance(self.menu.price, float)
        self.assertIsInstance(self.menu.inventory, int)

    def test_get_item(self):
        item = Menu.objects.create(
            title="IceCream",
            price=5.23,
            inventory=2
        )
        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCream : 5.23")
        self.assertEqual(item.__str__(), "IceCream : 5.23")

class MenuViewTest (TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.menu = Menu.objects.create(
            title = "Pizza",
            price = 13.25,
            inventory =10
        )


    def test_title_label(self):
        menu = Menu.objects.get(title="Pizza")
        field_label = menu._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_title_max_length(self):
        menu = Menu.objects.get(title="Pizza")
        max_length = menu._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_last_name_comma_first_name(self):
        menu = Menu.objects.get(title="Pizza")
        expected_object_name = f'{menu.title} : {menu.price}'
        self.assertEqual(str(menu), expected_object_name)

    def setUp(self):
        self.client = Client()
        self.menu1 = menu= Menu.objects.create(
            title = "Foul",
            price = 3.25,
            inventory =10
        )
        self.menu2 = menu= Menu.objects.create(
            title = "Lentil",
            price = 3.25,
            inventory =10
        )
        self.client = APIClient()
        self.user = User.objects.create_superuser('admin1', 'admin@admin.com', 'admin1234')
        self.token = Token.objects.create(user=self.user)
       

    def test_menu_items_view(self):
             
        response = RequestFactory().get('/menu-items/', HTTP_AUTHORIZATION=f"Token {self.token.key}", format='json')
        view = MenuItemsView.as_view()(response)
        self.assertEqual(view.status_code, 200)
        self.assertContains(view, self.menu1.title)
        self.assertContains(view, self.menu2.title)
        self.assertNotContains(view, 'Lentil2')

        # client.credentials()

    def test_getall(self):
        item = Menu.objects.all()
        self.assertEqual(len(item), 3)


   

    # def getToday( self ):
    #     return datetime.date.today()
    # def getNow( self ):
    #     return datetime.datetime.now()