import numpy as np

# Create a dictionary for Ali with course names as keys and total/obtained marks as values
ali_marks = {
    'Math': {'total': 100, 'obtained': 90},
    'Physics': {'total': 100, 'obtained': 85},
    'Chemistry': {'total': 100, 'obtained': 92},
    'English': {'total': 100, 'obtained': 88},
}

# Save the dictionary to a text file
text_file_path = 'ali_marks.txt'
with open(text_file_path, 'w') as text_file:
    for course, marks in ali_marks.items():
        text_file.write(f"{course}: Total - {marks['total']}, Obtained - {marks['obtained']}\n")

# Save the dictionary to a NumPy file
numpy_file_path = 'ali_marks.npy'
np.save(numpy_file_path, ali_marks)

print(f"Dictionary saved to text file: {text_file_path}")
print(f"Dictionary saved to NumPy file: {numpy_file_path}")
