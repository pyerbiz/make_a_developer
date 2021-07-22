""" reproducible in windows """

# try to write binary data in write mode
with open("data.bin", "w") as f:
    f.write(b"\xf1\xf2\xf3\xf4\xf5")
# TypeError: write() argument must be str, not bytes


# write a file with binary data in binary mode
with open("data.bin", "wb") as f:
    f.write(b"\xf1\xf2\xf3\xf4\xf5")
# written file has UTF-8 encoding


# preferred encoding in my system is different
import locale

print(locale.getpreferredencoding())
# cp1252


# read file with binary data and is in UTF-8 encoding \
# should fail acc to book, but doesn't
with open("data.bin") as f:
    print(f.read())
# ñòóôõ
# its as if encoding is 'cp1252' by default


# book specifies the encoding to get same result as above
with open("data.bin", encoding="cp1252") as f:
    data = f.read()
