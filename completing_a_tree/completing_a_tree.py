vertex_num = int(input())
edges = []

while True:
    try:
        edges.append(list(map(int, input().split())))
    except EOFError:
        break
print((vertex_num - 1 - len(edges)))