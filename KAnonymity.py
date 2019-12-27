# encoding: gbk

from MyTree import *
import datetime
import time
cluster = []

def findcluster(one):
    if len(cluster) == 0:
        return -1
    for i in range(0, len(cluster)):
        temp = cluster[i][0]
        if temp[0] == one[0] and temp[1] == one[1] and temp[2] == one[2] and temp[3] == one[3]:
            return i
    return -1

file = open("adult.data","r")
line = file.readline()

while line:
    #print line
    line = line[:-1]
    if line == "":
        break
    content = line.split(", ")

    newcontent = []
    qidcontent = []
    qidcontent.append(content[3])
    qidcontent.append(content[4])
    qidcontent.append(content[8])
    qidcontent.append(content[13])
    for i in range(0, len(content)):
        if i == 2 or i == 3 or i == 4 or i == 8 or i == 13:
            continue;
        else:
            newcontent.append(content[i])
 #   print newcontent
    index = findcluster(qidcontent)
    if index == -1:
        cluster.append([qidcontent])
        cluster[len(cluster)-1].append(newcontent)
    else:
        cluster[index].append(newcontent)
    line = file.readline()

# for i in range(0,len(cluster[0])):
#     print(cluster[0][i])
# for i in range(0,len(cluster[1])):
#     print(cluster[1][i])
# print(len(cluster[0]))
# for i in range(0,len(cluster)):
#     print(len(cluster[i]))
# print(cluster[0][0][0])
# 初始化分类树
# 四棵树分别是educationTree,educationNumTree,raceTree,nativeCountryTree
treeList=buildTree()
# print(cluster[0][0])
# raceDistance,racePublicNode=treeList[2].distanceAndFirstPublicNode(cluster[0][0][2],cluster[0][0][2])
# print(raceDistance)
# print(racePublicNode)
# 开始扰动
K=int(input('输入K匿名标准K：'))
startTime=datetime.datetime.now()
flag=False
while flag==False:
    for i in range(0,len(cluster)):
        if len(cluster[i])-1>=K:
            flag=True
            continue
        else:
            flag=False
            # minDistance存储最小距离，minJ存储最小距离的元组
            minDistance=100
            minIndex=0
            for j in range(0,len(cluster)):
                if i==j:
                    continue

                # print('=========================')
                # print(cluster[j][0][2])
                educationDistance,edcationPublicNode=treeList[0].distanceAndFirstPublicNode(cluster[i][0][0],cluster[j][0][0])
                educationNumDistance,edcationNumPublicNode=treeList[1].distanceAndFirstPublicNode(cluster[i][0][1],cluster[j][0][1])
                raceDistance,racePublicNode=treeList[2].distanceAndFirstPublicNode(cluster[i][0][2],cluster[j][0][2])
                nativeCountryDistance,nativeCountryPublicNode=treeList[3].distanceAndFirstPublicNode(cluster[i][0][3],cluster[j][0][3])
                if minDistance>=(educationDistance+educationNumDistance+raceDistance+nativeCountryDistance):
                    minDistance=(educationDistance+educationNumDistance+raceDistance+nativeCountryDistance)
                    minIndex=j
                    generalizationEducation=edcationPublicNode.identifier
                    generalizationEducationNum=edcationNumPublicNode.identifier
                    generalizationRace=racePublicNode.identifier
                    generalizationNativeCountry=nativeCountryPublicNode.identifier
            print(minIndex)
            cluster[i][0][0] = generalizationEducation
            cluster[i][0][1] = generalizationEducationNum
            cluster[i][0][2] = generalizationRace
            cluster[i][0][3] = generalizationNativeCountry
            # for k in range(0,len(cluster[i])):
            #     cluster[i][k][0]=generalizationEducation
            #     cluster[i][k][1]=generalizationEducationNum
            #     cluster[i][k][2]=generalizationRace
            #     cluster[i][k][3]=generalizationNativeCountry
            for k in range(1,len(cluster[minIndex])):
                # cluster[minIndex][k][0]=generalizationEducation
                # cluster[minIndex][k][1]=generalizationEducationNum
                # cluster[minIndex][k][2]=generalizationRace
                # cluster[minIndex][k][3]=generalizationNativeCountry
                cluster[i].append(cluster[minIndex][k])
            del cluster[minIndex]
            break
endTime=datetime.datetime.now()
print('扰动时间为:'+str(endTime-startTime))
resultFile=open('result_'+str(K),'w')
#写入文件
for k in range(0,len(cluster)):
    qidstr = ''
    for l in range(0, len(cluster[k][0])):
        qidstr += cluster[k][0][l] + ','
    for l in range(1,len(cluster[k])):
        # resultFile.writelines(cluster[k][l])
        # resultFile.write('\n')
        singleLine = qidstr
        for m in range(0,len(cluster[k][l])):
            singleLine += str(cluster[k][l][m])+','
        singleLine = singleLine[:-1]
        singleLine += '\n'
        # print(singleLine)
        resultFile.write(singleLine)
resultFile.close()
# 计算NCP
NCPValue=0
allNum=0
for k in range(0,len(cluster)):
    oneNCPValue = 0
    educationNCP = treeList[0].subtree(cluster[k][0][0]).size() / 16.0
    raceNCP = treeList[2].subtree(cluster[k][0][2]).size() / 5.0
    nativeCountryNCP = treeList[3].subtree(cluster[k][0][3]).size() / 42.0
    educationNumNCP = len(treeList[1].leaves(cluster[k][0][1])) / 16.0
    oneNCPValue += educationNCP + educationNumNCP + raceNCP + nativeCountryNCP
    oneNCPValue *= (len(cluster[k])-1)
    NCPValue += oneNCPValue
    allNum += len(cluster[k])-1
    # for l in range(0,len(cluster[k])):
    #     allNum+=1
    #     educationNCP=treeList[0].subtree(cluster[k][l][0]).size()/16
    #     raceNCP=treeList[2].subtree(cluster[k][l][2]).size()/5
    #     nativeCountryNCP=treeList[3].subtree(cluster[k][l][3]).size()/42
    #     educationNumNCP=len(treeList[1].leaves(cluster[k][l][1]))/16
    #     NCPValue+=educationNCP+educationNumNCP+raceNCP+nativeCountryNCP
print('NCP:'+ str(NCPValue))
# print(allNum)
print('GCP:'+ str(NCPValue/(allNum*4.0)))

            