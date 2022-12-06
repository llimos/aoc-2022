from aocd import data, submit

def find_token(length):
    chars = set()
    l = 0
    r = 0
    while r - l < length and r < len(data):
        if data[r] in chars:
            while data[l] != data[r]:
                chars.remove(data[l])
                l += 1
            if l < r:
                chars.remove(data[l])
                l += 1
        chars.add(data[r])
        r += 1
    return r

print(find_token(4))
print(find_token(14))
