Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: D:/ÍøÂç163-28/test/pythonÔª×é.py =================
>>> tup1 = ();
>>> tup1 = (50,);
>>> tup1 = ('physics','chemistry',1997,2000);
>>> tup2 = (1,2,3,4,5,6,7);
>>> print "tup1[0]:",tup1[0]
tup1[0]: physics
>>> print"tup2[1:5]:",tup2[1:5]
tup2[1:5]: (2, 3, 4, 5)
>>> tup1 = (12,34.56);
>>> tup2 = ('abc','xyz');
>>> tup3 = tup1 + tup2;
>>> print tup3;
(12, 34.56, 'abc', 'xyz')
>>> tup = ('physics','chemistry',1997,2000);
>>> print tup;
('physics', 'chemistry', 1997, 2000)
>>> del tup;
>>> print "After deleting tup:"
After deleting tup:
>>> print tup;

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print tup;
NameError: name 'tup' is not defined
>>> print 'abc',-4.24e93,18+6.6j,'xyz';
abc -4.24e+93 (18+6.6j) xyz
>>> x,y = 1,2;
>>> print "Value of x,y:¡°£¬x,y;
SyntaxError: EOL while scanning string literal
>>> print "Value of x,y:",x,y;
Value of x,y: 1 2

>>> tup1 = ("all")
>>> print tup1
all
>>> tup1 = ("all",)
>>> print tup1
('all',)
>>> 
