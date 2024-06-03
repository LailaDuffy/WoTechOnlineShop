import datetime;

class Client:
  number_of_clients = 0

  def __init__(self, name, postage_address, payment_details):
    self.name = name
    self.transactions = []
    self.postage_address = postage_address
    self.payment_details = payment_details
    Client.number_of_clients += 1

  def create_provisional_transaction(self, transaction):
    self.transactions.append(transaction)
    
class Item:
  def __init__(self, name, serial_no, price):
    self.name = name
    self.serial_no = serial_no
    self.price = price

class Transaction:
  def __init__(self, no, total_amount = 0.0):
    self.no = no
    self.total_amount = total_amount
    self.purchased_items = []
    self.time_stamp = datetime.datetime.now()
  
  def add_item(self, item):
    self.purchased_items.append(item)

  def calculate_total_transaction_amount(self):
    self.total_amount = sum(item.price for item in self.purchased_items)

# creating a list for clients and adding new clients
clients = []
clients.append(Client('Amy Stake', '123 Street, Dallas', 'Bank transfer'))
clients.append(Client('Barb Dwyer', '66 Townhouse, New York', 'Card payment'))
clients.append(Client('Toby Lerone', '909 Park Street, Ohio', 'Card payment'))

for client in clients:
  print(f"Client's name: {client.name},\n  Address: {client.postage_address},\n  Payment: {client.payment_details}")
print(f'The total number of clients: {Client.number_of_clients}')

# adding a transaction placeholder for each client
clients[0].create_provisional_transaction(Transaction('TR0001'))
clients[1].create_provisional_transaction(Transaction('TR0002'))
clients[2].create_provisional_transaction(Transaction('TR0003'))
clients[2].create_provisional_transaction(Transaction('TR0004'))

for client in clients:
  print(f'{client.name} has the following transactions: ')
  for transaction in client.transactions:
    transaction.calculate_total_transaction_amount()
    print(f'  {transaction.time_stamp} {transaction.no} Total amount: {transaction.total_amount}')

# adding items for each transaction
clients[0].transactions[0].add_item(Item('Eraser', 'ST10502', 0.90))
clients[0].transactions[0].add_item(Item('Tipex', 'ST10552', 1.80))
clients[1].transactions[0].add_item(Item('Wire', 'EL32321', 23.99))
clients[1].transactions[0].add_item(Item('Socket', 'EL00874', 9.09))
clients[2].transactions[0].add_item(Item('Chocolate', 'SW36550', 2.50))
clients[2].transactions[1].add_item(Item('Nuggat', 'SW00212', 2.99))
clients[2].transactions[1].add_item(Item('Sugar', 'SW0002', 1.49))

for client in clients:
  print(f'{client.name} has the following transactions: ')
  for transaction in client.transactions:
    transaction.calculate_total_transaction_amount()
    print(f'  {transaction.time_stamp} {transaction.no} Total amount: {transaction.total_amount}')
    for item in transaction.purchased_items:
      print(f'    {item.name} {item.serial_no} {item.price}')
