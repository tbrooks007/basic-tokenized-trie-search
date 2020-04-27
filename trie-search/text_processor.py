import re
import spacy
from spacy.tokenizer import Tokenizer
from spacy.util import compile_prefix_regex, compile_suffix_regex


def get_noun_chunks(spacy_doc):
    """
    Processes and cleans noun chunks from given spacy document. Processing includes removing punctuation
    and stop words. Note, this is a very basic cleaning function and something more robust would be needed
    for a production system.
    :param spacy_doc: spacy document object
    :return: set of cleaned noun chunks
    """

    phrase_tokens = []
    cleaned_noun_chunks = set()

    for chunk in spacy_doc.noun_chunks:
        for token in chunk:
            # remove stop words and punctuation from noun chunks
            if not token.is_stop and not token.is_punct:
                phrase_tokens.append(str(token))

        # add cleaned chunks to set
        cleaned_chunk = " ".join(phrase_tokens)
        cleaned_noun_chunks.add(cleaned_chunk)
        phrase_tokens = []
        temp_phrase = None

    # DEBUG Me:
    # for cleaned_chunk in cleaned_noun_chunks:
    #     print(cleaned_chunk)

    return cleaned_noun_chunks


def parse_text(text):
    """
    Raw text to parse
    :param text: string
    :return: spacy document
    """

    def custom_tokenizer(nlp_object):
        infix_re = re.compile(r'''[.\,\?\:\;\...\‘\’\`\“\”\"\'~]''')
        prefix_re = compile_prefix_regex(nlp_object.Defaults.prefixes)
        suffix_re = compile_suffix_regex(nlp_object.Defaults.suffixes)

        return Tokenizer(nlp_object.vocab, prefix_search=prefix_re.search,
                         suffix_search=suffix_re.search,
                         infix_finditer=infix_re.finditer,
                         token_match=None)

    nlp = spacy.load('en_core_web_sm')

    # add a custom tokenizer that will enable us to properly tokenize phrases with hyphens
    # so that the tokenizer doesn't split tokens on the hyphen
    nlp.tokenizer = custom_tokenizer(nlp)
    doc = nlp(text)

    return doc


