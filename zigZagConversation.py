class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res_constructor = []
        res = ""
        nr_intermidiate_leters = numRows - 2


        column_counter = numRows
        intermidiate_counter = nr_intermidiate_leters


        lista_aux = []
        flag = 0
        e=0
        while e < len(s):
            if flag == 0: #enquanto preenche a primeira coluna
                if column_counter == numRows:
                    lista_aux = []
                lista_aux += s[e]
                column_counter -= 1
                e += 1
                if column_counter == 0:
                    column_counter = numRows
                    res_constructor.append(lista_aux)
                    flag = 1
            elif flag == 1: #esta nas letras intermedias
                if nr_intermidiate_leters > 0:
                    lista_aux = [' '] * numRows
                    lista_aux[nr_intermidiate_leters] = s[e]
                    res_constructor.append(lista_aux)
                    e += 1
                    nr_intermidiate_leters -= 1
                else:
                    nr_intermidiate_leters = numRows - 2
                    flag = 0
        if column_counter > 0 and column_counter != numRows:
            lista_aux_2 = [' '] * numRows
            for e in range(len(lista_aux)):
                lista_aux_2[e] = lista_aux[e]
            res_constructor.append(lista_aux_2)

        for i in range(numRows):
            for e in range(len(res_constructor)):
                res += res_constructor[e][i]
        res = res.replace(' ', '')
        return res
