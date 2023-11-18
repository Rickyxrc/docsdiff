import hashlib, os
from colorama import Fore, Style, just_fix_windows_console

just_fix_windows_console()

def sha_file(filename:str) -> str:
    with open(filename, "rb") as file_byte:
        sha256obj = hashlib.sha256()
        sha256obj.update(file_byte.read())
        return sha256obj.hexdigest()

source_dir = input("请将原来的文件夹拖入这里：")
dest_dir = input("请将现在的文件夹拖入这里：")

def dfs(result:dict, path:str, basic_dir:str) -> None:
    for file in os.listdir(os.path.join(basic_dir, path)):
        accual_path = os.path.join(basic_dir, path, file)
        file_path = os.path.join(path, file)
        if os.path.isdir(accual_path):
            dfs(result, file_path, basic_dir)
        else:
            result[file_path] = sha_file(accual_path)

source_files = {}
dest_files = {}

print(f"{Fore.BLUE}正在扫描原始文件夹……{Style.RESET_ALL}")
dfs(source_files, '', source_dir)
print(f"{Fore.BLUE}正在扫描目标文件夹……{Style.RESET_ALL}")
dfs(dest_files, '', dest_dir)

for source in source_files:
    if dest_files.get(source, None) == None:
        print(f"{Fore.RED}{source} 文件已被删除！{Style.RESET_ALL}")

for dest in dest_files:
    if source_files.get(dest, None) == None:
        print(f"{Fore.GREEN}{dest} 文件已被添加！{Style.RESET_ALL}")

for source in source_files:
    if dest_files.get(source, None) != None:
        if source_files[source] != dest_files.get(source):
            print(f"{Fore.YELLOW}{source} 文件的内容已被变更！{Style.RESET_ALL}")

