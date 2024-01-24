import matplotlib.pyplot as plt

# Data
courses = ['PF', 'DL', 'CV']
y_pos = [2, 0, 1]
scores = [70, 60, 40]

# Create bar graph
plt.bar(y_pos, scores, align='center', alpha=0.7)
plt.xticks(y_pos, courses)
plt.ylabel('Scores')
plt.title('Scores in Different Courses')
plt.show()
