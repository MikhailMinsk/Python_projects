from ftplib import FTP
from sys import exit


#           for local host :
#
# ftp = FTP('')
# ftp.connect('localhost',15001 - input number of port)
# print(ftp.login())

# ______________________________________________________________________
try:
    ftp = FTP(input('Input server: '))
except Exception:
    print('Host can not be resolved')
    exit()

user = input('Input username: ')
password = input('input password: ')

try:
    if len(user) > 0:
        print(ftp.login(user, password))
    else:
        print(ftp.login())
except Exception:
    print('Invalid login combination')
    exit()
# _______________________________________________________________________


print("input 'help' for a list of commands and information about them")


def uppath(path):
    cur = 0
    for _ in path[::-1]:
        cur += 1
        if _ == '/':
            return path[0:len(path) - cur]


while True:
    tmp = []
    tmp = input('FTP:> ').split()
    if 'help' in tmp:
        print("Available commands:"
              "\n rmd  <name directory>     \t- remove directory"
              "\n mkd  \\<name directory>   \t- make directory "
              "\n dir                       \t- print working directory"
              "\n rename <name> to <name>   \t- rename file or directory"
              "\n list \\<name directory>   \t- list "
              "\n up                        \t- 1 directory up"
              "\n cwd  \\<name directory>   \t- change working directory <name directory>"
              "\n pwd                       \t- path work directory"
              "\n delete <file name>        \t- delete file "
              "\n exit                      \t- close session")
    elif 'dir' in tmp:
        print(ftp.retrlines('LIST'))
    elif 'rename' in tmp:
        print(ftp.rename(tmp[1], tmp[2]))
    elif 'rmd' in tmp:
        print(ftp.rmd(tmp[1]))
    elif 'mkd' in tmp:
        try:
            print(ftp.mkd(tmp[1]))
        except Exception as s:
            print('       Input full path to directory')
    elif 'list' in tmp:
        print(ftp.dir(tmp[1]))
    elif 'delete' in tmp:
        print(ftp.delete(tmp[1]))
    elif 'cwd' in tmp:
        try:
            print(ftp.cwd(tmp[1]))
        except Exception as s:
            print('       Input full path to directory')
    elif 'pwd' in tmp:
        print(ftp.pwd())
    elif 'up' in tmp:
        print(ftp.cwd(uppath(ftp.pwd())))
    elif 'exit' in tmp:
        print('Session ended')
        ftp.close()
        exit()
    else:
        print("Wrong input. Input 'help' to view commands")
        continue
