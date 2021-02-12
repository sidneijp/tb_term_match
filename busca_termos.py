# coding: utf-8


def otimizarTermos(termos):
    termos = instanciate_terms_list(termos)
    termos = set(termos)
    return termos


def testarMatch(termos, texto):
    termos = instanciate_terms_list(termos)
    exclusion_terms = [term for term in termos if term.sign == 'E']
    inclusion_terms = [term for term in termos if term.sign == 'I']
    has_exclusion_terms = any(
        term.has_match(texto) for term in exclusion_terms
    )
    has_inclusion_terms = any(
        term.has_match(texto) for term in inclusion_terms
    )
    if has_exclusion_terms:
        return False
    if has_inclusion_terms:
        return True
    return has_exclusion_terms or has_inclusion_terms


def instanciate_terms_list(terms_dict_list):
    terms = []
    for termo in terms_dict_list:
        if isinstance(termo, dict):
            termo = TermFactory.from_dict(termo)
        terms.append(termo)
    return terms


class Term(object):
    def __init__(self, term, sign, type):
        self.term = term
        self.sign = sign
        self.type = type

    def type(text):
        raise NotImplementedError

    def search(text):
        raise NotImplementedError

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.term, self.sign, self.type))


class TermWords(Term):
    type = 'P'

    @property
    def words(self):
        return self.term.split()

    def has_match(self, text):
        text = text.lower()
        return all(word in text.split() for word in self.words)


class TermPhrase(Term):
    type = 'F'

    @property
    def phrase(self):
        return self.term

    def has_match(self, text):
        text = text.lower()
        return self.term in text


class TermTypes(object):
    types = [
        TermWords,
        TermPhrase,
    ]

    @classmethod
    def get_termclass_by_type(cls, term_type_name):
        for TermClass in cls.types:
            if TermClass.type == term_type_name:
                return TermClass


class TermFactory(object):
    @classmethod
    def from_dict(cls, term):
        _type = term.get('tipo')
        TermoClass = TermTypes.get_termclass_by_type(_type)
        return TermoClass(
            term=term.get('termo'),
            sign=term.get('signo'),
            type=_type
        )
