class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build trie from all words
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        results = set()
        rows, cols = len(board), len(board[0])
        
        def dfs(row, col, node, path):
            ch = board[row][col]
            if ch not in node.children:
                return  # No word has this prefix — stop early
            
            node = node.children[ch]
            path.append(ch)
            
            # If this path completes a word, record it
            if node.is_end:
                results.add(''.join(path))
                node.is_end = False  # Prevent duplicate collection
            
            # Mark as visited
            board[row][col] = '#'
            
            # Explore neighbors
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, node, path)
            
            # Unmark (backtrack)
            board[row][col] = ch
            path.pop()
        
        # Start DFS from every cell
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie.root, [])
        
        return list(results)