# coding: utf-8
import unittest

import busca_termos


class TestTermos(unittest.TestCase):
    def setUp(self):
        self.termos = [
            {"signo": 'I', "tipo": 'F', "termo": "grande são paulo"},
            {"signo": 'I', "tipo": 'F', "termo": "grande são paulo"},
            {"signo": 'I', "tipo": 'F', "termo": "são paulo"},
            {"signo": 'I', "tipo": 'P', "termo": "covid vacina"},
            {"signo": 'I', "tipo": 'P', "termo": "calendário vacina covid"},
            {"signo": 'E', "tipo": 'P', "termo": "futebol"},
            {"signo": 'E', "tipo": 'F', "termo": "voley feminino"},
        ]
        self.texto_c_exclusoes1 = 'são paulo é a capital do voley feminino'
        self.texto_c_exclusoes2 = 'são paulo é a capital do futebol'
        self.texto_s_exclusoes = 'são paulo é a capital do basquete'
        self.texto_inclusoes_parciais = 'calendário do basquete'
        self.texto_inclusoes_completa = \
            'baixar calendário da vacina p/ o covid'
        self.texto_inclusoes_palavra_parecida = \
            'baixar calendário de vacinação p/ o covid'
        self.texto_s_inclusoes_exclusoes = '42 é a resposta'

    def test_otimizarTermos(self):
        expected = 6
        result = busca_termos.otimizarTermos(self.termos)
        self.assertEquals(expected, len(result))

    def test_testarMatch(self):
        cases = [
            {'text': self.texto_c_exclusoes1, 'expected': False},
            {'text': self.texto_c_exclusoes2, 'expected': False},
            {'text': self.texto_s_exclusoes, 'expected': True},
            {'text': self.texto_inclusoes_parciais, 'expected': False},
            {'text': self.texto_inclusoes_completa, 'expected': True},
            {'text': self.texto_inclusoes_palavra_parecida, 'expected': False},
            {'text': self.texto_s_inclusoes_exclusoes, 'expected': False},
        ]
        for case in cases:
            result = busca_termos.testarMatch(self.termos, case['text'])
            case['returned'] = result
            self.assertEquals(case['expected'], result, str(case))
