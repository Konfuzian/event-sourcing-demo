from warehouse_product_repository import WarehouseProductRepository

class Quantity():
	def __init__(self, quantity: int):
		self.quantity = quantity
	
	def is_valid(self) -> bool:
		return True


def get_sku_from_console():
	return input("Enter sku: ")

def get_quantity():
	return Quantity(int(input("Enter quantity: ")))

def get_adjustment_reason():
	return input("Enter reason: ")


warehouse_product_repository = WarehouseProductRepository()

print("R: Receive Inventory")
print("S: Ship Inventory")
print("A: Adjust Inventory")
print("Q: Quantity On Hand")
print("E: Events")
print("X: Exit")

key = input("> ").upper()
while (key != "X"):
	sku = get_sku_from_console()
	warehouse_product = warehouse_product_repository.get(sku)

	match key:
		case "R":
			receive_input = get_quantity()
			if (receive_input.is_valid()):
				warehouse_product.receive_product(receive_input.quantity)
				print(f"{sku} received: {receive_input.quantity}")

		case "S":
			ship_input = get_quantity()
			if (ship_input.is_valid()):
				warehouse_product.ship_product(ship_input.quantity)
				print(f"{sku} shipped: {ship_input.quantity}")

		case "A":
			adjustment_input = get_quantity()
			if (adjustment_input.is_valid()):
				reason = get_adjustment_reason()
				warehouse_product.adjust_inventory(adjustment_input.quantity, reason)
				print(f"{sku} adjusted: {adjustment_input.quantity} ({reason})")

		case "Q":
			current_quantity_on_hand = warehouse_product.get_quantity_on_hand()
			print(f"{sku} quantity on hand: {current_quantity_on_hand}")

		case "E":
			print("{sku} events:")
			for event in warehouse_product.get_events():
				print(event)
	
	warehouse_product_repository.save(warehouse_product)
	print(f"\n{warehouse_product}")
	input()

	print("R: Receive Inventory")
	print("S: Ship Inventory")
	print("A: Adjust Inventory")
	print("Q: Quantity On Hand")
	print("E: Events")
	print("X: Exit")

	key = input("> ").upper()
	print()