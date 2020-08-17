def generate_hashtag(s):
    if s=="" or len(s.replace(" ", ""))<141:
        return False
    else:
        solution="#"
        for i in range(len(s)):
            if s[i-1]==" " or i==0 and type(s[i])==