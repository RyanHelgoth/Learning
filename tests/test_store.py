
from classes.Item import Item 
from classes.Store import Store
from pytest_mock import MockFixture




import pytest

class TestStore:
    items: list[Item] = [
            Item(1, "Shoes", 30.0),
            Item(2, "Computer", 199.99),
            Item(3, "Jeans", 14.99)
        ]
    store: Store = Store(1, "Joe's Store", items, expenses=57.23)


    def test_inventory_value(self) -> None:
        assert pytest.approx(self.store.inventory_value()) == 244.98


    def test_profits(self, mocker: MockFixture) -> None:
        mocker.patch("classes.Store.Store.inventory_value", return_value=244.98)
        assert pytest.approx(self.store.profit()) == 187.75