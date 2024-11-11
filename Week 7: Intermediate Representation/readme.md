When you run intermediate-rep.py , you would get output like:

TAC for expression 'x = a + b * c':
t0 = b * c
t1 = a + t0
x = t1

TAC for if-else statement:
if a > b goto L0
goto L1
L0:
t2 = x + 1
x = t2
goto L2
L1:
t3 = x - 1
x = t3
L2:

TAC for method call 'result = add(a, b)':
param a
param b
t4 = call add, 2
result = t4


This is because we have put our test cases in the code at the function call. This explains the concept of Third-Address Code(TAC)
