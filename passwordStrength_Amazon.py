# Password strength - Amazon Assesment question
# Given a password string. Find the strength of the passwrd
# Strength of a password is defined as number of substrings 
# having atleast 1 vowel and 1 consonant

# Example :
# password = "thisisbeautifulplace"
# output = 8

# Explanation:
# substrings - 
# 'thi', 'si', 'sbe', 'aut', 'if', 'ul', 'pla', 'ce'


def strength(password):
    vowel = 0
    consonant = 0
    strength = 0
    vowels = 'aeiou'
    for ch in password:
        if ch in vowels:
            vowel += 1
        else:
            consonant += 1
        if vowel >= 1 and consonant >= 1:
            vowel = 0
            consonant = 0
            strength += 1
    return strength

if __name__ == '__main__':
    password = "thisisbeautifulplace"

    ans = strength(password)
    print(ans)