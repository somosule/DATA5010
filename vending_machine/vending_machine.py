class VendingMachine:
    DEFAULT_INVENTORY = 20

    def __init__(self, initial_inventory=None, product_name="drink"):
        self.inventory = (
            VendingMachine.DEFAULT_INVENTORY
            if initial_inventory is None
            else initial_inventory
        )
        self.product_name = product_name
        self.total_purchased = 0
        self.total_restocked = 0

    def purchase(self, amount):
        if amount < 0:
            raise ValueError("Cannot purchase a negative number of bottles.")
        if not self._has_enough_stock(amount):
            print(
                f"Purchase of {amount} bottle(s) declined -- "
                f"only {self.inventory} in stock."
            )
            return False
        self.inventory -= amount
        self.total_purchased += amount
        return True

    def restock(self, amount):
        if amount < 0:
            raise ValueError("Cannot restock a negative number of bottles.")
        self.inventory += amount
        self.total_restocked += amount
        return True

    def report_inventory(self):
        print(f"Inventory: {self.inventory} bottles")

    def _has_enough_stock(self, amount):
        return amount <= self.inventory

    def __str__(self):
        return (
            f"VendingMachine({self.product_name}): {self.inventory} in stock, "
            f"{self.total_purchased} sold, {self.total_restocked} restocked"
        )

    def __eq__(self, other):
        if not isinstance(other, VendingMachine):
            return NotImplemented
        return self.inventory == other.inventory


def main():
    purchase_amount_1 = int(input("Enter amount to purchase: "))
    restock_amount = int(input("Enter amount to restock: "))
    purchase_amount_2 = int(input("Enter amount to purchase again: "))

    machine = VendingMachine()
    machine.purchase(purchase_amount_1)
    machine.restock(restock_amount)
    machine.purchase(purchase_amount_2)
    machine.report_inventory()


if __name__ == "__main__":
    main()

    