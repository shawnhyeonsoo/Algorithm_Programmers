import re
def solution(files):
    temp = [re.split(r"([0-9]+)", i) for i in files]
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    return ["".join(s) for s in sort]