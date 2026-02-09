import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_html(file_path):
    """Loads an HTML file"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def iterates_data(data, template):
    output = ""

    for animal_data in data:
        output += f"Name: {animal_data.get('name', 'Unknown')}\n"
        output += f"Diet: {animal_data.get('characteristics', {}).get('diet', 'Unknown')}\n"
        output += f"Location: {animal_data.get('locations', ['Unknown'])[0]}\n"
        output += f"Type: {animal_data.get('characteristics', {}).get('type', 'Unknown')}\n\n"

    new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(new_html)


animals_data = load_data("animals_data.json")
template = load_html("animals_template.html")
iterates_data(animals_data, template)
