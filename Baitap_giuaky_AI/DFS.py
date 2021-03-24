#Tạo danh sách nodes
nodes = ('Arad','Bucharest','Craiova','Drobeta'
            ,'Eforie','Fagaras','Giurgiu','Hirsova','Iasi'
            ,'Lugoj','Mehadia','Neamt','Oraden','Pitesti',
            'Rimnicu Vilcea','Sibiu','Timisoara','Urziceni',
            'Vaslui','Zenrid')
#distances liện kết
graph1 = {
    'Arad': {'Zenrid': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Bucharest':{'Pitesti':101,'Fagaras':211,'Urziceni':85,'Giurgiu':90},
    'Craiova':{'Rimnicu Vilcea':146,'Drobeta':120,'Pitesti':138},
    'Drobeta':{'Mehadia':75,'Craiova':120},
    'Eforie':{'Hirsova':86},
    'Fagaras':{'Sibiu':99,'Bucharest':211},
    'Giurgiu':{'Bucharest':90},
    'Hirsova':{'Urziceni':98,'Eforie':86},
    'Iasi':{'Neamt':87,'Vaslui':92},
    'Lugoj':{'Timisoara':111,'Mehadia':70},
    'Mehadia':{'Lugoj':70,'Drobeta':75},
    'Neamt':{'Iasi':87},
    'Oraden':{'Zenrid':71,'Sibiu':151},
    'Pitesti':{'Rimnicu Vilcea':97,'Craiova':138,'Bucharest':101},
    'Rimnicu Vilcea':{'Sibiu':80,'Pitesti':97,'Craiova':146},
    'Sibiu':{'Oraden':151,'Arad':140,'Fagaras':99,'Rimnicu Vilcea':80},
    'Timisoara':{'Lugoj':111,'Arad':118},
    'Urziceni':{'Bucharest':85,'Vaslui':142,'Hirsova':98},
    'Vaslui':{'Iasi':92,'Urziceni':142},
    'Zenrid':{'Arad':75,'Oraden':71}
    }
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited

visited = dfs(graph1,'Oraden', [])
count = 0
for n in visited:
    if n == 'Zenrid' :
        diembatdau = count + 1
    if n == 'Bucharest' :
        diemketthuc = count
    count+=1
print('Đường đi từ Zenrid tới Bucharest bằng DFS :')
print(visited[diembatdau-1],end='')
while diembatdau <= diemketthuc :
    print(' -> '+visited[diembatdau],end='')
    diembatdau+=1