from django.contrib.auth import get_user_model
from django.test import TestCase

from salesflow.business.models import Business


User = get_user_model()

class BusinessModelTestCase(TestCase):
    field_name = [
        "name",
        "location",
        "country",
        "owner",
        "manager",
        "assistant_manager",
        "date_modified",
        "user_created",
        "user_updated",
        "user_deleted",
    ]

    def setUp(self):
        self.user = User.objects.create(email="test@yahoo.com", password="password")
        self.business = Business.objects.create(
            name="Business",
            location="location",
            country="country",
            owner=self.user,
            user_created=self.user,
        )

    def validate_model_data(self, business_model, business_data):
        for field in self.field_name:
            self.assertEquals(getattr(business_model, field), business_data[field])

    def test_created_business(self):
        expected_data = {
            "name": "Business",
            "location": "location",
            "country": "country",
            "owner": self.user,
            "manager": None,
            "assistant_manager": None,
            "date_modified": None,
            "user_created": self.user,
            "user_updated": None,
            "user_deleted": None,
        }
        self.validate_model_data(self.business, expected_data)

    def test_update_business(self):
        Business.objects.filter(id=self.business.pk).update(name="Business Updated")
        business = Business.objects.get(id=self.business.pk)
        self.assertEquals(business.name, "Business Updated")

    def test_fetch_business(self):
        business = Business.objects.get(id=self.business.pk)
        self.assertEquals(business, self.business)

    def test_delete_business(self):
        Business.objects.get(id=self.business.pk).delete()
        business = Business.objects.filter(id=self.business.pk)
        self.assertEquals(len(business), 0)
