class Personal:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.salary = 0
        self.work_time = 0
        self.productivity = 0 

    def calculate_productivity(self):
        return f'Процент продуктивности: {self.work_time * 100 / 40}'

    def func(self, *args):
        return args


class Manager(Personal):

    def __init__(self, name, salary, work_time, id):
        self.name = name
        self.salary = salary
        self.work_time = work_time
        self.id = id
        self.productivity = work_time * 100 / 40

    def func(self):
        print(f'имя - {self.name}\nзаработная плата - {self.salary}\nперсональный номер - {self.id}')

class Secretary(Personal):
    def __init__(self, name, salary, work_time, id):
        self.name = name
        self.salary = salary
        self.work_time = work_time 
        self.id = id
        self.productivity = work_time * 100 / 40

    def func(self):
        print(f'имя - {self.name}\nзаработная плата - {self.salary}\nперсональный номер - {self.id}')

class Seller(Personal):
    def __init__(self, name, salary, sold, id, work_time):
        self.name = name
        self.id = id
        self.salary = salary + work_time * 50
        self.sold = sold
        self.work_time = work_time * 100 / 40

    def func(self):
        print(f'имя - {self.name}\nперсональный номер - {self.id}\nзаработная плата - {self.salary}')
        
class Employee(Personal):
    def __init__(self, name, work_time, id):
        self.name = name
        self.work_time = work_time
        self.id = id
        self.salary = work_time * 100
        self.productivity = work_time * 100 / 40

    def func(self):
        print(f'имя -  {self.name}\nПерсональные номера - {self.id}\nзаработная плата - {self.salary}')
    


class Employee2(Personal):
    def __init__(self, name, work_time, id):
        self.name = name
        self.work_time = work_time
        self.id = id
        self.salary = work_time * 100
        self.productivity = work_time * 100 / 40

    def func(self):
        print(f'имя -  {self.name}\nПерсональные номера - {self.id}\nЗаработная плата: {self.salary}')

class Replacement_secretary(Personal):
    def __init__(self, name, work_time, id):
        self.name = name
        self.work_time = work_time
        self.id = id
        self.salary = work_time * 100
        self.productivity = work_time * 100 / 40

    def func(self):
        print(f'имя - {self.name}\nПерсональный номер - {self.id}\nЗаработная плата: {self.salary}')


a = Manager("Barsbek Kanakulov", 45000, 18, 1)
print(Manager.func())
print(Secretary.calculate_productivity())
print()


b = Secretary("Alymkul Tilekbaev", 20000, 38, 2)
print(Secretary.func())
print(Secretary.calculate_productivity())
print()

c = Seller("Aiperi Shalymbekova", 20000, 20, 3, 38)
print(Seller.func())
print(Seller.calculate_productivity())
print()

d = Employee("Bakyt Rustamov", 25, 4)
print(Employee.func())
print(Employee.calculate_productivity())
print()

e = Employee2("Altynai Shirinbaeva", 40, 5 )
print(Employee2.func())
print(Employee2.calculate_productivity())
print()

f = Replacement_secretary("Zhanar Ryskulov", 33, 6)
print(Replacement_secretary.func())
print(Replacement_secretary.calculate_productivity())
print()


amount = 0
lst = [a, b, c, d, e, f]
for i in lst:
    amount += i.salary
print(f'Общая сумма: {amount}')

lst2 = [i.productivity for i in lst]
the_most_productive = {}
the_most_unproductive = {}
for i in lst:
    if max(lst2) == i.productivity:
        the_most_productive[i.name] = i.productivity
    elif min(lst2) == i.productivity:
        the_most_unproductive[i.name] = i.productivity
print(f'Самый продуктивный: {the_most_productive}')
print(f'Самый непродуктивный: {the_most_unproductive}')