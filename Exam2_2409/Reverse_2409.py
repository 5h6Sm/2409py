#2409 임수민

str = input("영문자 입력 : ")
ntrs = []
num = len(str)
trs = list(str)
trs.reverse()
ntrs = ''.join(trs)
print(f"거꾸로 출력 : {ntrs}",end="")