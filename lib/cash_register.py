#!/usr/bin/env python3

class CashRegister:
  def __init__(self):
    self.items = []
    self.total = 0.0

  def add_item(self, title, price, quantity=1):
    for _ in range(quantity):
      self.items.append(title)
      self.total += price

  def apply_discount(self, discount_percentage):
    discount_amount = self.total * (discount_percentage / 100)
    self.total -= discount_amount

  def void_last_transaction(self):
    if len(self.items) > 0:
      last_item_price = self.total - self.items.pop()
      self.total -= last_item_price
    else:
      print("No items to void.")
