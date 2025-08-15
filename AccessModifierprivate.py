class Employee:
    def __init__(self, name, salary, department):
        # private attribute
        self._name = name
        self.__salary = salary
        self.__department = department

    # private method
    def _showData(self):
        print('ชื่อพนักงาน = {}'.format(self._name))
        print('เงินเดือน = {} '.format(self.__salary))
        print('แผนก = {} '.format(self.__department))

emp1 = Employee('กิตติธัช', 50000, 'HTD2')
emp1.__salary = 50001
emp1._showData()