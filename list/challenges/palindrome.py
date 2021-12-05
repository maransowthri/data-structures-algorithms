str1 = 'malaayalam'
str2 = 'malaayalam'


def check_palindrome(str1, str2):
    if len(str1) != len(str2):
        return False
    
    for i in range(len(str1)):
        if str1[i] != str2[len(str2) - i - 1]:
            return False
    
    return True


print(check_palindrome(str1, str2))