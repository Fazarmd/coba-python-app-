class Order:
  def __init__(self, order_id, costumer_name, order_date, total_amount):
    self.order_id = order_id
    self.costumer_name = costumer_name
    self.order_date = order_date
    self.total_amount = total_amount

  def calculate_tax(self, tax_rate):
    return self.total_amount * tax_rate
  
  def display_order(self):
    print(f"Order ID: {self.order_id}")
    print(f"Costumer Name: {self.costumer_name}")
    print(f"Order Date: {self.order_date}")
    print(f"Total Amount: {self.total_amount}\n")

class OrderProcessor:
  def __init__(self):
    self.orders = []

  def add_order(self, order):
    self.orders.append(order)

  def calculate_total_revenue(self):
    return sum(order.total_amount for order in self.orders)
  
  def calculate_total_tax(self, tax_rate):
        return sum(order.calculate_tax(tax_rate) for order in self.orders)
  
  def display_order(self):
    for order in self.orders:
      order.display_order()


orderan = OrderProcessor()

order1 = Order("ORD001", "Ayam", "12-08-2024", 100000)
order2 = Order("ORD002", "Bebek", "13-08-2024", 150000)
order3 = Order("ORD003", "Cicak", "14-08-2024", 75000)

orderan.add_order(order1)
orderan.add_order(order2)
orderan.add_order(order3)

total_revenue = orderan.calculate_total_revenue()
print(f"Total Pendapatan: {total_revenue}")

tax_rate = 0.1
total_tax = orderan.calculate_total_tax(tax_rate)
print(f"Total Pajak: {total_tax}")

print("\nDetail Pesanan:")
orderan.display_order()