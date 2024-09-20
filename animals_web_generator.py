import json

# Specify the path to your JSON file (or use the correct path if not in the same directory)
file_path = 'animals_data.json'

def generate_html(animals_template, matching_animals):
    # Read the HTML template


    print(matching_animals)
    # Prepare the content part of the HTML
    output = ''  # define an empty string
    for animal_data in matching_animals:
        # append information to each string
        output += f"Name: {animal_data['name']}\n"
        output += f"Diet: {animal_data['characteristics']['diet']}\n"

    animals_template = animals_template.replace("__REPLACE_ANIMALS_INFO__", output)

    # Replace placeholders in the template


    # Write the final HTML content to a file
    with open("animals.html", "w") as file:
        file.write(animals_template)

    print("HTML file 'animals_template.html' has been updated.")

def main():
    # Load the JSON data
    with open(file_path, 'r') as json_file:
        animals_data = json.load(json_file)

    with open('animals_template.html', 'r') as html_file:
        animals_template = html_file.read()

    while True:
        # Prompt the user for the skin_type they want to search for
        user_input = input("Enter the skin type you want to search for (or 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            break

        # Initialize a list to store matching animals
        matching_animals = []

        # Iterate through the list of animals
        for animal in animals_data:
            # Get the skin_type for the current animal
            skin_type = animal.get("characteristics", {}).get("skin_type", "Unknown")

            # Check if the skin_type matches the user input
            if skin_type.lower() == user_input.lower():
                matching_animals.append(animal)

        # Print debug information
        print(f"User input: {user_input}")
        print(f"Matching animals: {matching_animals}")

        # Generate and save the HTML
        generate_html(animals_template, matching_animals)

if __name__ == "__main__":
    main()
