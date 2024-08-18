import stripe
from config.settings import STRIPE_API_KEY
stripe.api_key = STRIPE_API_KEY


def create_stripe_product():
    return stripe.Product.create(name="Course")


def create_stripe_price(amount, product):
    """Создает цену на платеж"""
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product_data={"name": product},
    )


def create_stripe_sessions(price):
    """Создает сессию на оплату"""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 2}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
