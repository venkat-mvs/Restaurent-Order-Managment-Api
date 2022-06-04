from sqlalchemy.orm import Session

from . import models, schemas


def get_menu(db: Session):
    return db.query(models.Item).all()


def add_item(db: Session, item: schemas.Item):

    item_instance = models.Item(name=item.name, cost=item.cost, type=item.type, isavailable=item.isavailable)

    db.add(item_instance)

    db.commit()
    db.refresh(item_instance)

    return item_instance