import numpy as np
from math import ceil, floor


def rot_mat(theta):
    return np.array([
        [np.cos(theta), -1 * np.sin(theta)],
        [np.sin(theta), np.cos(theta)]])

def grid(w, h):
    for x in range(w + 1):
        for y in range(h + 1):
            yield (x, y)

def vertical_ways_v0(w, h):
    """Too slow."""
    seen = set()
    for p1 in grid(w, h):
        for x in range(p1[0], w + 1):
            for y in range(p1[1], h + 1):
                p2 = (x, p1[1])
                p3 = (p1[0], y)
                p4 = (x, y)
                pts = tuple(sorted(set((p1, p2, p3, p4))))
                if len(pts) < 4:
                    continue
                seen.add(pts)
    return len(seen)


def vertical_ways(w, h):
    count = 0
    for size_w in range(1, w + 1):
        for size_h in range(1, h + 1):
            news = ((w - size_w + 1) * (h - size_h + 1))
            # print(size_w, size_h, news)
            count += news
    return count

def line_ways(w, h):
    count = 0
    for size_w in range(1, 2 * (w + 1)):
        for size_h in range(1, 2 * (h + 1)):
            # lines
            line_count = max(h + 1 - ceil((size_w + size_h) / 2), 0)
            line_ways = max(
                    w + 1 - ceil(size_w / 2) - ceil(size_h / 2), 0)
            news = line_count * line_ways
            # print(size_w, size_h, news)
            count += news
    return count

def dot_ways(w, h):
    count = 0
    for size_w in range(1, 2 * (w + 1)):
        for size_h in range(1, 2 * (h + 1)):
            # lines
            line_count = max(h - floor((size_w + size_h) / 2), 0)
            line_ways = max(
                    w - floor(size_w / 2) - floor(size_h / 2), 0)
            news = line_count * line_ways
            # print(size_w, size_h, news)
            count += news
    return count

def diag_ways(w, h):
    return line_ways(w, h) + dot_ways(w, h)

def ways(w, h):
    return diag_ways(w, h) + vertical_ways(w, h)

def ans(w, h):
    count = 0
    for i in range(1, w + 1):
        for j in range(1, h + 1):
            count += ways(i, j)
    return count

if __name__ == '__main__':
    assert diag_ways(3, 2) == 7 + 2 + 4 + 4 + 1 + 1
    assert vertical_ways(3, 2) == 18
    assert ways(1, 1) == 1
    assert ways(2, 1) == 4
    assert ways(3, 1) == 8
    assert ways(1, 2) == 4
    assert ways(2, 2) == 18
    assert ways(3, 2) == 37
    assert ans(3, 2) == 72
    print(ans(47, 43))
    # rot = rot_mat(-1 * np.pi/4)
    # X = np.array([[1], [2]])
    # print(rot.dot(X) / (2 ** .5) * 2)
