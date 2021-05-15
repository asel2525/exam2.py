#задание 1

def country (name, **kwargs):
    print(name, kwargs)
country(name = "USA", population = "330 million", is_democratic = True)

#задание 2

s = ("Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colorful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next program in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colorless. But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money.")
num = 0
for i in s:
    if i == "t" and i == "s":
        num += 1
print("количество букв s = ", s.count("t"))
print("количество букв t = ", s.count("s"))

def adverts():
    lst_of_words = s.split()
    for i in lst_of_words:
        if 'advert' in i:
            print(i.upper())
adverts()

#задание 4
import unittest
from task_4 import func


class TesterClass(unittest.TestCase):
	def test_arguments(self):
		result = func(5, 1, 7)
		self.assertEqual(result, 13)

	def test_diff_arguments(self):
		result = func(1, 'two', 3, 'four', 5)
		self.assertEqual(result, 9)

	def test_diff_arguments_2(self):
		input_data = [(5, 3, 1), 5.7, 'thirteen', 10, {1: 10}]
		result = func(*input_data)
		self.assertEqual(result, 15.7)

#задание 3
students = [
    {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Agness', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Don', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'},
    {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Alexey', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Mikel', 'age': 24, 'course': 'python', 'gender': 'Male'},
    {'name': 'Susanne', 'age': 25, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Stevie', 'age': 26, 'course': 'python', 'gender': 'Male'},
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aktanbek', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'},
    {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
]


ptn_names = []
for i in ptn_names:
    for j in i.values():
        if j == 'python':
            ptn_names.append(i.get('name'))
 
java_names = []
for i in java_names:
    for j in i.values():
        if j == 'java':
            java_names.append(i.get('name'))

js_names = []
for i in js_names:
    for j in i.values():
        if j == 'javascript':
            js_names.append(i.get('name'))

courses = {
    'python': ptn_names,
    'java': java_names,
    'javascript': js_names
}
print(courses)

#2

names = []
age = []
for i in students:
    for j in i.values():
        names.append(i.get('name'))
        ages.append(i.get('age'))
        names_ages = dict(zip(names, ages))

print(names_ages)