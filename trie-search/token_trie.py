
class TokenTrie(object):

    def __init__(self):
        self.children = dict()
        self.value = None

    @staticmethod
    def insert(token_trie, phrase_tokens, phrase):
        """
        Insert phrase into tree.
        :param token_trie: TokenTrie
        :param phrase_tokens: list of strings that are tokens in value phrase
        :param phrase: phrase that represents value at terminal nodes in the tree
        """

        for token in phrase_tokens:
            if token not in token_trie.children:
                token_trie.children[token] = TokenTrie()
            token_trie = token_trie.children[token]

        token_trie.value = phrase

    @staticmethod
    def search(token_trie, phrase_tokens):
        """
        Searches tree for phrase with given tokens.
        :param token_trie: TokenTrie
        :param phrase_tokens: list of strings that are tokens in a phrase
        :return: Found phrase or None
        """

        for token in phrase_tokens:
            if token in token_trie.children:
                token_trie = token_trie.children[token]

        return token_trie.value
