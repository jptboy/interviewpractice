#include <iostream>
#include <functional>
#include <cstring>
#include <fstream>
#include <vector>
#include <stack>
using namespace std;

class Node
{
    public:
        Node(char letter) : letter(letter),
                            children(new Node*[26]),
                            isleaf(false)
        {
            memset((void*)children,0,sizeof(Node*)*26);
        };
        Node() : children(new Node*[26]),
                 isleaf(false)
        {
            memset((void*)children,0,sizeof(Node*)*26);
        };
        Node** children;
        bool isleaf;
        int count;
        char letter;
        ~Node()
        {
            delete[] children;
        }
};
class Trie
{
    public:
        Trie()
        {
            root = new Node('*');
            root->isleaf = false;
            root->count = 1;
        };
        Node* root;
        void fromVec(vector<string>& words)
        {
            for (auto& s: words)
            {
                insertWord(s);
            }
        }
        void insertWord(string word)
        {
            if (search(word)) return;
            Node* crawl = root;
            auto len = word.length();
            for (int i = 0; i < len; ++i)
            {
                char c = word[i];
                bool flag = false;
                flag = i == len - 1;
                if (!(crawl->children[c - 'a']))
                {
                    crawl->children[c-'a'] = new Node;
                    if (flag) crawl->children[c-'a']->isleaf = true;
                    crawl->children[c-'a']->count = 1;
                    crawl->children[c-'a']->letter = c;
                }
                else
                {
                    crawl->children[c-'a']->count++;
                    if (flag) crawl->children[c-'a']->isleaf = true;
                }
                crawl = crawl->children[c-'a'];
            }
        }
        bool deleteWord(string word)
        {
            if (!search(word)) return false;
            auto len = word.length();
            function<Node*(Node*, string, int)> helper = [&](Node* root, string word, int index) -> Node*
            {
                if (++index == len)
                {
                    return NULL;
                }
                root->children[word[index] - 'a'] = helper(root->children[word[index] - 'a'], word, index); 
                root->count--;
                if (root->count == 0)
                {
                    delete[] root->children;
                    root->children = NULL;
                    delete root;
                    return NULL;
                }
                else
                {
                    return root;
                }
                
            };
            root->children[word[0] - 'a'] = helper(root->children[word[0] - 'a'], word, 0);
            return true;
        }
        void searchPrefix(string word)
        {
            auto len = word.length();
            Node* crawl = root;
            auto ret = true;
            for (int i = 0; i < len; ++i)
            {
                auto c = word[i];
                if (!crawl->children[c-'a'])
                {
                    ret = false;
                    break;
                }
                else
                {
                    crawl = crawl->children[c-'a']; 
                }
            }
            if (!ret)
            {
                cout << "No words with prefix\n";
                return;
            }
            else
            {
                vector<string> words;
                function<void(Node*, string)> helper = [&](Node* root, string cword)
                {
                    if (root)
                    {
                        if (root->isleaf)
                        {
                            cword += root->letter;
                            words.push_back(word.substr(0,word.size() - 1) + cword);
                            for (int i = 0; i < 26; ++i)
                            {
                                auto n = root->children[i];
                                if (n)
                                {
                                    helper(n, cword);
                                }
                            }
                        }
                        else
                        {
                            cword += root->letter;
                            for (int i = 0; i < 26; ++i)
                            {
                                auto n = root->children[i];
                                if (n)
                                {
                                    helper(n,cword);
                                }
                            }
                        }
                    }
                };
                helper(crawl,string(""));
                for (auto w: words)
                {
                    cout << w << "\n";
                }
            }
        }
        bool search(string word)
        {
            auto len = word.length();
            Node* crawl = root;
            for (int i = 0; i < len; ++i)
            {
                auto c = word[i];
                auto flag = i == len - 1;
                if (flag)
                {
                    if (!crawl->children[c-'a'] || !crawl->children[c-'a']->isleaf)
                    {
                        return false;
                    }
                }
                else if (!crawl->children[c-'a'])
                {
                    return false;
                }
                else
                {
                    crawl = crawl->children[c-'a']; 
                }
            }
            return true;
        }
        void printContents()
        {
            vector<string> words;
            function<void(Node*, string)> helper = [&](Node* root, string word)
            {
                if (root)
                {
                    if (root->isleaf)
                    {
                        word += root->letter;
                        words.push_back(word);
                        for (int i = 0; i < 26; ++i)
                        {
                            auto n = root->children[i];
                            if (n)
                            {
                                helper(n, word);
                            }
                        }
                    }
                    else
                    {
                        word += root->letter;
                        for (int i = 0; i < 26; ++i)
                        {
                            auto n = root->children[i];
                            if (n)
                            {
                                helper(n,word);
                            }
                        }
                    }
                }
            };
            for (int i = 0; i < 26; ++i)
                helper(root->children[i], string(""));
            for (auto w: words)
            {
                cout << w << "\n";
            }
        }
        ~Trie()
        {
            _deleteRoot();
        }
    private:
        void _deleteRoot()
        {
            function<void(Node*)> helper = [&](Node* root)
            {
                if (root != NULL)
                {
                    for (int i = 0; i < 26; i++) helper(root->children[i]);
                    delete[] root->children;
                    root->children = NULL;
                    delete root;
                }
            };
            helper(root);
        }
};
template <typename T>
void printvec(vector<T> v)
{
    cout << "[";
    for (auto i: v)
    {
       cout << i << "\n "; 
    }
    cout << "]\n";
}

inline void menu()
{
    cout << "Make selection: (i)nsert, (d)elete, (s)earch, (p)rint, (e)nd, search (pre)fix.\n";
}

inline void selector(Trie& t, string option)
{
   if (option == "i")
   {
        string word;
        cout << "Enter word: ";
        getline(cin, word);
        t.insertWord(word); 
   } 
   else if (option == "d")
   {
        string word;
        cout << "Enter word: ";
        getline(cin, word);
        t.deleteWord(word) ? cout << "Word deleted.\n" : cout << "Word could not be found.\n";
   }
   else if (option == "s")
   {
        string word;
        cout << "Enter word: ";
        getline(cin, word);
        t.search(word) ? cout << "Word found.\n" : cout << "Word not found.\n";
   }
   else if (option == "p")
   {
       t.printContents();
   }
   else if (option == "pre")
   {
        string word;
        cout << "Enter prefix: ";
        getline(cin, word);
        t.searchPrefix(word);
   }
   else
   {
       cout << "Select valid option\n";
   }
   
}

int main(int argc, char const *argv[])
{
    vector<string> words;    
    ifstream wordfile("words.txt");
    string line;
    while (getline(wordfile, line))
    {
        words.push_back(line);
    }
    wordfile.close();
    string option;
    Trie t;
    t.fromVec(words);
    while(true)
    {
        menu();
        getline(cin, option);
        if (option == "e") break;
        selector(t, option);
    }

    return 0;
}
