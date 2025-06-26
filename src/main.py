"""
Test script

Take a store and calculate a potential profits (sum of values of items - expenses)
Save value to .txt file.

Try test driven development here
"""

from classes.Store import Store
from classes.Item import Item

def main() -> None:
    items1: list[Item] = [
            Item(1, "Dvd player", 39.99),
            Item(2, "Record player", 120.00),
            Item(3, "Video game console", 99.99)
    ]

    items2: list[Item] = [
            Item(4, "Dvd player", 39.99),
            Item(5, "Jacket", 50.00),
            Item(6, "Jeans", 10.00),
            Item(7, "book", 5.99)
    ]
    store1: Store = Store(1, "Joe's Store", items1, expenses=83.12)
    store2: Store = Store(2, "Bob's Store", items2, expenses=62.78)

    stores: list[Store] = [store1, store2]
    get_total_profit(stores)


def get_total_profit(stores: list[Store]) -> None:
    total_profit: float = 0
    for store in stores:
        profit: float = store.profit()
        print(f"Store #{store.store_num} profits: {profit}")
        total_profit += profit
    print(f"The total profit for all stores is: {total_profit}")
    





if __name__ == "__main__":
    main()
