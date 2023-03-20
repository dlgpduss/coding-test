# word = input().upper()
# word_list = list(set(word))

# cnt = []
# for i in word_list:
#   count = word.count
#   cnt.append(count(i))

# if cnt.count(max(cnt)) > 1:
#   print("?")

# else:
#   print(word_list[(cnt.index(max(cnt)))])

# 중복 없는 단어를 한글자씩 받아서 count 해줌 
# => 가장 많이 나온 값을 대문자로 변환 후 출력,
# 여러 개가 많이 나오면 ? 출력

s = input()
s = s.upper()
res = [0]*26
for i in range(len(s)):
    res[ord(s[i]) - ord('A')] += 1
    mx = max(res)
    mx_cnt = res.count(mx)
if mx_cnt > 1:
    print("?")
else:
    print(chr(res.index(mx)+65))