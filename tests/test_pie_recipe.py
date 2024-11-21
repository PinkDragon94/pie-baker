import unittest
from pie_recipe import can_bake_pies

class TestPieRecipe(unittest.TestCase):
    def test_sufficient_ingredients(self):
        ingredients = {
            "sugar": 5, 
            "pumpkin_puree": 10, 
            "eggs": 12
        }
        self.assertEqual(can_bake_pies(4, ingredients), "You can bake the pies")

    def test_insufficient_ingredients(self):
        ingredients = {
            "sugar": 5, 
            "pumpkin_puree": 10, 
            "eggs": 6
        }
        expected_missing = {"eggs": 6}
        self.assertEqual(can_bake_pies(4, ingredients), expected_missing)

if __name__ == "__main__":
    unittest.main()