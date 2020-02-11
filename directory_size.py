import os
path = r"C:\Users\ling910520\Desktop\c-sharp\New folder"

# print(f"{os.path.getsize(path)}")

def folder_size(path='.'):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += folder_size(entry.path)
    print(f"before return {total}")
    return total

ans = folder_size(path)
ans/1e6