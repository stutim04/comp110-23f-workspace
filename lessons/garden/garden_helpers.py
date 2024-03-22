"""Some functions for my garden plan!"""


__author__ = "730669462"

# Function name: add_by_kind
# Parameters: dict[str, list[str]], str, str
# Return Type: None


def add_by_kind(plants_by_kind: dict[str, list[str]], plant_kind: str, plant: str) -> None:
    """Add by kind."""
    if plant_kind in plants_by_kind:
        plants_by_kind[plant_kind].append(plant)
    else:
        plants_by_kind[plant_kind] = []
        plants_by_kind[plant_kind].append(plant)


def add_by_date(plants_by_date: dict[str, list[str]], month: str, plant: str,) -> None:
    """Add by date."""
    if month in plants_by_date:
        plants_by_date[month].append(plant)
    else:
        plants_by_date[month] = []
        plants_by_date[month].append(plant)


# Function name: lookup_by_kind_and_date
# Parameters: dict[str, list[str]], dict[str, list[str]], str, str
# Return Type: str
        

def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], plant_kind: str, month: str) -> str:
    """Look up by kind and date."""
    assert plant_kind in plants_by_kind
    assert month in plants_by_date
    kind_list: list[str] = plants_by_kind[plants_by_kind]
    # Get a list of all plants planted ina specific month 
    month_list: list[str] = plants_by_date[month]
    combined_list: list[str] = []
    for plant in kind_list:
        for other_plant in month_list:
            if plant == other_plant: 
                combined_list.append(other_plant)
    if len(combined_list) > 0:
        return f"{plant_kind}s to plant in {month}: {combined_list}"
    else:
        return f"No {plant_kind}s to plant in {month}"