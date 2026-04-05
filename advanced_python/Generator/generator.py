aadhar_files=[ i for i in range(10) ]


def process_file(file):
    return f"Processed file : {file}"

def main():
    for file in aadhar_files:
        result = process_file(file)
        yield result


for result in main():
    print(result)

