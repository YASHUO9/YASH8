def main(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0] == s[1]:
        small_output = main(s[2:])
        return s[0] + small_output
    else:
        small_output = main(s[1:])
        return s[0]+ small_output
        
print(main("ppsskk"))