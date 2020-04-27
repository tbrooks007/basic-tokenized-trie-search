# Tokenized Trie Search

This project provides a very basic implementation of a modified Trie tree that indexes tokens instead of characters.
The trie tree uses dictionaries to keep track of the lists of child nodes and stores the value of the phrases in its 
terminal nodes. In a production setting I would explore implementing a linked list based approach where lists of child 
nodes are singly linked list.

### Document Preprocessing
The document we are processing with Tokenized Trie goes through some basic preprocessing. This preprocessing includes:
* removing punctuation and stop words
* tokenization

### Possible Improvements

There are a number of improvements that could be made to this implementation including:
* loading all text and seed data from files where the files are passed into the driving module as paths
* serializing tree to a format that would allow us to flush the tree to disk and load it again so that we don't have to 
rebuild it each time we run it 
* implement unit tests for all functions
* refactor tree data structure to use singly linked lists instead of dictionaries
* implement fuzzy search matching
 
### Setup

1. Python 3.6+
2. virtualenv (`pip install virtualenv`)
3. virtualenvwrapper (`pip install virtualenvwrapper`)

### Install Required Libraries

- `mkvirtualenv trie-search` (if python 3.X+ is your default python version) OR
- Type which python3, to get the path of your python3 (i.e. /usr/local/bin/python)
- `mkvirtualenv -p [Path To Python3] trie-search`
- cd to project directory
- `pip install spacy`

### Download Spacy English Models
`python -m spacy download en_core_web_sm`

### Run
Go to the root of this project and type:

```
python run.py
```
