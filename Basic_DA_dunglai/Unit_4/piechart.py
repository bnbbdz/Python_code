# read file
with open(r"D:\Hoc tap\Python + SQL + R\Python_dunglai\Unit_4\clean_data.csv", encoding="utf8") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]

total_student = len(students)

# split header
header = header.split(",")
subjects = header[5:]

# turn each student to a list
for i in range(len(students)):
	students[i] = students[i].split(",")

# remove empty list (end of file)
students.pop()

# number of students who took 0,1,2,3,... subjects
num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0]

for s in students:
	count = 0
	for i in range(11):
		if s[i+5] != "-1":
			count += 1

	num_of_exam_taken[count] += 1

print(num_of_exam_taken)

# Draw pie chart
# https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_features.html

import matplotlib.pyplot as plt
labels = "0 Môn", "1 Môn", "2 Môn", "3 Môn", "4 Môn", "5 Môn", "6 Môn", "7 Môn", "8 Môn", "9 Môn", "10 Môn", "11 Môn"
# sizes = [0, 80, 122, 2598, 4334, 318, 2730, 64261, 0, 0, 0, 1]
sizes = num_of_exam_taken

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.show()

# Draw online
# https://www.rapidtables.com/tools/pie-chart.html