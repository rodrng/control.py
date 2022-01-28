
import re

data = "jr4jf34jfh4n2fh23j3l43kffjjk34fj32d23dmnasdf"

# 문자열에서 숫자 제거 정규식
newdata = re.sub(r'[0-9]+',"", data)
# newdata = re.sub(r'[^0-9]+',"", data) #문자제거 정규식
print(newdata)


data2 = "g@g%^23dfsgf@sdf235g$#fg54%@gf#^g%345^&^%*d*()h(+_54)*g++f&%$#h"
newdata2 = re.sub("[!@#$%^&*()_+-=]","", data2) # 특수문자 제거 정규식
print(newdata2)


data3 ="789asdf안df223녕$%$4하sdaf세!%$요#4s%$fs@"
newdata3 = re.sub("[^ㄱ-ㅣ가-힣]", "", data3) # 한글만 추출 정규식
print(newdata3)
