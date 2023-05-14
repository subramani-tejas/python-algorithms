import re


def sort_by_marks(student_list):
    marks = re.findall(r'(\d+)', student_list)
    return int(marks[0])


def solve(arr):
    arr.sort(key=sort_by_marks, reverse=True)
    # sorted(arr, key=sort_by_marks)
    return arr


nums = ["adarsh80", "harsh95", "shivam95", "tejas89"]
q = solve(nums)
print(q)
