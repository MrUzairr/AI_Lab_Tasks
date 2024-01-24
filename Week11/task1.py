def read_last_two_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Extract the last two lines
            last_two_lines = lines[-2:]

            # Print or return the last two lines
            for line in last_two_lines:
                print(line.strip())

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = './task1.txt'
read_last_two_lines(file_path)
