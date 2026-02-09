import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_html(file_path):
    """Loads an HTML file"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def serialize_animal(animal_obj):
    """Serializes a single animal object into an HTML list item."""
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj.get("name", "Unknown")}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'    <strong>Diet:</strong> {animal_obj.get("characteristics", {}).get("diet", "Unknown")}<br/>\n'
    output += f'    <strong>Location:</strong> {", ".join(animal_obj.get("locations", ["Unknown"]))}<br/>\n'
    output += f'    <strong>Type:</strong> {animal_obj.get("characteristics", {}).get("type", "Unknown")}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output


def iterates_data(data, template):
    """Generates the full HTML page with all animals."""
    output = ""
    for animal_data in data:
        output += serialize_animal(animal_data)

    new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(new_html)


animals_data = load_data("animals_data.json")
template = load_html("animals_template.html")
iterates_data(animals_data, template)