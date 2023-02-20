import string
def letters_file_line(n):
    with open("words.txt","w") as f:
        alphabet=string.ascii_letters
        for i in range(0,len(alphabet),n):
            letters=[alphabet[i:i+n]+"\n"]
            f.writelines(letters)
letters_file_line(2)