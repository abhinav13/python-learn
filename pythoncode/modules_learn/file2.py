import  file1


def file2_func2():
    print("This is file2_func2 calling file1_func1")
    file1.file1_func1()

if __name__ == '__main__':
    file2_func2()
