from API.db import utils, crud, models, schemas


def mapper(db_order: models.Orders):
    return schemas.OrderEntry(**db_order.__dict__)

class BillingService:

    def get_bill(self, table_id:int):
        
        orders_by_item:dict[int, models.Orders] = self.get_order_data(table_id)
        menu:list[models.Item] = self.get_menu()
        item_ids = list(orders_by_item.keys())
        ordered_items:list[models.Item] = [
            item for item in menu if item.id in item_ids
        ]

        ''' 
            cost calculation
                sum(cost_per_item*quantity_ordered for each item in order)
        '''
        cost_per_item = [item.cost*orders_by_item[item.id].quantity_ordered for item in ordered_items]
        billed_items = self.build_billed_items(ordered_items, orders_by_item)
        bill = schemas.Bill(items=billed_items, cost=sum(cost_per_item))

        return bill

    def build_billed_items(self, ordered_items:list[models.Item] , orders_by_item:dict[int, models.Orders]):

        items = [
            schemas.BillItem(name=item.name, cost=item.cost, count=orders_by_item[item.id].quantity_ordered) 
            for item in ordered_items
        ]

        return list(items)

    def get_order_data(self, table_id:int):
        db = next(utils.get_db())
        data = crud.get_table_items_ordered_by_table_id(db, table_id)
        data_dict = { row['Orders'].item_id: row['Orders'] for row in data}

        return data_dict

    def get_menu(self):
        db = next(utils.get_db())
        data = crud.get_menu(db)
        return data
