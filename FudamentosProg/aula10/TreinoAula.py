def matchesPattern(s, pattern):
    s = s.lower()
    pattern = pattern.lower()
    if len(s) == len(pattern):
        for i in range(len(s)):
            if s[i] == pattern[i] or pattern[i]=="?":
                x = True
            else:
                x= False
    else: 
        x= False
    return x


print( matchesPattern("secret", "s?c??t") )  #-> True
print( matchesPattern("secreta", "s?c??t") ) #-> False
print( matchesPattern("socket", "s?c??t") )  #-> True
print( matchesPattern("soccer", "s?c??t") )  #-> False
print( matchesPattern("SEcrEt", "?ecr?t") )  #-> True
print( matchesPattern("SEcrET", "?ecr?t") )  #-> True
print( matchesPattern("SecrEt", "?ECR?T") )  #-> True