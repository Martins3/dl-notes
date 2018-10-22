import networkx as nx
import os
import matplotlib.pyplot as plt
import re
G = nx.MultiDiGraph()

to_dir = "/home/martin/X-Brain/Tianchi"
fname = os.path.join(to_dir, "new_link_top")
a = os.path.exists(fname)

# 使用 skip 的 原因是为了跳过第一行的数据
def create():
    skip = True
    with open(fname) as f:
        for line in f:
            if(skip):
                skip = False
                continue
            line = re.sub('\n', '', line)
            nodes = line.split(';')
            node = nodes[0]
            in_node = nodes[1].split('#')
            out_node = nodes[2].split('#')

            # add in_node
            for i in in_node:
                if(i==''):
                    continue
                G.add_edge(i, node)

            for i in out_node:
                if(i==''):
                    continue
                G.add_edge(node, i)
    return G
            # add out_node

def draw_graph():
    G = create()
    nx.draw(G, with_labels=True)
    plt.savefig('links.png', dpi=200)
