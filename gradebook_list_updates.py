last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]


# Add computer science grade to gradebook
gradebook.append(["computer science", 100])

# Add visual arts grade to gradebook
gradebook.append(["visual arts", 93])

# Correct visual arts score in gradebook by adding 5
gradebook[-1][-1] = gradebook[-1][-1] + 5

# Remove poetry grade from gradebook
gradebook[2].remove(gradebook[2][-1])

# Add in 'Pass' as new poetry grade in gradebook
gradebook[2].append('Pass')

# Union gradebook to last_semester_gradebook
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)