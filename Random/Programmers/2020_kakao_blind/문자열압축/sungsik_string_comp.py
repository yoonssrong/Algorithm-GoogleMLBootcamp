s = "aabbacccd"
# expect : 7
# 2a2ba3c


result = len(s)               # 압축 한번도 안됐을 때의 길이
for w in range(1, (len(s)//2)+1):   # window 크기
  sub_s = s[:w]   # 판별할 부분 문자열
  cnt = 1         # 현재 부분 문자열의 반복된 개수

  comp = ''
  for i in range(w, len(s), w):       # window 크기만큼 이동하며 문자열 압축
    if sub_s == s[i:w + i]:           # 부분 문자열과 현재 문자열이 같으면 cnt +1
      cnt += 1
    else:                             # 부분 문자열과 현재 문자열이 다르면
      if cnt > 1:                         # cnt가 1보다 크면
        comp = comp + str(cnt) + sub_s    # 압축 문자열에 cnt와 부분 문자열 합쳐서 붙임
      else:                               # cnt가 1이면
        comp = comp + sub_s               # 압축 문자열에 부분 문자열만 붙임
      sub_s = s[i:i + w]              # 부분 문자열을 현재 문자열로 교체
      cnt = 1                         # cnt를 1로 초기화

  if cnt > 1:                       # 예외처리(마지막 문자열 판별):
    comp = comp + str(cnt) + sub_s  # cnt가 1보다 크면 압축 문자열에 cnt와 부분 문자열 합쳐서 붙임
  else:
    comp = comp + sub_s             # cnt가 1이면 압축 문자열에 부분 문자열만 붙임

  result = min(result, len(comp))   # 현재 압축 결과의 길이를 result와 비교해서 작은 수로 업데이트

print(result)              # 모든 압축 결과 중 가장 길이가 작은 수 반환
