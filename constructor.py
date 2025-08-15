#constructor
#เป็น Method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบุก็ได้)
#โครงสร้าง Constructur
#def __init__(self):
#    Pass

#destrustor
#เป็น Method พิเศษตรงข้ามกัน Constructor จะถูกใช้งานเมื่อ
#สิ้นสุดการทำงานของ Class หรือถูกทำก่อนจะสลาย object
#ส่วนใหญ่จะเป็นกลุ่มคำสั่งที่ทำหน้าที่คือหน่วยความจำไห้ระบบ(ไม่ระบุก็ได้)
#โครงสร้าง
#def __del__(self):
#  pass


class Employee:
        def __init__(self, name, salary, department):
            self.name = name
            self.salary = salary
            self.department = department

        def showData(self):
            print('ชื่อพนักงาน = {}'.format(self.name))
            print('เงินเดือน = {} '.format(self.salary))
            print('แผนก = {} '.format(self.department))

          #มีหรือไม่ก็ได้ destructor
        def __dir__(self):
            print('call destructor')

emp1 = Employee('กิตติธัช', 50000, 'HTD2')
emp1.showData()

emp2 = Employee('เเก้วชัยสุญ', 60000, 'HTD2')
emp2.showData()

emp3 = Employee('Kittithat', 9000000, 'HTD2')
emp3.showData()

emp4 = Employee('PAO', 80000,'HR')
emp4.salary = 81000
emp4.showData()