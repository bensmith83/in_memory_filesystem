

CWD = "/"
ALL_FS=[]


def get_cwd():
    return CWD


def fs_find_node(cwd):
    global ALL_FS
    for myfile in ALL_FS:
        if myfile.name == cwd:
            return myfile
    return None

class File:
    def __init__(self,name,is_dir,parent):
        self.name = name
        self.is_dir = is_dir
        self.parent = parent
        self.children = []
        self.update_parents(parent,name)

    def get_full_path():
        pass
    def list_children():
        return self.children
        
    def update_parents(self,parent,name):
        cwd = get_cwd()
        parent_node = fs_find_node(parent)
        if parent_node:
            parent_node.children.append(name)



def fs_ls(args):
    cwd = get_cwd()
    for myfile in ALL_FS:
        if myfile.parent == cwd:
            print(myfile.name)
    return True

def fs_mkdir(args):
    if len(args) != 1:
        return True
    ALL_FS.append(File(args[0],True,get_cwd()))
    return File(args[0],is_dir=True,parent=get_cwd())
    return True

def fs_cd(args):
    if len(args) == 1:
        set_cwd(args[0])
    return True

def fs_touch(args):
    if len(args) != 1:
        return True
    ALL_FS.append(File(args[0],False,get_cwd()))
    return True

    
def set_cwd(arg):
    global CWD
    #TODO: check that arg exists
    cwd = get_cwd()
    if arg == ".":
        return
    if arg == "..":
        if cwd == "/":
            return CWD
        for myfile in ALL_FS:
            if cwd in myfile.children:
                set_cwd(myfile.name)
    for myfile in ALL_FS:
        if myfile.name == arg:
            CWD = arg
    return CWD

def fs_exit(args):
    return False

def fs_pwd(args):
    return get_cwd()

def init_fs():
    global ALL_FS
    ALL_FS = [File("/",True,"/")]

COMMANDS = {
    "ls": fs_ls,
    "mkdir": fs_mkdir,
    "cd": fs_cd,
    "touch": fs_touch,
    "pwd": fs_pwd,
    "exit": fs_exit
}

def main():
    more = True
    init_fs()
    print("Welcome to the Filesystem")
    while more:
        shell = input("> ")
        parsed = shell.split(" ")
        cmd = parsed[0]
        args = parsed[1:]
        if cmd in COMMANDS:
            more = COMMANDS[cmd](args)
            print(f"- {more}")
            

if __name__ == '__main__':
    main()
