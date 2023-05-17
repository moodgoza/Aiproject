import tkinter as tk
from tkinter import messagebox

class DFS_GUI:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()

        self.root = tk.Tk()
        self.root.title("DFS Algorithm")

        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

        self.btn_dfs = tk.Button(self.root, text="Start DFS", command=self.start_dfs)
        self.btn_dfs.pack()

    def draw_node(self, node, color):
        x = 50 + node[0] * 100
        y = 50 + node[1] * 100
        self.canvas.create_oval(x-20, y-20, x+20, y+20, fill=color)
        self.canvas.create_text(x, y, text=node)

    def draw_edge(self, node1, node2, color):
        x1 = 50 + node1[0] * 100
        y1 = 50 + node1[1] * 100
        x2 = 50 + node2[0] * 100
        y2 = 50 + node2[1] * 100
        self.canvas.create_line(x1, y1, x2, y2, fill=color)

    def draw_graph(self):
        for node in self.graph:
            self.draw_node(node, "white")
            for neighbor in self.graph[node]:
                self.draw_edge(node, neighbor, "black")

    def start_dfs(self):
        self.visited.clear()
        self.canvas.delete("all")

        self.draw_graph()
        self.root.update()  # Update the GUI to display the entire graph

        start_node = (0, 0)
        self.dfs(start_node)

        messagebox.showinfo("DFS Complete", "DFS traversal finished!")

    def dfs(self, node):
        self.visited.add(node)
        self.draw_node(node, "green")
        self.root.update()  # Update the GUI to reflect changes

        self.root.after(1000)  # Delay for one second (1000 milliseconds)

        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.draw_edge(node, neighbor, "blue")
                self.draw_node(node, "yellow")
                self.root.after(1000)
                self.dfs(neighbor)

        self.draw_node(node, "red")
        self.root.after(1000)
        self.root.update()  # Update the GUI to reflect changes

if __name__ == "__main__":
    graph = {
        (0, 0): [(1, 0), (0, 1), (1, 1)],
        (1, 0): [(2, 0)],
        (0, 1): [(0, 2)],
        (0, 2): [(1, 2)],
        (1, 1): [],
        (2, 0): [(2, 1), (3, 1)],
        (1, 2): [],
        (2, 1): [],
        (3, 1): [(3, 2)],
        (3, 2): [(3, 3)],
        (3, 3): [],
    }

    dfs_gui = DFS_GUI(graph)
    dfs_gui.root.mainloop()