import random

edges = []
with open("input.txt", "r") as file:
	for line in file:
		edges.append(line.strip().split(" -> "))

def get_adjacent_edges(pos, edges):
	choices = []
	for edge in edges:
		if pos == edge[0]:
			choices.append(edge[1])
	return choices

split_edges = []
for edge in edges:
	if len(edge[1]) > 1:
		split = edge[1].split(',')
		for item in split:
			split_edges.append([edge[0], item])
	else:
		split_edges.append([edge[0], edge[1]])

split_edges = [list(map(int, x)) for x in split_edges]

stack = []
circuit = []
pos = random.choice([x[1] for x in split_edges])
while len(split_edges) > 0:
	choices = get_adjacent_edges(pos, split_edges)
	while choices == []:
		circuit.append(pos)
		pos = stack.pop()
		choices = get_adjacent_edges(pos, split_edges)
	stack.append(pos)
	pos = random.choice(choices)
	split_edges.remove([stack[-1], pos])
stack.append(pos)

while len(stack) > 0:
	circuit.append(stack.pop())

circuit = list(map(str, circuit))
output = open('output.txt', 'w')
output.write('->'.join(circuit[::-1]))