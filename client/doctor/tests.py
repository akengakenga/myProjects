from django.test import TestCase

# Create your tests here.
a = {'bbb':456,'aaa':123,'ccc':789}
list = sorted(a.items(),key= lambda x:x[0])
print(list)