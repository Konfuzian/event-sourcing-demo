# TODO: try with protocols instead of classes

class Event:
    pass

class ProductShipped(Event):
    def __init__(self, sku, quantity, datetime):
        self.sku = sku
        self.quantity = quantity
        self.datetime = datetime

class ProductReceived(Event):
    def __init__(self, sku, quantity, datetime):
        self.sku = sku
        self.quantity = quantity
        self.datetime = datetime

class InventoryAdjusted(Event):
    def __init__(self, sku, quantity, reason, datetime):
        self.sku = sku
        self.quantity = quantity
        self.reason = reason
        self.datetime = datetime
