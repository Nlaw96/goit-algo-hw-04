def total_salary(path):
    try:
        total = 0
        cnt = 0
        with open(path, "r", encoding="utf-8") as file:
            for j in file:
                try:
                    p = j.strip().split(",")
                    total += int(p[1])
                    cnt += 1
                except ValueError:
                    print("Incorrect file data")

        average = total // cnt
        return total, average

    except FileNotFoundError:
        print("File 'path' not found")
    

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

