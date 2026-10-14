class PrefixTree:

    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        node=self.root
        for i in range(len(word)):
            if word[i] not in node:
                node[word[i]] = {}
            node = node[word[i]]
        node["#"]=True

    def search(self, word: str) -> bool:
        node=self.root
        for i in range(len(word)):
            if word[i] in node:
                node = node[word[i]]
            else:
                return False
        if '#' in node:
            return True
        return False
            

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for i in range(len(prefix)):
            if prefix[i] in node:
                node = node[prefix[i]]
            else:
                return False
        return True
        