# autor: Tiago Ferreira Bonomo
# Protótipo de gerador de combinacções
# -*- coding: utf-8 -*-
import math
import random
import json


class GeNuLoto:

    def __init__(self, qt_combinacao, qt_dezenas):
        self.qt_combinacao = qt_combinacao
        self.qt_dezenas = qt_dezenas

    def ve_dados(self):
        print(" quantidade de combinações " + str(self.qt_combinacao) +
              " quantidade de dezenas " + str(self.qt_dezenas))

    def ge_comb(self):

        dezenas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                   14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        # dezenas = [1, 2, 3, 4, 5]
        combinacoes = []
        combinacao = []

        c = len(dezenas)
        p = self.qt_dezenas

        res = self.qt_combinacao
        #print("Resposta: ", res)

        cont_combs = 0
        counter_inters = 0
        counter_combs = 0

        # Combinações a Gerar
        while (res > cont_combs):
            combination = random.sample(dezenas, p)
            if len(combinacoes) == 0:
                #print("Combination: ", combination)
                combinacoes.append(sorted(combination))
                cont_combs = cont_combs + 1

            if len(combinacoes) > 0:

                cont_inters = 0
                for i in combinacoes:
                    inters = set(i).intersection(combination)

                    if len(inters) == p:
                        cont_inters = cont_inters + 1

                if cont_inters == 0:
                    #print("Combinação: ", combination)
                    #print("Interceção: ", inters)
                    #print("Quantidade de Interceções: ", len(inters))
                    combinacoes.append(sorted(combination))
                    cont_combs = cont_combs + 1

        cont_res = 0
        indice = 0
        lista_chaves = []
        lista_comb = []
        for i in combinacoes:

            cont_res = cont_res + 1

            lista_chaves.append(str(cont_res))
            lista_comb.append(i)

            # print(str(lista_chaves[indice])+str(lista_comb[indice]))

            #print(str(cont_res)+"º Combinação: ", i)
            #print(str(indice)+" variavel indice ")

            indice = indice + 1

        dict_comb = dict(zip(lista_chaves, lista_comb))
        json_comb = json.dumps(dict_comb)
        print(json_comb)
        return dict_comb


#lotofacil = GeNuLoto(100, 15)
# lotofacil.ve_dados()
# lotofacil.ge_comb()
