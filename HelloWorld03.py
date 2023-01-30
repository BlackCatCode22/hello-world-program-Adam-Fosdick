# dH 1/24/23
# HelloWorld03.py
#
#
# Create a hello world program that asks the user for her name and then echos the name back with a greeting
#
# Reference: https://www.w3schools.com/python/python_user_input.asp
#
# Sample code:
user_name = input("Please enter you name: ")
print("\n\n Hello " + user_name + " how are you today?")


student_name = input("Please put in your name: ")
student_id = input("Please input student id: ")
student_age = input("Please tell me your age: ")
student_question = float(input("What is pie in decimal form: "))

print("\n\nHello " + student_name + "\nyour student Id:" + student_id)
print("you are " + student_age + " years old")
print("Pie Answer: " , end=' ')
print(student_question)
