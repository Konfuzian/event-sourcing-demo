from warehouse_product import WarehouseProduct
from events import Event

class WarehouseProductRepository():
	# this keeps track of all the events on a per-sku basis
	_in_memory_streams: dict[list[Event]] = {}

	# whenever we get a product from the repository, we create a new WarehouseProduct and replay all the events
	def get(self, sku: str) -> WarehouseProduct:
		warehouse_product = WarehouseProduct(sku)

		if sku in self._in_memory_streams:
			for event in self._in_memory_streams[sku]:
				warehouse_product.add_event(event)

		return warehouse_product

	# saving a product updates self._in_memory_streams with the current events for the product 
	def save(self, warehouse_product: WarehouseProduct) -> None:
		self._in_memory_streams[warehouse_product.sku] = warehouse_product.get_events()
