def solution(w, h):
    import math
    if (w > h):
        w, h = h, w

    return w * h - (h + w - math.gcd(w, h))