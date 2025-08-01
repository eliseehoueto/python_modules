def read_file_with_error():
    try:
        filename="input.txt"
        with open(filename,'r') as readfile:
            content = readfile.read()
        print(content)
        
        with open(filename,'w') as inputfile:
            inputfile.write('This is the modification!!!')
            inputfile.write('In hope to become a good enginner!!!')

        
        with open(filename,'r') as readfile:
            content = readfile.read()
        print(content)
    except FileNotFoundError:
        print("File not exist")
    except FileNotFoundError:
        print('File not found')
    except Exception as error:
        print(f'The error is:{error}')

        
read_file_with_error()