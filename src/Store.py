from Item import Item

class Store:
    def __init__(self, store_num: int, name: str, inventory: list[Item], expenses: float) -> None: 
        self.store_num: int = store_num
        self.name: str = name  
        self.expenses: float = expenses
        self.inventory: list[Item] = inventory

    def inventory_value(self) -> float:
        item: Item
        total_value: float = 0
        for item in self.inventory:
            total_value += item.value

        return total_value
    

    def profit(self) -> float:
        return self.inventory_value() - self.expenses
