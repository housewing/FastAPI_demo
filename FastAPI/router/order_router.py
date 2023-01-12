from fastapi import APIRouter, HTTPException, status
from model.order_model import OrderModel
from model.order import Order

router = APIRouter()

@router.post('/order/add', status_code=status.HTTP_200_OK)
async def order_add(order: Order):
    order_model = OrderModel()
    order_model.Add(order)
    return {"add_order": order}

@router.post('/order/modify', status_code=status.HTTP_200_OK)
async def order_modify(order: Order):
    order_model = OrderModel()
    order_model.Update(order)
    return {"modify_order": order}

@router.post('/order/delete')
async def order_delete(obj: dict):
    if 'order_id' not in obj:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="order_id error"
        )

    order_id = obj['order_id']
    order_model = OrderModel()
    order_model.Delete(order_id)
    return {"delete_order": order_id}
