from pie_recipe import can_bake_pies

def main():
    available_ingredients = {
        "sugar": 5, 
        "pumpkin_puree": 10, 
        "eggs": 6
    }

    result = can_bake_pies(4, available_ingredients)

    if isinstance(result, dict):
        print("Missing ingredients:")
        for item, amount in result.items():
            print(f"{item}: {amount}")
    else:
        print(result)

if __name__ == "__main__":
    main()