from msilib import schema
from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models, schemas


def get_menu(db: Session):
    return db.query(models.Item).all()

def get_item(db: Session, item_id: int):
    return db.get(models.Item, id=item_id)

def add_item(db: Session, item: schemas.Item):
    item_instance = models.Item(name=item.name, cost=item.cost, type=item.type, isavailable=item.isavailable)
    db.add(item_instance)
    db.commit()
    db.refresh(item_instance)

    return item_instance

def get_tables(db:Session):
    return db.query(models.Table).all()

def add_table(db:Session, table_entry:schemas.Table):
    
    table_instance = models.Table(seats = table_entry.seats, isoccupied=table_entry.isoccupied)
    db.add(table_instance)
    db.commit()
    db.refresh(table_instance)

    return table_instance

def add_customer(db:Session, customer:schemas.Customer):

    customer_instance = models.Customer(phone_number=customer.phone_number)

    db.add(customer_instance)

    db.commit()
    db.refresh(customer_instance)

    return customer_instance

def add_table_order(db:Session, order:schemas.OrderEntry):

    order_instance = models.Orders(table_id=order.table_id, item_id=order.item_id, quantity_ordered=order.quantity)

    db.add(order_instance)

    db.commit()
    db.refresh(order_instance)

    return order_instance

def get_table_items_ordered_by_table_id(db:Session, table_id:int):

    stmt = select(models.Orders).where(models.Orders.table_id == table_id)

    result = db.execute(stmt)

    return result.all()

def get_order(db:Session, entry:schemas.OrderEntry):

    with db:
        
        result = db.query(models.Orders) \
                 .filter_by(table_id=entry.table_id, item_id=entry.item_id) \
                 .one()
        return result

