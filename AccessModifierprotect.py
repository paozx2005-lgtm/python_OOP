class Employee:
    def __init__(self, name, salary, department):
        # protected attribute
        self._name = name
        self._salary = salary
        self._department = department

    # protected method
    def _showData(self):
        print('ชื่อพนักงาน = {}'.format(self._name))
        print('เงินเดือน = {} '.format(self._salary))
        print('แผนก = {} '.format(self._department))

emp1 = Employee('กิตติธัช', 50000, 'HTD2')
emp1._salary = 50001
emp1._showData()