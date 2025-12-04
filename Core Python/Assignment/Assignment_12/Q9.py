def count_word_char(str):
    char_count = 0
    word_count = 0
    in_word = False

    for ch in str:
        char_count +=1
        if(ch != ' ' and in_word == False):
            word_count +=1
            in_word = True
        elif (ch == ' '):
            in_word = False
    return word_count,char_count

string = input("enter the string : ")
word,char =count_word_char(string)

print("char : ",char)
print("words : ",word)