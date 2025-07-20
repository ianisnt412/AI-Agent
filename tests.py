from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def tests():
    result = (get_files_info("calculator", "."))
    print("Result for current directory:")
    print(result)

    result = (get_files_info("calculator", "pkg"))
    print("\nResult for 'pkg' directory:")
    print(result)

    result = (get_files_info("calculator", "fuck_boots"))
    print("\nResult for non-existing directory:")
    print(result)
   
    result = (get_files_info("calculator", "/bin"))
    print("\nResult for '/bin' directory:")
    print(result)

    result = (get_files_info("calculator", "../"))
    print("\nResult for '../' directory:")
    print(result)

def tests_2():
    result = get_file_content("calculator", "lorem.txt")
    print("\nResult for Ipsum text file:")
    print(result)

def tests_3():
    result = (get_file_content("calculator", "main.py"))
    print("Result for current directory:")
    print(result)

    result = (get_file_content("calculator", "pkg/calculator.py"))
    print("\nResult for 'pkg' directory:")
    print(result)

    result = (get_file_content("calculator", "fuck_boots"))
    print("\nResult for non-existing directory:")
    print(result)
   
    result = (get_file_content("calculator", "/bin/cat"))
    print("\nResult for '/bin' directory:")
    print(result)

    result = (get_file_content("calculator", "pkg/does_not_exist.py"))
    print("\nResult for '../' directory:")
    print(result)

def tests_4():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for write to /calculator/lorem.txt:")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("\nResult for new file /calculator/morelorem.txt:")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("\nResult for write file outside of permitted working directory:")
    print(result)

def tests_5():
    result = run_python_file("calculator", "main.py")
    print("\nResult for calculator usage:")
    print(result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("\nResult for running the calculator:")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print("\nResult for the tests.py file:")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print("\nResult for trying to run outside of the allowed working directory:")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print("\nResult for trying to run a file that doesn't exist:")
    print(result)


if __name__ == "__main__":
    #tests()
    #tests_2()
    #tests_3()
    #tests_4()
    tests_5()