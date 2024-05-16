import os, shutil

# run the user's program in our generated folders
os.chdir('module/root_folder')


def convert_size(size):
    if size < 1000:
        return f"{size}B"
    elif size < 10000:
        return f"{size // 1000}KB"
    elif size < 100000:
        return f"{size // 10000}MB"
    elif size < 1000000:
        return f"{size // 100000}GB"


# put your code here
print("Input the command")
while True:
    cmd = input().split(" ")
    if cmd[0] == "pwd":
        print(os.getcwd())
    elif cmd[0] == "cd":
        try:
            os.chdir(cmd[1])
            print(os.getcwd().split("/")[-1])
        except OSError:
            print("Invalid command")
        except IndexError:
            print("Invalid command")
    elif cmd[0] == "ls":
        files = sorted([x for x in os.listdir() if "." not in x])
        files.extend(sorted([x for x in os.listdir() if "." in x]))
        for item in files:
            size = os.stat(item).st_size
            if len(cmd) == 1:
                print(item)
            elif cmd[1] == "-l":
                print(f"{item} {size}" if "." in item else item)
            elif cmd[1] == "-lh":
                print(f"{item} {convert_size(size)}" if "." in item else item)
    elif cmd[0] == "rm":
        try:
            if cmd[1].startswith("."):
                files = [x for x in os.listdir() if cmd[1] in x]
                for item in files:
                    if cmd[1] in item:
                        os.remove(item)
                if not files:
                    print(f"File extension {cmd[1]} not found in this directory")
            elif "." in cmd[1]:
                os.remove(cmd[1])
            else:
                shutil.rmtree(cmd[1])
        except FileNotFoundError:
            print("No such file or directory")
        except NotADirectoryError:
            print("No such file or directory")
        except IndexError:
            print("Specify the file or directory")
    elif cmd[0] == "mv":
        try:
            if cmd[1].startswith("."):
                files = [x for x in os.listdir() if cmd[1] in x]
                for item in files:
                    if cmd[1] in item:
                        ans = ""
                        if os.path.exists(f"{cmd[2]}/{item}"):
                            ans = input(f"{item} already exists in this directory. Replace? (y/n)")
                        while ans not in ['y', 'n']:
                            ans = input(f"{item} already exists in this directory. Replace? (y/n)")
                        if ans == 'y':
                            shutil.move(item, cmd[2])
                if not files:
                    print(f"File extension {cmd[1]} not found in this directory")
            else:
                if os.path.isdir(cmd[2]) and os.path.exists(f"{cmd[2]}/{cmd[2]}"):
                    print("The file or directory already exists")
                elif not os.path.isdir(cmd[2]) and os.path.exists(cmd[2]):
                    print("The file or directory already exists")
                else:
                    shutil.move(cmd[1], cmd[2])
        except FileNotFoundError:
            print("No such file or directory")
        except IndexError:
            print("Specify the current name of the file or directory and the new location and/or name")
        
    elif cmd[0] == "mkdir":
        try:
            os.mkdir(cmd[1])
        except FileExistsError :
            print("The directory already exists")
        except IndexError:
            print("Specify the name of the directory to be made")
    elif cmd[0] == "cp":
        if len(cmd) > 3:
            print("Specify the current name of the file or directory and the new location and/or name")
        else:
            try:
                if cmd[1].startswith("."):
                    files = [x for x in os.listdir() if cmd[1] in x]
                    for item in files:
                        if cmd[1] in item:
                            ans = ""
                            if os.path.exists(f"{cmd[2]}/{item}"):
                                ans = input(f"{item} already exists in this directory. Replace? (y/n)")
                            while ans not in ['y', 'n']:
                                ans = input(f"{item} already exists in this directory. Replace? (y/n)")
                            if ans == 'y':
                                shutil.copy(item, cmd[2])
                    if not files:
                        print(f"File extension {cmd[1]} not found in this directory")
                else:
                    shutil.copy(cmd[1], cmd[2])
            except IndexError:
                print("Specify the file")
            except FileNotFoundError:
                print("No such file or directory")
            except NotADirectoryError:
                print("No such file or directory")
            except FileExistsError :
                print(f"{cmd[1]} already exists in this directory")
            except shutil.SameFileError:
                print(f"{cmd[1]} already exists in this directory")   
    else:
        print("Invalid command")
