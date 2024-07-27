import hashlib

def crackHash(inputPass):
    try:
        passFile = open("wordlist.txt", "r")
    except FileNotFoundError:
        print("Could not find file")
        return
    
    for password in passFile:
        password = password.strip()
        encPass = password.encode("utf-8")
        digest = hashlib.md5(encPass).hexdigest()
        if digest == inputPass:
            print("Password Found: " + password)
            passFile.close()
            return
    
    print("Password not found")
    passFile.close()

if __name__ == "__main__":
    crackHash("bdbabibcnie12efi393")
