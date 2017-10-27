class Trie {
    
    // Node inner class
    class Node {
        public char val;
        public boolean word; 
        public Node[] children = new Node[26];

        public Node() {
            this.val = ' ';
            this.word = false;
        }

        // Constructor to add char
        Node(char c){
            Node node = new Node();
            node.val = c;
        }
    }
    
    private Node root;
    
    /** Initialize your data structure here. */
    public Trie() {
        root = new Node();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        Node node = root;
        // Loop through word
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            // If null, create new node
            // Ascii arithmetic will produce correct index
            if(node.children[c - 'a'] == null){
                node.children[c - 'a'] = new Node(c);
            }
            node = node.children[c - 'a'];
        }
        // Mark it's a word
        node.word = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        Node node = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (node.children[c - 'a'] == null) return false;
            node = node.children[c - 'a'];
        }
        // Takes care of case where word may be a substring but not a word itself
        return node.word;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        Node node = root;
        for (int i = 0; i < prefix.length(); i++) {
            char c = prefix.charAt(i);
            if (node.children[c - 'a'] == null) return false;
            node = node.children[c - 'a'];
        }
        return true;
        // INCORRECT CASE - PREFIX IS A PREFIX OF ITSELF
        // Loop through the remaining node to see if there are any words
        /*for (int i = 0; i < root.children.length; i++) {
            if (root.children[i] != null) return true;
        }
        return false;
        */
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */