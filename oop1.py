# ชื่อ .เงินเดือน
class Employee: # การสร้าง class
   # สร้าง method
   def detail(self, name, salary , department):
    #สร้าง Attribute
    self.name = name
    self.salary = salary
    self.department= department
   def showData(self):
    print('ชื่อพนักงาน = {}'.format(self.name))
    print('เงินเดือน = {} '.format(self.salary))
    print('แผนก = {} '.format(self.department))

# Attibutte เป้นกลไกรที่กำหนดคุณสมบัติไห้กับ  class
# การสร้าง Attribute
 # self.name = ชื่อพนังงาน
 # self.salary = เงินเดือน
 # self .age = อายุของพนักงาน

 #์ Methood เป็นกลไกที่กำหนดพฤติกกรมไห้กับ  class
 # การสร้าง Method
 #   def getName (self):
 #    rtturn self.name
 # การเรียกใช้งาน
 #  ชื่อวัตถุ.getName()


 #คีย์เวิร์ด self
 #การใช้คีย์เวิร์ด self จะเป็นตัวชี้หรือบงบอกว่าตอนนี้เราทำงารกับวัตถุใด
 # ให้บอกตัวตนของวัตถุนั้นๆ   เช่น การกำหนดคุณสมบัติต่างๆในวัตถุ เป็นต้น
 #constructor
 # method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ(ไม่ระบุก็ได้
 #โครงสร้าง constructor
# def __init__(self):

#การสร้างวัตถุ

emp1 = Employee()
emp1.detail('กิตติธัช',50000,'HTD2')
emp1.showData()

emp2 = Employee()
emp2.detail('เเก้วชัยสุญ',60000, 'HTD2')
emp2.showData()

emp3 = Employee()
emp3.detail('Kittithat',9000000, 'HTD2')
emp3.showData()

