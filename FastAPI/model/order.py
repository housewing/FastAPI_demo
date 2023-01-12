from pydantic import BaseModel
from typing import List, Union
from model.order_item import OrderItem

class Order(BaseModel):
    order_id: Union[str, None] = None
    customer_id: str
    customer_name: str
    purchase_time: Union[str, None] = None
    order_item: List[OrderItem]
