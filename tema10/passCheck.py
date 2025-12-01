import re

def check(ex, txt):
    pattern=re.compile(ex)
    if len(pattern.findall(txt))>0:
        return True
    return False

def checkPassword(txt):
    if check(r".*[a-z]+.*", txt) and check(r".*[A-Z]+.*", txt) and check(r".*[~\!\@\#\$\%\^\&\*\(\)_\+`\-={}\|\[\]\\;':\",\./\<\>\?]+.*", txt):
        return True
    return False

print(checkPassword("1323Gaye!"))
