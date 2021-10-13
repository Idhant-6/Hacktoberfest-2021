import string
import os
import random
import pyperclip


def genpass(pass_len:int=16):
    passwd = ''
    passlen = pass_len
    chars = string.ascii_letters + string.digits + '!@#$%^&*()_+-=/*,./;'

    # generate random password
    random.seed = os.urandom(1024)
    passwd = ''.join(random.choice(chars) for i in range(passlen))
    
    # copy password to clipboard
    print("[!] GEnerated Password has been copied to the clipboard.")
    pyperclip.copy(passwd)


if __name__ == "__main__":
    pass_length = int(input("[+] Enter length of the password : "))
    genpass(pass_length)
