from pydantic import BaseModel

class OrderItem(BaseModel):
    product_id: str
    product_name: str
    amount: int
    price: int
