# Write a Python Program to count unique values inside a list

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()

        with open(destination_file, 'w') as destination:
            destination.write(content)

        print(f"Contents copied from {source_file} to {destination_file} successfully.")
    except FileNotFoundError:
        print("File not found. Please check the file paths.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
copy_file('source.txt', 'destination.txt')
