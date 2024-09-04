#-*-coding:utf-8-*-

check_time=0

#Welcome to KSADE!!

import copy
from time import time

class trade():
    def __init__(self, inputList):
        self._len=len(inputList)
        self._name=inputList[0]
        self._class_bef=int(inputList[1])-1
        self._class_aft=[int(inputList[i])-1 for i in range(2,self._len)]   
    
    def __str__(self):
        return "학번 : "+self._name+"\n과목 : "+self._subject+"\n현재분반 : "+str(self._class_bef)+"\n바꿀 분반 : "+str(self._class_aft)
    
    def __repr__(self):
        return self._name

class graph():
    def __init__(self,Graph=[[] for i in range(8)],Cycles=[]):
        self._graph=Graph
        self._cycles=Cycles
        self._newCycles=[]
        self._visited=[False for i in range(8)]
        self._newGraphs=[]
    
    def __str__(self):
        temp=[]
        for i in range(len(self._graph)):
            if self._graph[i]!=[]:
                temp.append(self._graph[i])
        return str(temp)

    def __repr__(self):
        return str(self._cycles)
    
    def add_edge(self,edge_input):
        self._graph[edge_input[1]].append(edge_input)

    def delete_trade(self, trade_input):  #1명이 여러분반에서 못나오잖아 멍청아
        i=trade_input._class_bef
        temp=[]
        for j in self._graph[i]:
            if j[0]._name!=trade_input._name:
                temp.append(j)
            self._graph[i]=temp
        
    def find_cycle(self, edge, visited, path):  #self._newEdge가 포함된 모든 cycle을 검색     #node : int, visited : list, path : list
        node=edge[2]
        visited[node]=3
        
        if len(self._graph[node])==0:
            visited[node]=3
            return None        
        
        for nextEdge in self._graph[node]:     # nextEdge == edge
            path.append(nextEdge)      #그 Node 더함
            
            if visited[nextEdge[2]]==True:               #visited[node]==True, have been before
                self._newCycles.append(path[:])
                
                path.pop()
                
            elif visited[nextEdge[2]]==False:     #visited[node]==False, never been before
                self.find_cycle(nextEdge, visited, path)
                path.pop()
                visited[nextEdge[2]]=3
                
            else:     
                path.pop()
                visited[nextEdge[2]]=3#구현 안해도 되나? 불확실
            
    def findAllCycles(self, edge):
        counter=0
        for i in self._cycles:
            if counter==1:
                break
            for j in i:
                if edge[0]==j[0]:
                    counter=1
                    break
        if counter==1: return [self]
        
        self.add_edge(edge)
        path=[edge]
        self._visited[edge[1]]=True
        self.find_cycle(edge,self._visited,path)
        
        result=[]
        for i in self._newCycles:
            temp=graph(Graph=copy.deepcopy(self._graph),Cycles=copy.deepcopy(self._cycles)+[i])
            for j in i:
                temp.delete_trade(j[0])
            result.append(temp)
        self._visited=[False for i in range(8)]
        self._newCycles=[]
        result.append(self)
        return result
        
              
class Dynamic_Graph():
    def __init__(self):
        self._list=[]    #현재 찾은 모든 cycle(+graph) 종류들의 list
        self._edges=[]
        self._students=[]
        
    def find_matches(self,f,Threshold):
        #f=open(textfile,"r")
        lines=f.readlines()
        for i in range(len(lines)):
            if i!=len(lines)-1:
                lines[i]=lines[i][:-1]        
            inputList=lines[i].split()
            a=trade(inputList)
            for j in a._class_aft:
                temp=[a,a._class_bef,j]
                self._edges.append(temp)
        
        num_students=0
        for i in self._edges:
            if i[0] not in self._students:
                self._students.append(i[0])
                num_students+=1
            if check_time==1:
                start=time()
                print [i[0],i[1]+1,i[2]+1]
            if self._list==[]:
                temp=graph(Graph=[[] for j in range(8)])
                temp.add_edge(i)
                self._list.append(temp)
            else:
                temp=[]
                for j in self._list:
                    new_graphs=j.findAllCycles(i)
                    for k in new_graphs:
                        count=0
                        for Cycle in k._cycles:
                            count+=len(Cycle)
                        if num_students-count<=Threshold:
                            temp.append(k)
                        else:
                            pass
                self._list=temp
            if check_time==1:
                end=time()                
                print end-start
        return self._list
    
    def find_optimal(self):
        if len(self._list)==0:
            print "-------------------Result--------------------"
            print "No such Match"
            return None
        Max=0
        maxGraph=graph()
        for i in self._list:    #i=Graph
            num=0
            for j in i._cycles:    #j=Cycle List
                for k in j:    #k=Cycle component
                    num+=1
            if num>Max:
                Max=num
                maxGraph=i
            elif num==Max:
                if len(maxGraph._cycles)<len(i._cycles):
                    Max=num
                    maxGraph=i                  
        return maxGraph._cycles
         
def main(text_input,Threshold):     
    try:
        f=open(text_input,"r")
    except IOError:
        f.close()
        return "Error"
    except TypeError:
        f.close()
        return "Error"
    else:     
        a=Dynamic_Graph()
        a.find_matches(f,Threshold)
        result=a.find_optimal()
        f.close()
        return result