from warehouse_product_repository import WarehouseProductRepository

def get_quantity():
	return int(input("Enter quantity: "))

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
	sku = input("Enter sku: ")
	warehouse_product = warehouse_product_repository.get(sku)

	match key:
		case "R":
			quantity = int(input("Enter quantity: "))
			warehouse_product.receive_product(quantity)
			print(f"{sku} received: {quantity}")

		case "S":
			quantity = int(input("Enter quantity: "))
			warehouse_product.ship_product(quantity)
			print(f"{sku} shipped: {quantity}")

		case "A":
			quantity = int(input("Enter quantity: "))
			reason = input("Enter reason: ")
			warehouse_product.adjust_inventory(quantity, reason)
			print(f"{sku} adjusted: {quantity} ({reason})")

		case "Q":
			print(f"{sku} quantity on hand: {warehouse_product.get_quantity_on_hand()}")

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