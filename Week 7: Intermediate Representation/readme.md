```
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


Test intermediate-rep2.py wwith the following test case:

    Input:
Enter assign and input:

Variable name: x
Left operand: a
Operator: +
Right operand: b
Enter if and input:

Left operand of condition: a
Comparison operator: >
Right operand of condition: b
Statements for the 'true' block: Enter assign with y = y + 1, then done
Choose yes for else block and enter assign with y = y - 1, then done
Enter while and input:

Left operand of condition: n
Comparison operator: >
Right operand of condition: 0
Statements for the while loop body: Enter assign with n = n - 1, then done
Enter call and input:

Function name: print
Arguments: x, y
Enter done to finish.

Expected Output:
t0 = a + b
x = t0
if a > b goto L0
goto L1
L0:
t1 = y + 1
y = t1
goto L2
L1:
t2 = y - 1
y = t2
L2:
L3:
if not n > 0 goto L4
t3 = n - 1
n = t3
goto L3
L4:
param x
param y
t4 = call print, 2


```
