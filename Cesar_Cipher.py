from replit import clear

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#  to avoid condition mentioned below at line 10 comment line 1 and un comment line 3 or just dont modify any thing this is just an optional way to avoid shifting problem..
# alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

proceed = True
possible_direction = ['encode','decode']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def caesar(message, shift_number, action):
    new_message = ''
    shift_number %= 25 
    if action == 'decode':
        shift_number *= -1
    for char in message:
        if char in alphabets:
            j = alphabets.index(char) + shift_number
            # what if shift number + index of letter is greater than 25 then we get an error the two ways of solving this is through lines 11,12 or by un commenting line 3 
            if j > 25:
                j = abs(j - 26)

            # a similar problem like at line 10 and to overcome this we can have an approach as below
            if j < 0:
                j = abs(j + 26)
            new_message += alphabets[j]
        else:
            new_message += char
    print(f"your message is {new_message} \n")



while proceed:
     # comment line 42 if you don't want to clear previous output
    clear()
    print(logo)
    direction = input("Type'encode' to encrypt, 'decode' to decrypt : ").lower()
    if direction not in possible_direction:
        print("OOPS!! seems like you entered the wrong keyword, TryAgain")
        go = input("Want to have another go (yes/no) : ")
        if go.lower() == 'no' or not go.lower() == 'yes':
            proceed = False
            print("Good Bye!!")
        continue
    text = input("Type your message : ")
    shift = int(input("enter the shift number : "))

    caesar(message=text,shift_number=shift,action=direction)
    go = input("Want to have another go (yes/no) : ")
    if go.lower() == 'no' or not go.lower() == 'yes':
        proceed = False
        print("Good Bye!!")


