# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
def is_palindrome(n):
    if n > 10:
        n = str(n)
        a = n[::-1]
        return a == n


output = filter(is_palindrome, range(1, 1000))
print(list(output))
