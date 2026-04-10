#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

#define pb push_back
#define endl '\n'

// TRIE NODE
struct trie_node {
   int pc; // prefix count
   trie_node *child[26];
   bool isend; // word ends here or not
   
   trie_node() {
       pc = 0;
       isend = false;
       for(ll i = 0; i < 26; i++){
          child[i] = NULL;
       }
   }
};

trie_node* root = new trie_node();

// INSERT FUNCTION
void insert(string s) {
  trie_node* curr = root;
  for(auto c : s) {
    c = tolower(c);
    ll index = c - 'a';
    
    if(index < 0 || index > 25) continue;
    
    if(curr->child[index] == NULL) {
        curr->child[index] = new trie_node();
    } 
    curr = curr->child[index];
    curr->pc++;
  }  
  curr->isend = true;
}

// CHECK IF NODE HAS NO CHILDREN
bool isLastNode(trie_node* curr) {
    for (int i = 0; i < 26; i++) {
        if (curr->child[i] != NULL)
            return false; // has at least one child
    }
    return true; // no children
}

// DFS FOR SUGGESTIONS
void dfs(trie_node* curr, string prefix) {
    // found a string in Trie with the given prefix
    if (curr->isend) {
        cout << prefix << endl;
    }

    // All children node pointers are NULL
    if (isLastNode(curr)) {
        return;
    }

    for (ll i = 0; i < 26; i++) {
        if (curr->child[i] != NULL) {
            // Append character and recurse (passed by value to prevent sibling bugs)
            dfs(curr->child[i], prefix + (char)('a' + i));
        }
    }
}

// AUTOCOMPLETE LOGIC FROM YOUR PROVIDED CODE
int auto_complete(string query) {
    trie_node* curr = root;
    
    // Check if prefix is present
    for (auto c : query) {
        c = tolower(c);
        ll index = c - 'a';
        
        if (index < 0 || index > 25) continue;

        // No string in the Trie has this prefix
        if (curr->child[index] == NULL) {
            return 0; 
        }
        curr = curr->child[index];
    }

    // If prefix is present as a word.
    bool isWord = curr->isend;

    // If prefix is last node of tree (has no children)
    bool isLast = isLastNode(curr);

    // If prefix is present as a word, but there is no subtree
    if (isWord && isLast) {
        cout << query << endl;
        return -1;
    }

    // If there are nodes below last matching character
    if (!isLast) {
        dfs(curr, query);
        return 1;
    }
    
    return 0;
}

// DRIVER CODE
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    insert("hello");
    insert("dog");
    insert("hell");
    insert("cat");
    insert("a");
    insert("hel");
    insert("help");
    insert("helps");
    insert("helping");

    cout << "Suggestions for 'hel':\n";
    int comp = auto_complete("hel");

    if (comp == -1) 
        cout << "No other strings found with this prefix\n"; 
    else if (comp == 0) 
        cout << "No string found with this prefix\n"; 
        
    cout << "\nSuggestions for 'hello':\n";
    int comp2 = auto_complete("hello");

    if (comp2 == -1) 
        cout << "No other strings found with this prefix\n"; 
    else if (comp2 == 0) 
        cout << "No string found with this prefix\n"; 

    return 0;
}
