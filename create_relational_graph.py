#----
# OK
#-----

import networkx as nx

G_following=nx.read_edgelist("Users_Following.txt")
G_follower=nx.read_edgelist("Users_Follower.txt")
#-------------------
# Integration of Following and Followers   ------into---> G_following
#--------------------------
# fp1=open()
for edge in G_follower.edges:
    if (G_following.has_edge(edge[0],edge[1])):
        print('Duplicate edge')
    else:
        G_following.add_edge(edge[0],edge[1])
        print(edge)

#-----------
# shortest_path AS relation_score
#-----
dic_relation_score={}
lst_all_edges=list()
for node1 in G_following.nodes:
    for node2 in G_following.nodes:

        edge_inverse=node2 + '_' + node1
        edge_new = node1 + '_' + node2    # asli
        if (edge_new in lst_all_edges):
            continue
        lst_all_edges.append(edge_new)

        if (edge_inverse in lst_all_edges):
            continue
        lst_all_edges.append(edge_inverse)


        try:
            dic_relation_score[edge_new]=1/(len(nx.shortest_path(G_following,node1,node2)))
        except:
            dic_relation_score[edge_new]=0


#----
# write to file
#----
import os
try:
    os.remove('relation_graph.txt')
except:
    print('there is no file relation_graph.txt')

fp=open('relation_graph.txt','a',encoding='utf8')
for item in dic_relation_score:
    fp.write(item+'---->'+str(dic_relation_score[item])+'\n')
fp.close()


#-----------------------------------------------

# import matplotlib.pyplot as plt
# nx.draw(G)
# plt.draw()  # pyplot draw()