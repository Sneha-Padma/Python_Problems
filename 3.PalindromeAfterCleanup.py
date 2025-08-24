#Day3 Palindrome After CleanupS
def palindrome_after_cleanup(s):
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1]
s = input()

if palindrome_after_cleanup(s):
    print("YES")
else:
    print("NO")