import os

print(os.getcwd())

os.makedirs('./data', exist_ok=True)

print(os.listdir('.'))

print('data' in os.listdir('.'))

print(os.listdir('./data'))

print()
file1 = open('./data/loans1.txt', 'r')
file1_content = file1.read()
# print(file1_content)
file1.close()

with open('./data/loans2.txt', 'r') as file2:
    file2_content = file2.read()
    # print(file2_content)

with open('./data/loans3.txt', 'r') as file3:
    file3_content = file3.readlines()
    # print(file3_content)

# print(file3_content[0].strip().split(','))

def parse_headers(header_line):
    return header_line.strip().split(',')

headers = parse_headers(file3_content[0])
print(headers) 

def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            values.append(float(item))
    return values

values = parse_values(file3_content[2])
print(values)

values = parse_values(file3_content[1])
print(values)

def create_item_dict(values: list[int], headers: list[str]) -> dict:
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result

values1 = parse_values(file3_content[1])
print(create_item_dict(values1, headers))


