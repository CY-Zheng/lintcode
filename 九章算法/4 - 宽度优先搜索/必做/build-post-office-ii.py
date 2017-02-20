class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # Write your code here
        # �жϵ�ǰ�ڵ��ǲ���û�߹���empty�ڵ�
        def isVaild(grid, r, c, row, col, visited):
            if r >= 0 and r < row and c >= 0 and c < col \
                    and grid[r][c] == 0 and (not visited[r][c]):
                return True            
            return False 
            
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        nbrow = [1, -1, 0, 0]
        nbcol = [0, 0, 1, -1]
        empty, wall, house, distance = self.initialize(grid, row, col)
        for h in house: #����ÿ������BFS
            jump = -1 
            queue = [h]
            # visited distance�ȸ������飬Ҫʹ����ԭʼ������
            # ��ÿ��Ԫ�ض�Ӧһ�����ӣ���������ݣ������Ǵ�����±꣩
            # ����Ҫ��in��ѯ�����Ӹ��Ӷȣ�
            visited = [[False for c in range(col)] for r in range(row)]
            while queue:
                jump += 1
                size = len(queue)
                for s in range(size):
                    node = queue.pop(0)
                    if grid[node[0]][node[1]] == 0:
                        distance[node[0]][node[1]] += jump
                    for i in range(4):
                        nx = node[0] + nbrow[i]
                        ny = node[1] + nbcol[i]
                        if isVaild(grid, nx, ny, row, col, visited):
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            for i in range(row):
                for j in range(col):
                    if not visited[i][j]:
                        # ���統ǰempty������һ�������޷�����
                        # ��ô�Ժ��ʾֲ�����ѡ�������棬·��Ҳ����ͨ����
                        # ���Ϊǽ���Ժ���Ҫ̽��
                        grid[i][j] = 2
                        distance[i][j] = 99999
        result = min([min(l) for l in distance])
        return result if result != 99999 else -1
             
    def initialize(self, grid, row, col):
        empty = []
        wall = []
        house = []
        distance = [[0 for c in range(col)] for r in range(row)]
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    house.append((r, c))
                elif grid[r][c] == 2:
                    wall.append((r, c))
                else:
                    empty.append((r, c))
        for r, c in wall:
            distance[r][c] = 99999
        for r, c in house:
            distance[r][c] = 99999  
        return empty, wall, house, distance