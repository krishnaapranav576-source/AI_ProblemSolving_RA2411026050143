from flask import Flask, render_template, request

app = Flask(__name__)

# Sample graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# BFS Algorithm
def bfs(start, goal):
    visited = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            visited.append(node)

            if node == goal:
                return path, visited

            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

    return None, visited


# DFS Algorithm
def dfs(start, goal):
    visited = []
    stack = [[start]]

    while stack:
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            visited.append(node)

            if node == goal:
                return path, visited

            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                stack.append(new_path)

    return None, visited


@app.route("/", methods=["GET", "POST"])
def home():
    bfs_path = None
    bfs_visited = None
    dfs_path = None
    dfs_visited = None

    if request.method == "POST":
        start = request.form["start"].upper()
        goal = request.form["goal"].upper()

        if start in graph and goal in graph:
            bfs_path, bfs_visited = bfs(start, goal)
            dfs_path, dfs_visited = dfs(start, goal)

    return render_template(
        "index.html",
        bfs_path=bfs_path,
        bfs_visited=bfs_visited,
        dfs_path=dfs_path,
        dfs_visited=dfs_visited
    )


if __name__ == "__main__":
    app.run(debug=True)