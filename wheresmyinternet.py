# Problem statement: https://open.kattis.com/problems/whereismyinternet

class Graph:

	def __init__(self, ver):
		self.V = ver
		self.graph = {}
		for i in range(self.V):
			self.graph[i] = []

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def BFS(self, s):
		visited = [False]*(len(self.graph))
		queue = []
		queue.append(s)
		visited[s] = True
		while queue:
			s = queue.pop(0)
			for i in self.graph[s]:
				if not visited[i]:
					queue.append(i)
					visited[i] = True
		return visited


x = [int(i) for i in input().split()]
n, m = x[0], x[1]
gr = Graph(n)
for i in range(m):
	x = [int(j) for j in input().split()]
	gr.addEdge(x[0]-1, x[1]-1)
	gr.addEdge(x[1]-1, x[0]-1)
x = gr.BFS(0)
y = []
for i in range(n):
	if not x[i]:
		y.append(i+1)
if not y:
	print('Connected')
else:
	for i in y:
		print(i)
