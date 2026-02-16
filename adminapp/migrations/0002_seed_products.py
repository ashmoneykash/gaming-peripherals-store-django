from django.db import migrations

def seed_products(apps, schema_editor):
    Product = apps.get_model('adminapp', 'Product')

    if Product.objects.exists():
        return

    products = [
        {
            "name": "NexGen Phantom X Mechanical Keyboard",
            "description": "RGB mechanical keyboard with ultra-fast response time and tournament-grade durability.",
            "price": 7999,
            "stock": 15,
        },
        {
            "name": "NexGen Velocity Pro Gaming Mouse",
            "description": "Lightweight ergonomic gaming mouse with 8000Hz polling rate and precision sensor.",
            "price": 3499,
            "stock": 20,
        },
        {
            "name": "NexGen Titan Wireless Headset",
            "description": "Low-latency wireless headset with immersive surround sound and noise cancellation.",
            "price": 6999,
            "stock": 12,
        },
        {
            "name": "NexGen Control Master Gamepad",
            "description": "Precision controller with haptic feedback and ultra-responsive triggers.",
            "price": 4999,
            "stock": 18,
        },
        {
            "name": "NexGen Stealth XL Mousepad",
            "description": "Extended anti-slip mousepad optimized for speed and control.",
            "price": 1499,
            "stock": 25,
        },
    ]

    for item in products:
        Product.objects.create(**item)


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),  # keep your correct dependency
    ]

    operations = [
        migrations.RunPython(seed_products),
    ]
