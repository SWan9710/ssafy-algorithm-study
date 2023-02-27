import sys
ds = tuple(zip((0, -1, 1, 0),
              (-1, 0, 0, 1)))


def cnt_sections(colors):
    cnt = 0
    for r in range(N):
        for c in range(N):
            if colors[r][c]:
                cnt += 1
                section = colors[r][c]
                stack = [(r, c)]
                colors[r][c] = ""
                while stack:
                    rr, cc = stack.pop()
                    for d in ds:
                        nr, nc = rr+d[0], cc+d[1]
                        if 0 <= nr < N and 0 <= nc < N and colors[nr][nc] == section:
                            stack.append((nr, nc))
                            colors[nr][nc] = ""
    return cnt


N = int(sys.stdin.readline())
RGBs = [[color for color in sys.stdin.readline().rstrip()] for _ in range(N)]
RG_Bs = [["B" if cell == "B" else "RG" for cell in row]for row in RGBs]
print(cnt_sections(RGBs), cnt_sections(RG_Bs))
