"""
vending_machine.py

Execution Instructions:
    Run directly in the terminal to support interactive input prompts:
    $ python3 vending_machine.py
"""

class VendingMachine: # CLASS OBJECT: groups the data (inventory) with the operations allowed to touch it
    DEFAULT_INVENTORY = 20 # CLASS ATTRIBUTE: shared by every instance -- how a new machine knows to start at 20 unless told otherwise

    def __init__(self, initial_inventory=None, product_name="drink"):  # INSTANCE METHOD (constructor): default params let a caller skip arguments for the common case
        self.inventory = (  # INSTANCE ATTRIBUTE: unique to this one machine
            VendingMachine.DEFAULT_INVENTORY   # falls back to the shared class attribute when no starting stock is given
            if initial_inventory is None      # so VendingMachine() alone still gives a fully working 20-bottle machine
            else initial_inventory
        )
        # INSTANCE ATTRIBUTES
        self.product_name = product_name   # defaults to "drink"; matters later for the __str__ output
        self.total_purchased = 0           # not required by the assignment, but makes testing and reporting easier
        self.total_restocked = 0           # same for restocking; we can track how many bottles have been added to the machine over its lifetime but defaults to 0 at steady state

    def purchase(self, amount):  # INSTANCE METHOD, part of the public interface; self is bound automatically to the calling instance
        if amount < 0:
            raise ValueError("Cannot purchase a negative number of bottles.")   # a negative purchase doesn't mean anything, so reject it before touching state
        if not self._has_enough_stock(amount): # checks the internal helper before changing anything
            print(
                f"Purchase of {amount} bottle(s) declined -- "
                f"only {self.inventory} in stock." # not enough stock: report it, but the inventory is not touched
            )
            return False  # declined -- inventory left completely unchanged
        self.inventory -= amount  # INSTANCE ATTRIBUTE: only now, after both checks pass, does the stock actually decrease by the amount purchased
        self.total_purchased += amount  # INSTANCE ATTRIBUTE: stock conversely increases by the amount purchased
        return True  # neither purchase() nor restock() can leave the object inconsistent, since both validate before changing state

    def restock(self, amount):  # INSTANCE METHOD, mirror image of purchase(): always succeeds, no reason to reject adding bottles
        if amount < 0:
            raise ValueError("Cannot restock a negative number of bottles.")
        self.inventory += amount 
        self.total_restocked += amount
        return True  # neither purchase() nor restock() can leave the object inconsistent, since both validate before changing state

    def report_inventory(self):  # INSTANCE METHOD: prints the exact line the assignment checks
        print(f"Inventory: {self.inventory} bottles")

    def _has_enough_stock(self, amount):  # INSTANCE METHOD, internal helper -- leading underscore signals "not part of the public interface"
        return amount <= self.inventory  # never called directly by outside code; only purchase() calls this, so the method stays hidden

    def __str__(self):  # INSTANCE METHOD (special method): controls what print(machine) shows (zyBook 9.8): class customization
        return (
            f"VendingMachine({self.product_name}): {self.inventory} in stock, "   # by default, printing gives '<VendingMachine object at 0x...>' -- this replaces that
            f"{self.total_purchased} sold, {self.total_restocked} restocked"   # one-line summary built from four instance attributes
        )

    def __eq__(self, other): # INSTANCE METHOD (special method): controls what machine_a == machine_b means
        if not isinstance(other, VendingMachine):  # is "other" the right type to compare against at all? Are they both VMs...?
            return NotImplemented  # ...if not, say "can't compare these" instead of guessing
        return self.inventory == other.inventory  # self = machine on the left of ==, other = machine on the right, compared by current inventory


def main():  # not indented under the class -- sits OUTSIDE VendingMachine; it uses the class, it isn't part of it
    purchase_amount_1 = int(input("Enter amount to purchase: "))  # three input() calls, one integer per line
    restock_amount = int(input("Enter amount to restock: "))
    purchase_amount_2 = int(input("Enter amount to purchase again: "))

    machine = VendingMachine()  # CLASS OBJECT is called for the machine INSTANCE OBJECT to be created, starting at 20 (no arguments given)
    machine.purchase(purchase_amount_1)
    machine.restock(restock_amount)
    machine.purchase(purchase_amount_2)  # stock carries through instead of resetting to 20
    machine.report_inventory()  # the graded line: "Inventory: {self.inventory} bottles"; everything above is internal bookkeeping

# We only runs main() when this file is executed directly (e.g. "python3 vending_machine.py").
# If another file imports VendingMachine class instead (like test_vending_machine.py does),
# __name__ is not "__main__" here, so main() is skipped and input() is never triggered.
if __name__ == "__main__":
    main()

    
