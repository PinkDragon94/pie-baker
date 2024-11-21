from utils import (
    calculate_total_required,
    get_available_ingredients,
    calculate_missing_ingredients,
)


def can_bake_pies(pies, ingredients):
    """
    Checks if sufficient ingredients are available to bake pies.

    Args:
        pies (int): Number of pies to bake.
        ingredients (dict): Available ingredients with quantities.

    Returns:
        str or dict: "You can bake the pies" if sufficient, otherwise a dictionary of missing ingredients.
    """

    recipe = {
        "sugar": 1, 
        "pumpkin_puree": 2, 
        "eggs": 3
    }

    total_required = calculate_total_required(recipe, pies)
    available = get_available_ingredients(ingredients)
    missing = calculate_missing_ingredients(total_required, available)

    if missing:
        return missing 
    return "You can bake the pies"