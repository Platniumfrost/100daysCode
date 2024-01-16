import os

# Get the directory of the current script
current_directory = os.path.dirname(__file__)

# Relative paths to input and output directories
input_directory = os.path.join(current_directory, "input")
output_directory = os.path.join(current_directory, "output/ReadyToSend")

# Full path to invited_names.txt
file_path_invited_names = os.path.join(input_directory, "names/invited_names.txt")

# Full path to starting_letter.txt
file_path_starting_letter = os.path.join(input_directory, "letters/starting_letter.txt")

# Read names from invited_names.txt
with open(file_path_invited_names) as names_file:
    names = names_file.readlines()

# Read the content of the starting letter
with open(file_path_starting_letter) as letter_file:
    letter_contents = letter_file.read()

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Generate letters for each name and save in the output directory
for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace("[name]", stripped_name)
    with open(os.path.join(output_directory, f"letter_for_{stripped_name}.txt"), mode="w") as completed_letter:
        completed_letter.write(new_letter)
