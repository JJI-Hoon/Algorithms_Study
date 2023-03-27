import copy

# 특정 기준에서 부터 Index 방향들 뽑아내는 방법 (방향만 고려하여 같은 도형을 선별하는 방법)
def dfs(graph, x, y, position, n, num):
    dic = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0,-1]}
    
    ret = [position]
    
    for i in range(4):
        nx = x + dic[i][0]
        ny = y + dic[i][1]
        
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == num:
            graph[nx][ny] = 2
            ret = ret + dfs(graph, nx, ny, [position[0] + dict[i][0], position[1] + dic[i][1], n, num])
            
    return ret

def rotate(lst):
    n = len(lst)
    
    ret = [[0] * n for _ in range(n)]
    
    # TODO 회전 방법 (시계 방향) -> 공부 필요
    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = lst[i][j]
            
    return ret

def solution(game_board, table):
    answer = 0
    game_board_copy = copy.deepcopy(game_board)
    
    n = len(game_board)
    block = []
    
    # 넣어야 할 도형 별 인덱스를 list로 뽑아서 배열로 넣음
    for i in range(n):
        for j in range(n):
            if game_board_copy[i][j] == 0:
                game_board_copy[i][j] = 2
                result = dfs(game_board_copy, i, j, [0,0], n, 0)[1:]

    # 회전을 4번 하면서 갖고 있는 도형의 방향 Index 다 뽑아냄
    # 그리고, 기존의 맞춰야하는 위의 Result안의 리스트와 비교하면서 있으면 값 더해주기
    for r in range(4):
        table = rotate(table)
        table_rotate_copy = copy.deepcopy(table)
        
        for i in range(n):
            for j in range(n):
                if table_rotate_copy[i][j] == 1:
                    table_rotate_copy[i][j] = 2
                    result = dfs(table_rotate_copy, i, j, [0, 0], n, 1)[1:]
                    # 어짜피 하나의 도형만 나오기 때문에
                    if result in block:
                        block.pop(block.index(result))
                        # 총 칸 수 구해야하기 때문에 기존의 시작점은 리스트에 없어서 +1 해주기
                        answer += (len(result) + 1)
                        
                        table = copy.deepcopy(table_rotate_copy)
                    
                    else:
                        table_rotate_copy = copy.deepcopy(table)
                        
    return answer

