import numpy as np


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


if __name__ == '__main__':
    assert vertical_ways(3, 2) == 18
    for w in range(1, 47 + 1):
        for h in range(1, 43 + 1):
            print(w, h, vertical_ways(w, h))
    # rot = rot_mat(-1 * np.pi/4)
    # X = np.array([[1], [2]])
    # print(rot.dot(X) / (2 ** .5) * 2)
