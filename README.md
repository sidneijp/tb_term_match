busca: conjunto de termos de busca para verificar em textos

     termos de busca podem ser tipo palavras (P) ou tipo frase (F)

     termos de busca podem ter signo de inclusão (I) ou exclusão (E)

     termos de busca tipo palavras:
     1 ou mais palavras separadas por espaços
     termo satisfeito si todas as palavras são encontradas no texto, não
importa a ordem
     nem a proximidade

     termos de busca tipo frase:
     2 ou mais palavras separadas por espaços
     termo satisfeito si a frase inteira é encontrada no texto

     termos = [
        {"signo":I, "tipo":F, "termo":"grande são paulo"},
        {"signo":I, "tipo":F, "termo":"são paulo"},
        {"signo":I, "tipo":P, "termo":"covid vacina"}
        {"signo":I, "tipo":P, "termo":"calendário vacina covid"}
        {"signo":E, "tipo":P, "termo":"futebol"}
        ]

     termos encode ISO, minúsculas
     texto unicode, maiúsculas/minúsculas

     (1) ESCREVER uma função otimizarTermos(termos)

       verificar e deletar termos redundantes, para eliminar tempo de
       processamento desnecessário


     (2) ESCREVER uma função testarMatch(termos, texto)

       retornar False si algum termo de busca de exclusão é satisfeito
       retornar True si algum termo de busca de inclusão é satisfeito
       retornar False si nenhum termo é satisfeito

