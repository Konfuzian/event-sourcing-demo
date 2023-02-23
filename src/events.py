# TODO: try with protocols instead of classes
from datetime import datetime

class Event:
    pass

class ProductShipped(Event):
    def __init__(self, sku: str, quantity: int, datetime: datetime) -> None:
        self.sku = sku
        self.quantity = quantity
        self.datetime = datetime
    
    def __repr__(self) -> str:
        return f"{self.datetime} | sku {self.sku} shipped: {self.quantity}"

class ProductReceived(Event):
    def __init__(self, sku: str, quantity: int, datetime: datetime) -> None:
        self.sku = sku
        self.quantity = quantity
        self.datetime = datetime
    
    def __repr__(self) -> str:
        return f"{self.datetime} | sku {self.sku} received: {self.quantity}"

class InventoryAdjusted(Event):
    def __init__(self, sku: str, quantity: int, reason: str, datetime: datetime) -> None:
        self.sku = sku
        self.quantity = quantity
        self.reason = reason
        self.datetime = datetime
    
    def __repr__(self) -> str:
        return f"{self.datetime} | sku {self.sku} received: {self.quantity} ({self.reason})"
