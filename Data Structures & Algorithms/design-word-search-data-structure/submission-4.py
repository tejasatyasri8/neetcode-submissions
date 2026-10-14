class WordDictionary:

    def __init__(self):
        self.root={}

    def addWord(self, word: str) -> None:
        node=self.root
        for i in range(len(word)):
            if word[i] not in node:
                node[word[i]]={}
            node=node[word[i]]
        node["#"]=True

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i==len(word):
                if "#" in node:
                    return True
                return False
            if(word[i]=="."):
                for ch in node:
                    if ch != "#" and dfs(node[ch], i+1):
                        return True
                return False
            elif(word[i]!="."):
                if word[i] not in node:
                    return False
                return dfs(node[word[i]],i+1)
        
        return dfs(self.root,0)
        

