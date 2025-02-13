def total_salary(path):
    try:
        with open("salary_file.txt", "r", encoding="utf-8") as path:
            read = [el.strip(",") for el in path.readlines()]
            print(read)
    except FileNotFoundError:
        print("File not found")
