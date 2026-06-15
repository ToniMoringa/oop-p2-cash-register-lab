#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        if not isinstance(discount, int) or discount < 0 or discount > 100:
            print("Not valid discount")
            discount = 0
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        cost = price * quantity
        self.total += cost
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            'item': item,
            'quantity': quantity,
            'total_cost': cost
        })

    def apply_discount(self):
       
        if self.discount > 0:
            self.total = self.total * (100 - self.discount) / 100
            if self.total.is_integer():
                total_display = int(self.total)
            else:
                total_display = f"{self.total:.2f}"
            
            print(f"After the discount, the total comes to ${total_display}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        
        if not self.previous_transactions:
            return
        last = self.previous_transactions.pop()
        self.total -= last['total_cost']
        for _ in range(last['quantity']):
            self.items.pop()

            