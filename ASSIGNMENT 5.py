"""
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message     

"""
student_marks = {
    "Ayush Chauhan": 85,
    "Divya Prakash": 92,
    "Nishant Gautam": 78,
    "Soni": 88,
    "Tushar Mishra": 81,
    "Amar Kumar": 95,
    "Geetika Sakuria": 76,
    "Das Ajay": 83,
    "Bharat Kumar": 89,
    "Smarty Tufchi": 90,
    "Anupriya Nisha Ekka": 87,
    "Upendra Kumar": 80
}

user_input = input("Enter your name: ").title().strip()
if user_input in student_marks:
    marks = student_marks.get(user_input)
    print(marks)

else:
    print("not found")


'''
Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

lists = [1,2,3,4,5,6,7,8,9,10]
print(f"Original list: {lists}")
slice_list = lists[0:5]
print(f"Extracts the first five elements: {slice_list}")
slice_list.reverse()
print(f"Reverses these extracted elements: {slice_list}")