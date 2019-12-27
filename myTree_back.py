from treelib import Tree,Node

class myTree(Tree):
    def distanceAndFirstPublicNode(self,node1,node2):
        depth=self.depth()
        depthNode1=self.depth(node1)
        depthNode2=self.depth(node2)
        # return depth,depthNode1,depthNode2
        if depthNode1>=depthNode2:
            deep=depthNode1
            shallow=depthNode2
            deeperNode=self.get_node(node1)
            shallowerNode=self.get_node(node2)
            # deeperNode=node1
            # shallowerNode=node2
        else:
            deep=depthNode2
            shallow=depthNode1
            # deeperNode=node2
            # shallowerNode=node1
            deeperNode=self.get_node(node2)
            shallowerNode=self.get_node(node2)
        dif=deep-shallow
        tmpNode=deeperNode
        for i in range(0,dif):
            # tmpNode.identifier获取节点的nid，也就是唯一标识符
            tmpNode=self.parent(tmpNode.identifier)
        deeperNode=tmpNode
        while deeperNode.identifier!=shallowerNode.identifier:
            dif+=2
            deeperNode=self.parent(deeperNode.identifier)
            shallowerNode=self.parent(shallowerNode.identifier)
        return dif,deeperNode




# QID中4个属性，所以有4棵分类树
educationTree=myTree()
educationNumTree=myTree()
raceTree=myTree()
nativeCountryTree=myTree()


file=open('ClassificationTreeValue','r')
lines=file.readlines()
file.close()
# 去除每行最后的\n，并且构造分类树
for i in range(0,len(lines)):
    lines[i]=lines[i][:-1]
    if lines[i].count(':')==0:
        if lines[i]=='education':
            T=educationTree
        elif lines[i]=='education_num':
            T=educationNumTree
        elif lines[i]=='race':
            T=raceTree
        else:
            T=nativeCountryTree
        continue
    nodes=lines[i].split(':')
    if nodes[1]=='*':
        T.create_node(nodes[1],nodes[1])
    else:
        T.create_node(nodes[1],nodes[1],nodes[0])





# educationNumTree.create_node('*','*')
# educationNumTree.create_node('<=8','<=8','*')
# educationNumTree.create_node('>8','>8','*')
# educationNumTree.create_node('1','1','<=8')
# educationNumTree.create_node('2','2','<=8')
# educationNumTree.create_node('3','3','<=8')
# educationNumTree.create_node('4','4','<=8')
# educationNumTree.create_node('5','5','<=8')
# educationNumTree.create_node('6','6','<=8')
# educationNumTree.create_node('7','7','<=8')
# educationNumTree.create_node('8','8','<=8')
# educationNumTree.create_node('9','9','>8')
# educationNumTree.create_node('10','10','>8')
# educationNumTree.create_node('11','11','>8')
# educationNumTree.create_node('12','12','>8')
# educationNumTree.create_node('13','13','>8')
# educationNumTree.create_node('14','14','>8')
# educationNumTree.create_node('15','15','>8')
# educationNumTree.create_node('16','16','>8')
# educationNumTree.show()

# print(educationNumTree.parent('1'))

educationNumTree.show()
dif,publicNode=educationNumTree.distanceAndFirstPublicNode('1','>8')
print(dif)
print(publicNode)
print('========')
educationTree.show()
dif,publicNode=educationTree.distanceAndFirstPublicNode('HS-grad','1st-4th')
print(dif)
print(publicNode)