def calculate_total_required(ingredients, pies):
    """
    Calculate total required ingredients for baking pies.

    Args:
        ingredients (dict): Ingredients with quantities per pie.
        pies (int): Number of pies.

    Returns:
        dict: Total required ingredients.
    """
    total_required = {}
    for item, required in ingredients.items():
        total_required[item] = pies * required
    return total_required


def get_available_ingredients(ingredients):
    """
    Get available ingredients from the input dictionary.

    Args:
        ingredients (dict): Available ingredients with quantities.

    Returns:
        dict: Available ingredients.
    """
    available = {}
    for item, quantity in ingredients.items():
        available[item] = quantity
    return available


def calculate_missing_ingredients(required, available):
    """
    Calculate missing ingredients.

    Args:
        required (dict): Required ingredients.
        available (dict): Available ingredients.

    Returns:
        dict: Missing ingredients.
    """
    missing = {}
    for item, required_quantity in required.items():
        available_quantity = available.get(item, 0)
        if available_quantity < required_quantity:
            missing[item] = required_quantity - available_quantity
    return missing