import networkx as nx
import matplotlib.pyplot as plt
import re

if __name__ == '__main__':
    G = nx.Graph()
    f = open('res.txt','r')
    cnt = 0
    prev = None
    for line in f.readlines():
        if line.find('END') != -1:
            prev = None
            cnt+=1
            print(cnt)
            continue
        result = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
        if result:
            if prev is None:
                prev = result[0]
            else:
                G.add_edge(prev,result[0])
                prev = result[0]
                # nx.draw_networkx(G,pos,node_size=sizes) 
    dd = nx.degree(G)
    d = {}
    for i in dd:
        d[i[0]] = i[1]
    nx.draw(G, nodelist=d.keys(), node_size=[v * 2 for v in d.values()])
    # nx.draw_networkx(G,node_size=2,with_labels=False)
    plt.show() 
    plt.savefig('res.png')
    # nx.draw(G)
    # plt.show()
    # f.close()