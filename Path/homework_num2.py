def get_cats_info(path):
    try:
        cat_info = []
        with open(path, "r", encoding="utf-8") as file:
            for i in file:
                line = i.strip().split(",")
                cat_info.append({"id": line[0], "name": line[1], "age": line[2]})
        return cat_info

    except FileNotFoundError:
        print("File not found")


cats = get_cats_info("text.txt")
print(cats)
