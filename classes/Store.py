from Item import Item

class Store:
    def __init__(self, store_num: int, name: str, inventory: list[Item], expenses: float): 
        self.store_num: int = store_num
        self.name: str = name  
        self.expenses: float = expenses
        self.inventory: list[Item] = inventory