from aocd import lines, submit

def do_line(line: str) -> bool:
    (elf1, elf2) = line.split(',')
    (start1, end1) = [int(x) for x in elf1.split('-')]
    (start2, end2) = [int(x) for x in elf2.split('-')]
    return (start1 >= start2 and end1 <= end2) or (start1 <= start2 and end1 >= end2)

# submit(len([x for x in lines if do_line(x)]))

def do_line2(line: str) -> bool:
    (elf1, elf2) = line.split(',')
    (start1, end1) = [int(x) for x in elf1.split('-')]
    (start2, end2) = [int(x) for x in elf2.split('-')]
    return (start1 >= start2 and end1 <= end2) or (start1 <= start2 and end1 >= end2)\
        or (start2 <= start1 <= end2) or (start2 <= end1 <= end2)\
        or (start1 <= start2 <= end1) or (start1 <= end2 <= end1)

submit(len([x for x in lines if do_line2(x)]))
