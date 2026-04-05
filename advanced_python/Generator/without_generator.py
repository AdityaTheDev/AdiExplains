aadhar_files=[ i for i in range(10) ]

def load_file():
    return aadhar_files

def process_file(file):
    return f"Processed file : {file}"

def main():
    files = load_file()
    for file in files:
        result = process_file(file)
        print(result)

main()