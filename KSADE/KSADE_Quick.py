#-*-coding:utf-8-*-

#Welcome to KSADE!!
#################### User Input #######################

#text_input="Trade_test.txt"   #불러올 .txt 파일 이름
#text_input="cpdbr2.txt"

#여기는 input 순서대로만 판단하기 때문에 결과 도출이 빠른 대신 몇명이 빠진, optimal 하지 않은 결과가 나올 수 있음
                   
#######################################################
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
    def __init__(self):
        self._graph=[[] for i in range(8)]
        self._subgraph=[]

    def __str__(self):
        return str(self._graph)
        
    def add_trade(self, trade_input):       #각 Node는 [trade object, 이전 분반, 가고싶은 분반], 숫자는 다 int
        for i in trade_input._class_aft:
            self._graph[int(trade_input._class_bef)].append([trade_input,trade_input._class_bef,i])
    
    def delete_trade(self, trade_input):  #1명이 여러분반에서 못나오잖아 멍청아
        i=trade_input._class_bef
        temp=[]
        for j in self._graph[i]:
            if j[0]._name!=trade_input._name:
                temp.append(j)
            self._graph[i]=temp
        
    def find_match(self, node, visited, path):  #node : int, visited : list, path : list
        visited[node]=True
        
        if len(self._graph[node])==0:
            visited[node]=False
            return None        
        
        for neighbour in self._graph[node]:     #neighbour == edge
            path.append(neighbour)      #그 Node 더함
            
            if visited[neighbour[2]]==True:               #visited[node]==True, have been before
                result=[]
                intersection=neighbour[2]
                for i in range(len(path)-1,-1,-1):        #path에서 겹치는 두 Node 및 그 사이 사이클 탐색
                    a=path[i]
                    result.append(a)
                    if a[1]==intersection:
                        break
                for i in range(len(result)/2):
                    result[i],result[len(result)-1-i]=result[len(result)-1-i],result[i]
                return result            
            
            elif visited[neighbour[2]]==False:     #visited[node]==False, never been before
                temp=self.find_match(neighbour[2], visited, path)
                if temp==None:
                    path.pop()
                    visited[neighbour[2]]=2
                    continue
                else:
                    visited[node]=False
                    return temp
        visited[node]=False
        return None
    
    def find_all_match(self):   #반 번호에+1 해주는거 구현해야함
        result=[]
        
        while True:
            counter=0
            visited=[False for i in range(8)]      #여기서 visited랑 path 언제 초기화해야 하는지 불확
            path=[]                                  
            
            for i in range(len(self._graph)):              #각 반(vertex)  
                temp=self.find_match(i,visited,path)
                if temp==None:
                    continue
                else:
                    result.append(temp)
                    for i in temp:
                        self.delete_trade(i[0])
                    counter=1
                    break
                
                visited[i]=2
            
            if counter==0:
                break
            
        for i in result:
            for j in range(len(i)):
                i[j][1]+=1
                i[j][2]+=1

        return result

def main(text_input):
    try:
        f=open(text_input,"r")
    except IOError:
        f.close()
        return "Error"
    except TypeError:
        f.close()
        return "Error"
    else:            
        lines=f.readlines()
        Graph=graph()
        for i in lines:
            i=i[:-1]
            inputList=i.split()
            Graph.add_trade(trade(inputList))
        a=Graph.find_all_match()
        #print "-------------------Result--------------------"
        #for i in a:
            #print i
        f.close()
        return a

#main()