import unittest
from utils import (
    calculate_total_required,
    get_available_ingredients,
    calculate_missing_ingredients,
)


class TestUtils(unittest.TestCase):
    def test_calculate_total_required(self):
        ingredients = {"sugar": 1, "pumpkin_puree": 2, "eggs": 3}
        pies = 4
        expected = {"sugar": 4, "pumpkin_puree": 8, "eggs": 12}
        self.assertEqual(calculate_total_required(ingredients, pies), expected)

    def test_get_available_ingredients(self):
        ingredients = {"sugar": 5, "pumpkin_puree": 10, "eggs": 6}
        expected = {"sugar": 5, "pumpkin_puree": 10, "eggs": 6}
        self.assertEqual(get_available_ingredients(ingredients), expected)

    def test_calculate_missing_ingredients(self):
        required = {"sugar": 4, "pumpkin_puree": 8, "eggs": 12}
        available = {"sugar": 5, "pumpkin_puree": 6, "eggs": 6}
        expected = {"pumpkin_puree": 2, "eggs": 6}
        self.assertEqual(calculate_missing_ingredients(required, available), expected)


if __name__ == "__main__":
    unittest.main()