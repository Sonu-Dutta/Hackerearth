# Sample Input
# 3
# abb
# aaab
# ababa
# Sample Output
# ab
# ab
# ababa

# Explanation
# In the first case, S = "abb". Since, S has same consecutive letter 'b' we will delete one of them. So, the good string will be "ab".

# In the second case, S = "aaab" and since S has same consecutive letter 'a' we will delete them one by one. aaab -> aab -> ab. So, the good string will be "ab".

# In the third case, S = "ababa" and S has no same consecutive letter. So, the good string will be "ababa".
n = int(input())
for i in range(n):
    s = input()
    st = []
    for i in range(len(s)):
        if len(st)==0:
            st.append(s[i])
        elif st[-1]==s[i]:
            pass
        else:
            st.append(s[i])
    print(''.join(st))