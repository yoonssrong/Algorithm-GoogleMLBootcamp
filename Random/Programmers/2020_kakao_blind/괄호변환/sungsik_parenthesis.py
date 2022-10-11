# 최소 단위의 "균형잡힌 괄호 문자열" 분리
def sep(p):
  l, r = 0, 0   # (:left / ):right 로 count
  for i in range(len(p)):
    if p[i] == '(':
      l += 1
    else:
      r += 1
    if l == r:
      u = p[:i + 1]
      v = p[i + 1:] if i + 1 < len(p) else ""
      break
  return u, v

# "올바른 괄호 문자열"인지 확인
def check(p):
  stack = []
  for c in p:
    if c == '(':
      stack.append(c)
    else:
      if not len(stack):
        return False
      elif stack[-1] == '(':
        stack.pop()
  return False if len(stack) else True

def solution(p):
  result = ""
  if not len(p): return ""    # 1
  u, v = sep(p)               # 2

  if check(u):                # 3
    result = u + solution(v)    # 3-1
  else:                       # 4
    tmp = "("                   # 4-1
    tmp += solution(v)          # 4-2
    tmp += ")"                  # 4-3
    u = u[1:-1]                 # 4-4
    for c in u:
      if c == '(':
        tmp += ')'
      else:
        tmp += '('
    result += tmp
  return result     # 4-5

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.

p = "()))((()"
print(solution(p))
