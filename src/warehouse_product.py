from datetime import datetime
from events import Event, ProductReceived, ProductShipped, InventoryAdjusted

class CurrentState():
	quantity_on_hand = 0

class WarehouseProduct():
	sku: str
	_events: list[Event]

	_current_state: CurrentState

	def __init__(self, sku: str) -> None:
		self.sku = sku
		self._events = []
		self._current_state = CurrentState()
	
	def __repr__(self) -> str:
		return f"WarehouseProduct(sku: {self.sku}, quantity_on_hand: {self._current_state.quantity_on_hand})"

	def ship_product(self, quantity: int) -> None:
		if quantity > self._current_state.quantity_on_hand:
			raise Exception("We don't have enough product to ship")
		self.add_event(ProductShipped(self.sku, quantity, datetime.now()))

	def receive_product(self, quantity: int) -> None:
		self.add_event(ProductReceived(self.sku, quantity, datetime.now()))

	def adjust_inventory(self, quantity: int, reason: str) -> None:
		if self._current_state.quantity_on_hand + quantity < 0:
			raise Exception("Cannot adjust to a negative stock")
		self.add_event(InventoryAdjusted(self.sku, quantity, reason, datetime.now()))

	def get_events(self) -> list[Event]:
		return self._events

	def add_event(self, event: Event) -> None:
		self.apply(event)
		self._events.append(event)

	# youtube video has 3 different apply methods, one for each event type
	def apply(self, event: Event) -> None:
		match event:
			case ProductShipped(event):
				self._current_state.quantity_on_hand -= event.quantity
			case ProductReceived(event):
				self._current_state.quantity_on_hand += event.quantity
			case InventoryAdjusted(event):
				self._current_state.quantity_on_hand += event.quantity

	def get_quantity_on_hand(self) -> int:
		return self._current_state.quantity_on_hand
