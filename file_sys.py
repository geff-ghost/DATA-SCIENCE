
with open('./data/loans1.txt', 'r') as file1:
    file1_content = file1.read()
# print(file1_content)

with open('./data/loans2.txt', 'r') as file2:
    file2_content = file2.read()
    # print(file2_content)

with open('./data/loans3.txt', 'r') as file3:
    file3_content = file3.readlines()
    # print(file3_content)

# print(file3_content[0].strip().split(','))

def parse_headers(header_line):
    return header_line.strip().split(',')

def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            values.append(float(item))
    return values

def create_item_dict(values: list[int], headers: list[str]) -> dict:
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result

def read_csv(path):
    result = []
    # Open the file in read mode
    with open(path, 'r') as f:
        # Get the list of line
        lines = f.readlines()
        # Parse in the headers
        headers = parse_headers(lines[0])
        # Loop through the remaining lines and parse in values
        for data_line in lines[1:]:
            # Parse in the values
            values = parse_values(data_line)
            # Create item dict with the values
            item_dict = create_item_dict(values, headers)
            # Add the item dict to the result
            result.append(item_dict)
    return result

print(read_csv('./data/loans1.txt'))
print()
print(read_csv('./data/loans2.txt'))
print()
print(read_csv('./data/loans3.txt'))
print()
print(read_csv('./data/students.txt'))


