import random
from datetime import date

def get_sales_summary():
    """Simulate fetching aggregated sales data."""
    return {
        "date": str(date.today()),
        "total_sales": random.randint(5000, 25000),
        "region": "Global",
        "top_product": "AI Chat Subscription",
        "growth_pct": round(random.uniform(3.5, 12.7), 2),
    }

def get_customer_info(customer_id: int):
    """Simulate fetching a single customer's data."""
    fake_customers = {
        1: {"name": "Alice", "region": "Europe", "purchases": 12},
        2: {"name": "Bob", "region": "North America", "purchases": 7},
        3: {"name": "Carla", "region": "Asia", "purchases": 15},
    }
    return fake_customers.get(customer_id, {"error": "Customer not found"})

def list_customers():
    """Simulate fetching a list of all customers."""
    return [
        {"id": 1, "name": "Alice", "region": "Europe"},
        {"id": 2, "name": "Bob", "region": "North America"},
        {"id": 3, "name": "Carla", "region": "Asia"},
    ]
