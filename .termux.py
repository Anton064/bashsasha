import os

os.system("clear")

re ="\033[1;31m"
wh ="\033[1;37m"
gr ="\033[1;32m"
cy ="\033[1;36m"
sn ="\033[1;35m"

os.system("pkg install screenfetch")
os.system("clear")

information = "Offline"

print(f"""
Welcome to Termux!
 ___________________
|👤 Пользователь    |
|-------------------|
|👤 USER_NAME: Саша |
|___________________|

Administrator: {re}"""+ information + f"""{wh}


Wiki:            {cy}https://wiki.termux.com{wh}
Community forum: {cy}https://termux.com/community{wh}
Gitter chat:     {cy}https://gitter.im/termux/termux{wh}
GitHub:          {cy}https://github.com/Anton064{wh}
IRC channel:     #termux on freenode

Working with packages:

 * Search packages:   pkg search <query>
 * Install a package: pkg install <package>
 * Upgrade packages:  pkg upgrade

Subscribing to additional repositories:

 * Root:     pkg install root-repo
 * Unstable: pkg install unstable-repo
 * X11:      pkg install x11-repo

Report issues at {cy}https://termux.com/issues{wh}
""")
