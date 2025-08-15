#objectToString
#เเปลง obect เป็น String
#def__str__(self):
# rrturn "=ชุดข้อความ"

class Employee:
    # class variable
    minSalary = 12000
    maxSalary = 50000
    companyName = 'บริษัท PAOihavecpu จัดกัด'

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department

#เเสดงรายละเอียด
    def _showData(self):
        print('ชื่อพนักงาน = '+self.__name)
        print('เงินเดือน = '+str(self.__salary))
        print('แผนก = '+self.__department)

#รายได้ต่อปี
    def _getIncome(self):
        return self.__salary * 12

    def __str__(self):
        return ("ชื่อพนักงาน = {}, เเผนก = {},เ งินเดือน = {}, รายได้ต่อปี = {}".
                format(self.__name,self.__department,self.__salary,self._getIncome()))

class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'
    def __init__(self,name, salary):
        super().__init__(name,salary,self.__departmentName)



class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'
    def __init__(self,name, salary):
        super().__init__(name, salary, self.__departmentName)



class Sale(Employee):
    __departmentName = 'แผนกขาย'
    def __init__(self,name, salary):
        super().__init__(name, salary, self.__departmentName)


account = Accounting("เปา", 35000)
print(account.__str__())
programmer = Programmer("อังเปา",50000)
print(programmer.__str__())
sale = Sale("ปังเปา", 25000)
print(sale.__str__())


