from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from categories.models import Category
from products.models import Product


class Command(BaseCommand):

    help = "Seed the database with sample data"

    def handle(self, *args, **kwargs):

        User = get_user_model()

        if not User.objects.filter(username="admin").exists():

            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="Admin@123"
            )

            self.stdout.write(
                self.style.SUCCESS("Superuser Created")
            )

        electronics, created = Category.objects.get_or_create(
            name="Electronics"
        )

        Product.objects.get_or_create(
            name="iPhone 16",
            defaults={
                "description": "Apple Smartphone",
                "price": 89999,
                "stock": 10,
                "category": electronics,
            }
        )

        Product.objects.get_or_create(
            name="Samsung S25",
            defaults={
                "description": "Samsung Smartphone",
                "price": 79999,
                "stock": 15,
                "category": electronics,
            }
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Database seeded successfully!"
            )
        )