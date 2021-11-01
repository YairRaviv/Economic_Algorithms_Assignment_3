import random
from typing import List

def findAlmostEnvyFree(agents:List[OrdinalAgent], totalRent:int):
    All_Posible_Partitions = []
    for i in range (0,totalRent+1):
        tmp = totalRent-i
        for j in range (0,tmp+1):
            k = totalRent - i - j
            All_Posible_Partitions.append([i,j,k])
    for partition in All_Posible_Partitions:
        index_0 = agents[0].bestRoom(partition)
        index_1 = agents[1].bestRoom(partition)
        index_2 = agents[2].bestRoom(partition)
        if index_0 != index_1 and index_0 != index_2 and index_1 != index_2:
            print(f'Agent 0 receives room {index_0} for {partition[0]} shekels.')
            print(f'Agent 1 receives room {index_1} for {partition[1]} shekels.')
            print(f'Agent 2 receives room {index_2} for {partition[2]} shekels.')
            # print("Agent 0 receives room " + index_0 + " for " + partition[0] + " shekels.")
            # print("Agent 1 receives room " + index_1 + " for " + partition[1] + " shekels.")
            # print("Agent 2 receives room " + index_2 + " for " + partition[2] + " shekels.")
            return 0
