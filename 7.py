from aocd import lines, submit


class DirectoryItem:
    def size(self):
        pass


class File(DirectoryItem):
    def __init__(self, size: int):
        self.bytes = size

    def size(self):
        return self.bytes


class Directory(DirectoryItem):
    def __init__(self, parent):
        self.parent = parent
        self.items = dict()

    def size(self):
        return sum([x.size() for x in self.items.values()])

    def add(self, name: str, item: DirectoryItem):
        self.items[name] = item

    def get_dir(self, name: str):
        return self.items.setdefault(name, Directory(self))

    def directories(self):
        return [x for x in self.items.values() if isinstance(x, Directory)]


# Start parsing
root = Directory(None)
cwd = [root]

for line in lines:
    tokens = line.split(' ')
    if tokens[0] == '$':
        if tokens[1] == 'cd':
            if tokens[2] == '/':
                cwd = [root]
            elif tokens[2] == '..':
                cwd.pop()
            else:
                cwd.append(cwd[-1].get_dir(tokens[2]))
        elif tokens[1] == 'ls':
            pass
    else:
        # It's a file, from ls
        if tokens[0] == 'dir':
            cwd[-1].get_dir(tokens[1])
        else:
            cwd[-1].add(tokens[1], File(int(tokens[0])))


# DFS
def part1(dir: Directory):
    dir_size = dir.size()
    size = dir_size if dir_size <= 100000 else 0
    size += sum([part1(x) for x in dir.directories()])
    return size


print(part1(root))

# Part 2
total_size = 70000000
needed = 30000000
used = root.size()
to_free = needed - (total_size - used)
# Find the smallest directory that's bigger than that
# Preorder DFS with short circuiting
def part2(dir: Directory) -> int:
     min_size = min([part2(x) for x in dir.directories() if part2(x)], default=None)
     if min_size:
         return min_size
     dir_size = dir.size()
     return dir_size if dir_size >= to_free else None
submit(part2(root))