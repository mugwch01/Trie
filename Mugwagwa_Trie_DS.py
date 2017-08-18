#My name is Charles Mugwagwa. This is an implementation of a Trie data structure.

class Trie:
    def __init__(self):
        self.start = None    
        
    def insert(self, item):
        self.start = Trie.__insert(self.start, item+"$")
    
    def __contains__(self,item):
        return Trie.__contains(self.start,item+"$")
        
    #using this function because the node can be None and recursion on self complicated
    def __insert(node,item):        
        if item == "":
            return None       
        if node == None:            
            node = Trie.TrieNode(item[0])
            node.follows = Trie.__insert(node.follows,item[1:])  
        elif item[0] == node.item:
            node.follows = Trie.__insert(node.follows, item[1:])
        else:
            node.next = Trie.__insert(node.next, item)
        return node
    
    def __contains(node,item):        
        if node == None:
            return False
        elif item[0] == node.item:
            if node.item == "$" and len(item) == 1:
                return True
            return Trie.__contains(node.follows,item[1:])
        elif item[0] != node.item:
            if node.next != None:
                return Trie.__contains(node.next,item)
            else:
                return False        
    
    class TrieNode:
        def __init__(self,item,next = None, follows = None):
            self.item = item
            self.next = next
            self.follows = follows
        
def main():
    trie = Trie()
    file = open('wordsEn.txt','r')
    for line in file:
        line = line[:-1]        
        trie.insert(line)
    file.close()
    
    file = open('declaration_of_independence.txt','r')              
    lineCount = sum(1 for line in file) #includes blank lines   
    file.seek(0) 
    for t in range(lineCount):
        line = file.readline()
        if line != "":
            splitLine = line.split()            
            for word in splitLine:                
                if word[-1]==',' or word[-1]=='.' or word[-1]==';' or word[-1]==':':
                    word = word[:-1]
                word = word.lower()              
                if word not in trie:
                    print(word)    

if __name__ == '__main__':
    main()