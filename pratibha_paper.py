#@###2nd
# symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|',':',';','"','<',',','>','.','?','/']
# num=['1','2','3','4','5','6','7','8','9','0']
# paragraph="My Name is Pratibha Tiwari . I AM 22 Years Old ! , Currently Studying in 'VIT' "
# New_par=[]
# for i in range(len(paragraph)):
#     if paragraph[i] in symbols:
        
#         New_par.append('3')
#     elif paragraph[i] in num:
#         New_par.append('2')
#     elif paragraph[i]==' ':
#         New_par.append(' ')
#     else:
#         New_par.append('1')
# a=''.join(New_par)
# print(a)


##3rd
# import sys
# lis=[11,2.0,[],(),' ']
# for i in range(len(lis)):
#     print(f"Type of {lis[i]} is {type(lis[i])}")
#     print(f"size of {lis[i]} is {sys.getsizeof(lis[i])}")
#     print(f"Memory Location of {lis[i]} is {id(lis[i])}")
#     print()

#4th
# import random as r
# xx=0
# yy=0
# for i in range(1,101):
#     x=r.randint(1,100)
#     y=r.randint(1,100)
#     if x==y:
#         print(1)
#         xx+=1
#     else:
#         print(0)
#         yy+=1
# print("Total Occurrences of 1 is -:",xx)
# print("Total Occurrences of 0 is -:",yy)

#1st-:
# string='I JAI KIT'
# print("Total Length is-:",len(string))
# a=string[len(string)//2]
# print('Median Character of String is-:',a)
# aa=0
# bb=0
# for i in range(len(string)//2):
#     aa+=ord(string[i])
#     print(bb)
#     bb+=ord(string[1+i+len(string)//2])
#     print(bb)
# print("Total Value of strings before median is-:",aa)

# print("Total Value of strings after median is-:",bb)
# print('max is',max(aa,bb))



##5th
# class XYZ:
#     def __init__(self) -> None:
        
#         self.books=0

# class Amazon(XYZ):
    
#     def __init__(self,books) -> None:
#         super().__init__()
#         self.books=books
#         self.discount=10
#     def total_discount(self):
#         self.book=self.books-self.discount
#         return self.book
# class Flipkart(XYZ):
    
#     def __init__(self,books) -> None:
#         super().__init__()
#         self.books=books
#         self.discount=15
#     def total_discount(self):
#         self.book=self.books-self.discount
#         return self.book

# class Myntra(XYZ):
    
#     def __init__(self,books) -> None:
#         super().__init__()
#         self.books=books
#         self.discount=20
#     def total_discount(self):
#         self.book=self.books-self.discount
#         return self.book

# book_value=45
# rvc=Amazon(book_value)
# print("Book discount on Amazon is rupees-:",rvc.total_discount())
# rrr=Myntra(book_value)
# print("Book discount on Myntra is rupees-:",rrr.total_discount())

