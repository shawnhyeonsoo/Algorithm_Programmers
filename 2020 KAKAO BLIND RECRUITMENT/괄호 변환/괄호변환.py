def is_right(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")" and len(stack) == 0:
            return False
        else:
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False

def is_balanced(s):
    if s.count('(') == s.count(')'):
        return True
    else:
        return False

def split_string_u(s,i):
    if is_balanced(s[:i]):
        return i
    else:
        return split_string_u(s,i+1)


def solution(s):
    ans = ''
    if s == '':
        return ans
    else:
        u = s[:split_string_u(s,1)]
        v = s[split_string_u(s,1):]
        ans = ''
        if is_right(u):
            u += solution(v)
            ans += u
        else:
            ans += '('
            ans += solution(v)
            u = u[1:-1]
            ans += ')'
            u=u.replace("(","i")
            u=u.replace(")",'j')
            u=u.replace("i",")")
            u=u.replace("j","(")
            ans += u

    return ans