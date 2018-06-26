"""Print out all the melons in our inventory."""


# from melons import melon_names, melon_seedlessness, melon_prices

def make_melon_dict(filename):
    """Takes in a file and creates a dictionary of the melon data."""

    melon_dict = {}

    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            name, price, seedless, rind_color, flesh_color, weight = line.split("|")
            melon_dict[name] = {
                'price': float(price),
                'seedless': bool(seedless),
                'rind color': rind_color,
                'flesh color': flesh_color,
                'weight': float(weight),
                }

    return melon_dict


def print_melons(melon_dict):
    """Print each melon with corresponding attribute information."""

    for melon, attributes in melon_dict.items():
        print(f"""{melon.upper()}
        seedless: {melon_dict[melon]['seedless']}
        price: {melon_dict[melon]['price']}
        flesh color: {melon_dict[melon]['flesh color']}
        rind color: {melon_dict[melon]['rind color']}
        weight: {melon_dict[melon]['weight']}
        """)

all_the_melons = make_melon_dict('melons.txt')
print_melons(all_the_melons)
