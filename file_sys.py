from functions import loan_emi

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

def compute_emis(loans):
    for loan in loans:
        loan['emi'] = loan_emi(
            amount=loan['amount'],
            rate=loan['rate'] / 12, # the CSV contains yearly rates
            duration=loan['duration'],
            down_payment=loan['down_payment']
        )



def write_csv(items, path):
    # Open the file in write mode
    with open(path, 'w') as f:
        # Return if there's nothing to write
        if len(items) == 0:
            return
        
        # Write the headers in the first line
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')

        # Write one item per line
        for item in items:
            values = []
            for header in headers:
                values.append((str(item.get(header, ''))))
            f.write(','.join(values) + '\n')

loans3 = read_csv('./data/loans3.txt')
compute_emis(loans3)
write_csv(loans3, './data/emis3.txt')

with open('./data/emis3.txt', 'r') as f:
    print(f.read())

print()

loans1 = read_csv('./data/loans1.txt')
compute_emis(loans1)
write_csv(loans1, './data/emis1.txt')

with open('./data/emis1.txt', 'r') as f:
    print(f.read())

print()

loans2 = read_csv('./data/loans2.txt')
compute_emis(loans2)
write_csv(loans2, './data/emis2.txt')

with open('./data/emis2.txt', 'r') as f:
    print(f.read())