# class Pet:
#     def __init__(self,name):
#         self.name = name
#
#     def talk(self):
#         print(f"{self.name} is talking")
#
# class Dog(Pet):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
#
#     def talk(self,type):
#         print(f"{self.name} is {self.age} years old,he is talking {type}")
#
#
# miao = Dog('miao',2)
# miao.talk('something')
#


# class FileUtiles:
#
#     def __init__(self,fileType,filename):
#         self.fileType = fileType
#         self.filename = filename
#
#     def file_handle(self):
#         print("File Handler")
#
# class CsvFileUtiles(FileUtiles):
#
#     def file_handle(self):
#         print('正在处理CSV')
#
#
# class ExcelFileUtiles(FileUtiles):
#
#     def file_handle(self):
#         print('正在处理EXCEL')
#
# class ParesFile:
#     def get_data_from_file(self,file:FileUtiles):
#         file.file_handle()
#
#
# f1 = ExcelFileUtiles('EXCEL','data.xlsx')
# p = ParesFile()
# p.get_data_from_file(f1)



