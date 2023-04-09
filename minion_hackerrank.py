def minion_game(string):
    # your code goes here
    vowels = ['A','E','I','O','U']
    stuart = 0
    kevin = 0 
    for i in range(len(string)):
        if string[i] in vowels:
                kevin += len(string) - i
        else:
                stuart += len(string)  - i 
    if stuart>kevin:
        print(f'Stuart {stuart}')
    elif stuart<kevin:
        print(f'Kevin {kevin}') 
    else:
        print("Draw")
if __name__ == '__main__':
     s = input("string : ")
     minion_game(s)