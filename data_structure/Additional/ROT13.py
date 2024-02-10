# ROT13(字符替换加密算法,将每个字母替换为字母表中相对应的第13个字母)
def rot13(text):
    encrypted = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            rotated = (ord(char) - ascii_offset + 13) % 26 + ascii_offset
            encrypted += chr(rotated)
        else:
            encrypted += char
    return encrypted
