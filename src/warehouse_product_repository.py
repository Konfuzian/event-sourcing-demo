from warehouse_product import WarehouseProduct

class WarehouseProductRepository():
	_in_memory_streams = {}

	def get(self, sku: str) -> WarehouseProduct:
		warehouse_product = WarehouseProduct(sku)

		if sku in self._in_memory_streams:
			for event in self._in_memory_streams[sku]:
				warehouse_product.add_event(event)

		return warehouse_product

	def save(self, warehouse_product: WarehouseProduct):
		self._in_memory_streams[warehouse_product.sku] = warehouse_product.get_events()
