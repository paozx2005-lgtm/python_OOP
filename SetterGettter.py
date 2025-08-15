#Getter / Setter method
#Setter การกำหนดค่าไห้ object

#Getter การดึงค่าจาก object
# Ex_Setter
    #def setName(self, newname):
    #  Self.__name = newname
#Ex_Getter
    #def getName(self):
    #  return self.__name

class Employee:
    def __init__(self, name, salary, department):
        # private attribute
        self.__name = name
        self.__salary = salary
        self.__department = department

    # private method
    def _showData(self):
        print('ชื่อพนักงาน = {}'+self.getName())
        print('เงินเดือน = {} '+self.getSalary())
        print('แผนก = {} '+self.getDepartment())

     # Setter method
    def setName(self, newname):
         self.__name = newname
    def setSalary(self, newsalary):
        self.__salary = newsalary
    def setDepartment(self, newdepartment):
        self.__department = newdepartment

#getter method
    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department

emp1 = Employee('กิตติธัช', 50000, 'HTD2')
print('พนักงานดีเด่นประจำปี = {}'.format(emp1.getName()))
print('เงินเดือน = {}'.format(emp1.getSalary()))
print('แผนก = {}'.format(emp1.getDepartment()))
