Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="""raju
how are you
and then
we are making some random testing"""
>>> b=list(a)
>>> b
['r', 'a', 'j', 'u', '\n', 'h', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '\n', 'a', 'n', 'd', ' ', 't', 'h', 'e', 'n', '\n', 'w', 'e', ' ', 'a', 'r', 'e', ' ', 'm', 'a', 'k', 'i', 'n', 'g', ' ', 's', 'o', 'm', 'e', ' ', 'r', 'a', 'n', 'd', 'o', 'm', ' ', 't', 'e', 's', 't', 'i', 'n', 'g']
>>> b=a.split('  ')
>>> b
['raju\nhow are you\nand then\nwe are making some random testing']
>>> c=b.replace(\n,',')
SyntaxError: unexpected character after line continuation character
>>> c=''.join(b)
>>> c
'raju\nhow are you\nand then\nwe are making some random testing'
>>> d=c.replace('\n',',')
>>> d
'raju,how are you,and then,we are making some random testing'
>>> d1=list(d)
>>> d1
['r', 'a', 'j', 'u', ',', 'h', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', ',', 'a', 'n', 'd', ' ', 't', 'h', 'e', 'n', ',', 'w', 'e', ' ', 'a', 'r', 'e', ' ', 'm', 'a', 'k', 'i', 'n', 'g', ' ', 's', 'o', 'm', 'e', ' ', 'r', 'a', 'n', 'd', 'o', 'm', ' ', 't', 'e', 's', 't', 'i', 'n', 'g']
>>> d1=d.split(',')
>>> d1
['raju', 'how are you', 'and then', 'we are making some random testing']
>>> for kd in d1:
	x=kd+' super'
print(x)
SyntaxError: invalid syntax
>>> for kd in d1:
	x=kd+' super'
	print(x)

	
raju super
how are you super
and then super
we are making some random testing super
>>> x
'we are making some random testing super'
>>> z=[]
>>> for kd in d1:
	x=kd+' super'
	z.append(x)
	print(z)

	
['raju super']
['raju super', 'how are you super']
['raju super', 'how are you super', 'and then super']
['raju super', 'how are you super', 'and then super', 'we are making some random testing super']
>>> q=''
>>> for w in z:
	q+=w
	print(q)

	
raju super
raju superhow are you super
raju superhow are you superand then super
raju superhow are you superand then superwe are making some random testing super
>>> len(q)
80
>>> 