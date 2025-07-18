from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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



if __name__ == "__main__":
    #tests()
    #tests_2()
    tests_3()