

# Filename Cleaner (CLI Tool)
# Author: Moe
# Description: Cleans up a list of filenames by removing unwanted characters,
# replacing spaces with underscores, and converting to lowercase.

# Function to clean a single filename
def clean_filename(name):
    # Remove leading/trailing whitespace
    name = name.strip()
    # Replace spaces with underscores
    name = name.replace(" ", "_")
    # Convert to lowercase
    name = name.lower()
    return name

# Function to clean a list of filenames
def clean_all_filenames(filenames):
    cleaned = []
    for name in filenames:
        cleaned_name = clean_filename(name)
        cleaned.append(cleaned_name)
    return cleaned

# Main function to interact with the user
def main():
    print("Filename Cleaner")
    print("Enter filenames one by one. Type 'done' when finished.\n")

    original_filenames = []

    while True:
        user_input = input("Enter filename: ")
        if user_input.lower() == "done":
            break
        if user_input.strip() == "":
            print("Empty input ignored.")
            continue
        original_filenames.append(user_input)

    if not original_filenames:
        print("\nNo filenames entered.")
        return

    print("\nOriginal Filenames:")
    for name in original_filenames:
        print("-", name)

    cleaned_filenames = clean_all_filenames(original_filenames)

    print("\nCleaned Filenames:")
    for name in cleaned_filenames:
        print("-", name)

# Start the program
main()
