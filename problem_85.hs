-- Horrifying
-- 
--
ways j k = dim1ways j * dim1ways k
    where dim1ways p = p * (p + 1) / 2

offset (j, k) = abs(2000000 - ways j k)
first a b = a
second a b = b
better p1 p2 
    | offset p1 < offset p2 = p1
    | offset p1 >= offset p2 = p2

search' i (cur_j, maxval)
    | cur_j == maxval = (i, maxval) 
    | otherwise       = better (i, cur_j) (search' i (cur_j + 1, maxval))
search i maxval = search' i (1, maxval)

search2' (cur_i, maxval)
    | cur_i == maxval = search cur_i maxval
    | otherwise       = better (search cur_i maxval) (search2' (cur_i + 1, maxval))

search2 maxval = search2' (1, maxval)

prod (a, b) = a * b 
answer = prod(search2 1000)
main = print(answer)

