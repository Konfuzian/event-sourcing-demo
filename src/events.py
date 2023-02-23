# TODO: try with protocols instead of classes

class Event:
    pass

class ProductShipped(Event):
    def __init__(self, sku, quantity, datetime):
        self.sku = sku
        self.quantity = quantity
        self.datetime = datetime
    
    def __repr__(self):
        return f"{self.datetime} | sku {self.sku} shipped: {self.quantity}"

class ProductReceived(Event):
    def __init__(self, sku, quantity, datetime):
        self.sku = sku
        self.quantity = quantity
        self.datetime = datetime
    
    def __repr__(self):
        return f"{self.datetime} | sku {self.sku} received: {self.quantity}"

class InventoryAdjusted(Event):
    def __init__(self, sku, quantity, reason, datetime):
        self.sku = sku
        self.quantity = quantity
        self.reason = reason
        self.datetime = datetime
    
    def __repr__(self):
        return f"{self.datetime} | sku {self.sku} received: {self.quantity} ({self.reason})"
