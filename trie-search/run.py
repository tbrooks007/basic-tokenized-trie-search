from token_trie import TokenTrie
from text_processor import *


def process_raw_text(raw_text):
    """
    Function processes raw text. Processing includes tokenizing, removing stop words, punctuation and returning document as
    a set of unique noun phrases.
    :param raw_text: string
    :return: set of cleaned noun chunks as strings
    """

    spacy_doc = parse_text(raw_text)
    noun_chunks = get_noun_chunks(spacy_doc)

    return noun_chunks


def search(root, txt):
    """
    Searches tree for given string
    :param root: TokenTrie
    :param txt: string
    :return: Phrase string if found, None if not found
    """

    tokens = txt.split(' ')
    results = TokenTrie.search(root, tokens)

    return results


def build_token_trie_tree(root, vocabulary):
    """
    Build tokenized trie tree.
    :param root: TokenTrie
    :param vocabulary: list of strings
    """

    for phrase in vocabulary:
        phrase_tokens = phrase.split(' ')

        # insert phrase into the tree
        TokenTrie.insert(root, phrase_tokens, phrase)


if __name__ == "__main__":

    # build tokenized trie tree
    seed_vocabulary = ['Borrower', 'Subsidiaries', 'Material Project Party', 'Project',
                       'Project Manager',
                       'Anti-Money Laundering Laws',
                       'Sanctions',
                       'Anti-Corruption Laws',
                       'Affiliates',
                       'Sanctioned Person',
                       'Sanctioned Country',
                       'Person',
                       'Officer',
                       'Director',
                       'Agents']

    # sort seed list
    seed_vocabulary.sort()

    # build tokenized trie tree
    root = TokenTrie()
    build_token_trie_tree(root, seed_vocabulary)

    # process raw text
    raw_txt = 'The operations of each Borrower, and the activities of the officers and directors and, to the knowledge of each Borrower,  any Subsidiaries of the ' \
              'Borrowers, employees, agents and representatives of each Borrower, while acting on behalf of such Borrower, and to the knowledge of each Borrower the ' \
              'operations of each Material Project Party in relation to the Project, have been conducted at all times in compliance with all applicable Anti-Money Laundering Laws, Sanctions, and Anti-Corruption Laws. ' \
              'Neither Borrower, nor any Subsidiaries of the Borrowers, nor any officer or director or, to the knowledge of any Borrower, Affiliates, employee, agent or representative of either Borrower has ' \
              'engaged, directly or indirectly, in any activity or conduct which would violate any Anti-Corruption Laws or Anti-Money Laundering Laws. Neither Borrower nor any Subsidiaries of the Borrowers, nor any ' \
              'officer or director or, to the knowledge of any Borrower, Affiliates, employee, agent or representative of either Borrower has engaged, directly or indirectly, in any dealings or transactions with, ' \
              'involving or for the benefit of a Sanctioned Person,or in or involving a Sanctioned Country, where such dealings or transactions would violate Sanctions, in the five (5) year period immediately preceding the date hereof.'

    processed_noun_chunks = process_raw_text(raw_txt)

    # search the tree for phrases in text
    found_phrases = []

    for chunk in processed_noun_chunks:
        phrase = search(root, chunk)

        if phrase:
            found_phrases.append(phrase)

    print()
    print("The Following Phrases Were Found In The Tree: ")
    for phrase in found_phrases:
        print(phrase)



