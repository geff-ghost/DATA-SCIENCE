import os

print(os.getcwd())

os.makedirs('./data', exist_ok=True)

print(os.listdir('.'))

print('data' in os.listdir('.'))

print(os.listdir('./data'))

print()
file1 = open('./data/loans1.txt', 'r')
file1_content = file1.read()
print(file1_content)
file1.close()

with open('./data/loans2.txt', 'r') as file2:
    file2_content = file2.read()
    print(file2_content)

with open('./data/loans3.txt', 'r') as file3:
    file3_content = file3.readlines()
    print(file3_content)

print(file3_content[0].strip().split(','))


