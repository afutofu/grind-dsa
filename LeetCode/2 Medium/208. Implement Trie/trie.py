class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root

        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]

        cur["*"] = ""

    def search(self, word: str) -> bool:
        cur = self.root

        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]

        return "*" in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]

        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # True
    print(trie.search("app"))  # False
    print(trie.startsWith("app"))  # True
    trie.insert("app")
    print(trie.search("app"))  # True
