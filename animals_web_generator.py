import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def iterates_data(data):
    output = ""

    for animal_data in data:
        output += f'Name: {animal_data.get("name", "Unknown")}\n'

        output += f'Diet: {animal_data.get("characteristics", {}).get("diet", "Unknown")}\n'

        output += f'Location: {animal_data.get("locations", ["Unknown"])[0]}\n'

        output += f'Type: {animal_data.get("characteristics", {}).get("type", "Unknown")}\n\n'

    print(output)


animals_data = load_data('animals_data.json')
iterates_data(animals_data)
