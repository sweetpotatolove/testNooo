time = input("일어나야 하는 시간 입력 [ex) 6:30] : ")
time_list = time.split(":")
h = int(time_list[0])
m = int(time_list[1])
m -= 40
if m < 0:
    h -= 1
    m += 60
if h < 0:
    h += 24
print("알람 시간: [ %d:%d ]"%(h,m))


n = int(input("몇 번째 피보나치 수를 알고싶나연?"))
f_list = [0,1]
for i in range(n):
    f_list.append(f_list[i]+f_list[i+1])
print(f_list[n])
## 그.. 처음에 수식 안보고 예시만 보고 제맘대로 짜봤는데여
## 리스트에는 index 9번째까지 들어가긴 하는데
## 일단 답이 나와서 걍 썼거든요
## 근데 뭐라 할까봐 수식 적힌대로 다시 짜봄
f_list2 = [0,1]
for j in range(2,n+1):
    f_list2.append(f_list2[j-1]+f_list2[j-2])
print(f_list2[n])