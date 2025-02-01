student_score = [90, 80, 70, 60, 50, 40, 30, 20, 10, 98, 97, 96, 95, 94, 93, 92, 91, 89, 88, 87, 86, 85, 84, 83, 82, 81, 79, 78, 77, 76, 75, 74, 73, 72, 71, 69, 68, 67, 66, 65, 64, 63, 62, 61, 59, 58, 57, 56, 55, 54, 53, 52, 51, 49, 48, 47, 46, 45, 44, 43, 42, 41, 39, 38, 37, 36, 35, 34, 33, 32, 31, 29, 28, 27, 26, 25, 24, 23, 22, 21, 19, 18, 17, 16, 15, 14, 13, 12, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]    

# total_score = sum(student_score)
# average_score = total_score / len(student_score)
# print("Total score: ", total_score)
# print("Average score: ", average_score)

# sum = 0
# for score in student_score:
#     sum += score
# print(sum)

# print(max(student_score))

# max_score = 0
# for score in student_score:
#     if score > max_score:
#         max_score = score
# print(max_score)

print(min(student_score))

min_score = 100
for score in student_score:
    if score < min_score:
        min_score = score
print(min_score)