# คือ ระดับในการเข้าถึง class attribute method และอื่นๆ ในภาษาเชิงวัตถุ
# โดยมีประโยชน์อย่างมากในเรื่องของการกำหนดระดับการเข้าถึง
# สิทธิในการเข้าใช้งาน การซ้อนข้อมูลและอื่นๆ

# Public คือการประกาสระดับการเข้าถึงที่เข้มงวดน้อยที่สุด หรือกล่าวได้ว่าใครๆ ก็สามารถเข้าถึงและเรียกใช้งานได้

# Protectted(_) เป็นการประกาศระดับการเข้าถึงเฉพาะคลาสของตัวมันเองและคลาสลูกที่สืบทอดคุณสมบัติไปใช้เท่านั้น

# Private(_) เป็นการประกาศระดับการเข้าถึงที่เข้มงวดที่สุด กล่าวคือ จะมีแต่คลาสของตัวมันเองเท่านั้นที่มีสิทธิ์ใช้งานได้

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

#public method
    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {} '.format(self.salary))
        print('แผนก = {} '.format(self.department))



emp1 = Employee('กิตติธัช', 50000, 'HTD2')
emp1.salary = 41000
emp1.showData()