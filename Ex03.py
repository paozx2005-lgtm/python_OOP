# เขียนโปรแกรมสร้าง class ชื่อ Human โดยมี attribute และ Method ดังนี้
# attribute
# name เป็นชื่อบุคคล
# age เป็นอายุของบุคคล
# method
# aging(year) รับ parameter 1 ตัว คือ year
# - แสดงอายุปัจจุบัน
# - เพิ่มอายุขึ้นเท่ากับ year
# - แสดงอายุหลักหลังเพิ่มแล้ว

# เขียนโปรแกรมสร้าง class ชื่อ Human โดยมี attribute และ Method ดังนี้
# attribute
# name เป็นชื่อบุคคล
# age เป็นอายุของบุคคล
# method
# aging(year) รับ parameter 1 ตัว คือ year
# - แสดงอายุปัจจุบัน
# - เพิ่มอายุขึ้นเท่ากับ year
# - แสดงอายุหลักหลังเพิ่มแล้ว

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def aging(self, year):
        print(f"ชื่อ {self.name},อายุปัจจุบัน{self.age}")
        self.age += year
        print(f"ถ้าอายุเพิ่ม{year}ปี,จะอายุ{self.age}")

pao = Human('Kittithat', 19)
pao.aging(5)