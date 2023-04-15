# Continuation of inventory.py.
# Return a dictionary that repesents the updated inventory.


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(f'{v} {k}')        
    print(f'Total number of items: {item_total}')


def addToInventory(inventory, addedItems):
    for item in addedItems:
        # Gets value of `item` in dictionary `inventory`
        # If item does not exists, sets inventory item to 0, then adds 1
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)