def arithmetic (first, second, operation):
    if operation == '*':
        print(first*second)
    elif operation == '/':
        print(first/second)
    elif operation == '+':
        print(first+second)
    elif operation == '-':
        print(first-second)
    else:
        print('Неизвестная операция')
print ('Введите простой математический пример: ')
s=input()
l=len(s)
i=0
first_s=''
while '0'<=s[i]<='9':
    first_s+=s[i]
    i+=1
operation_s=s[i]
j=i
i+=1
second_s=''
while j<=len(s):
    second_s+=s[j]
    j+=1
arithmetic(int(first_s),int(second_s),operation_s)