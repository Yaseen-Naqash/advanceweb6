import random
from datetime import date, timedelta
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.utils.text import slugify

# Replace 'your_app' with your actual app name
from base.models import User, Product, Category, Tag, Cart, OrderedProduct


class Command(BaseCommand):
    help = "Populate the database with dummy data for testing the admin panel"

    def add_arguments(self, parser):
        parser.add_argument(
            '--products',
            type=int,
            default=30,
            help='Number of products to create (default: 30)',
        )
        parser.add_argument(
            '--users',
            type=int,
            default=5,
            help='Number of users to create (default: 5)',
        )
        parser.add_argument(
            '--flush',
            action='store_true',
            help='Delete existing dummy data before creating new data',
        )

    def handle(self, *args, **options):
        num_products = options['products']
        num_users = options['users']

        if options['flush']:
            self.stdout.write(self.style.WARNING('Flushing existing data...'))
            OrderedProduct.objects.all().delete()
            Cart.objects.all().delete()
            Product.objects.all().delete()
            Tag.objects.all().delete()
            Category.objects.all().delete()
            User.objects.filter(is_superuser=False).delete()

        # ---------- Categories ----------
        category_titles = [
            'Electronics', 'Clothing', 'Books', 'Home & Kitchen',
            'Sports', 'Toys', 'Beauty', 'Automotive', 'Garden', 'Food',
        ]
        categories = []
        for title in category_titles:
            cat, _ = Category.objects.get_or_create(title=title)
            categories.append(cat)
        self.stdout.write(self.style.SUCCESS(f'✓ Categories: {len(categories)}'))

        # ---------- Tags ----------
        tag_titles = [
            'new', 'sale', 'bestseller', 'limited', 'eco-friendly',
            'premium', 'budget', 'imported', 'handmade', 'gift',
        ]
        tags = []
        for title in tag_titles:
            tag, _ = Tag.objects.get_or_create(title=title)
            tags.append(tag)
        self.stdout.write(self.style.SUCCESS(f'✓ Tags: {len(tags)}'))

        # ---------- Users ----------
        first_names = ['Ali', 'Sara', 'Reza', 'Mina', 'Hassan', 'Neda', 'Omid', 'Laleh']
        last_names = ['Ahmadi', 'Karimi', 'Hosseini', 'Rezaei', 'Mohammadi', 'Sadeghi']

        users = []
        for i in range(num_users):
            first = random.choice(first_names)
            last = random.choice(last_names)
            username = f'user_{slugify(first)}_{i}'
            email = f'{username}@example.com'

            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': first,
                    'last_name': last,
                    'email': email,
                    'phone': f'0912{random.randint(1000000, 9999999)}',
                },
            )
            if created:
                user.set_password('password123')
                user.save()
            users.append(user)
        self.stdout.write(self.style.SUCCESS(f'✓ Users: {len(users)}'))

        # ---------- Products ----------
        adjs = ['Premium', 'Classic', 'Modern', 'Vintage', 'Deluxe',
                'Compact', 'Pro', 'Ultra', 'Smart', 'Eco']
        nouns = ['Widget', 'Gadget', 'Device', 'Tool', 'Item',
                 'Accessory', 'Kit', 'Unit', 'Box', 'Set']

        products = []
        for i in range(num_products):
            title = f'{random.choice(adjs)} {random.choice(nouns)} {i + 1}'
            price = random.randint(10_000, 5_000_000)
            quantity = random.randint(0, 500)
            discount = random.choice([0, 0, 0, 5, 10, 15, 20, 25, 50])

            product = Product(
                title=title,
                description=(
                    f'This is a detailed description for "{title}". '
                    'It is a high-quality product suitable for everyday use. '
                    'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
                ),
                price=price,
                quantity=quantity,
                instock=quantity > 0,
                rating=Decimal(str(round(random.uniform(1.0, 5.0), 1))),
                category=random.choice(categories),
                size=random.choice([choice[0] for choice in Product.SIZES]),
                discount=discount,
                Expire=date.today() + timedelta(days=random.randint(30, 730)),
            )
            product.save()

            # Attach 1-3 random tags
            product.tags.set(random.sample(tags, k=random.randint(1, 3)))
            products.append(product)
        self.stdout.write(self.style.SUCCESS(f'✓ Products: {len(products)}'))

        # ---------- Carts & Ordered Products ----------
        cart_count = 0
        ordered_count = 0
        for user in users:
            # Each user gets 0-2 carts
            for _ in range(random.randint(0, 2)):
                cart = Cart.objects.create(user=user)
                cart_count += 1

                # Add 1-5 products to each cart
                chosen = random.sample(products, k=min(random.randint(1, 5), len(products)))
                for product in chosen:
                    OrderedProduct.objects.create(
                        cart=cart,
                        product=product,
                        quantity=random.randint(1, 4),
                        size=random.choice([choice[0] for choice in Product.SIZES]),
                    )
                    ordered_count += 1
        self.stdout.write(self.style.SUCCESS(
            f'✓ Carts: {cart_count}, OrderedProducts: {ordered_count}'
        ))

        self.stdout.write(self.style.SUCCESS('\n🎉 Dummy data created successfully!'))
        self.stdout.write(f'   Users password: "password123"')