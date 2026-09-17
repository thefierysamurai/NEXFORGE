import json,networkx as nx
from pathlib import Path
DATA=json.loads((Path(__file__).resolve().parents[1]/'data/network.json').read_text())
G=nx.Graph();G.add_nodes_from((n['id'],n) for n in DATA['nodes']);G.add_edges_from((e['source'],e['target']) for e in DATA['edges'])
b=nx.betweenness_centrality(G);d=nx.degree_centrality(G)
for n in DATA['nodes']:
 n['calculated_centrality']=round(b[n['id']],3);n['criticality']=max(n['criticality'],round(min(99,35+b[n['id']]*120+d[n['id']]*30)))
def get_node(i):return next((n for n in DATA['nodes'] if n['id']==i),None)
def payload():return {'nodes':DATA['nodes'],'edges':DATA['edges']}
def overview():return {'assets':len(DATA['nodes']),'edges':len(DATA['edges']),'critical_assets':sum(n['criticality']>=80 for n in DATA['nodes']),'exposure':31}
