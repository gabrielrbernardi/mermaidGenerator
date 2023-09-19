import string

class Main():
    def __init__(self) -> None:
        self.maiusculo = string.ascii_uppercase
        self.letras = string.ascii_uppercase + string.ascii_lowercase
        self.menu()
        pass

    def menu(self):
        (opcao_geral, qtd) = self.main_menu()
        if opcao_geral == 1:
            self.trata_tokens(qtd)
        elif opcao_geral == 2:
            self.menu_automato(qtd)
        else:
            print("Erro")
            exit()
        
    def main_menu(self):
        print("MENU".center(50, "="))
        print(" 1 - TOKENS (automático)")
        print(" 2 - Autômatos")
        opcao = int(input("Escolha: "))
        qtd_pecas = int(input("Quantidade de tokens/automatos: "))
        return (opcao, qtd_pecas)

    def trata_tokens(self, qtd):
        f = open("tokens.txt", "w")
        print("TOKENS".center(50, "-"))
        for i in range(qtd):
            print("Token " + str(i + 1))
            token = input("Digite o TOKEN: ")
            excecao = input("Digite o valor de excecao: ")

            for x in range(len(token) + 1):
                f.write(self.letras[i] + str(x) + "((" + str(x) + "))" + "\n")
            f.write(self.letras[i] + str(len(token) + 1) + "(((" + token + ")))" + "\n")

            f.write(self.letras[i] + "INICIO" + "((S)) --> " + self.letras[i] + str(0) + "\n")
            for idx, x in enumerate(token):
                temp = self.letras[i] + str(idx) + ' -- "' + x + '" --> ' + self.letras[i] + str(idx + 1)
                f.write(temp + "\n")
            
            f.write(self.letras[i] + str(len(token)) + ' -- "' + excecao + '" --> ' + self.letras[i] + str(len(token) + 1) + "\n\n")
        f.close()
        
    
    def menu_automato(self, qtd):
        f = open("automato.txt", "w")
        print("Automatos".center(50, "-"))
        for i in range(qtd):
            temp_list = []
            grupo_controle = []
            for x in self.maiusculo:
                temp_dict = {"no": x, "final": False, "connections": []}
                temp_list.append(temp_dict)
            
            while(True):
                inicio = input("Inicio: ")
                if inicio == "fim" or inicio == "FIM":
                    break

                if inicio not in grupo_controle:
                    grupo_controle.append(inicio)

                final = input("Final: ")
                if final not in grupo_controle:
                    grupo_controle.append(final)
                no_final = input("No final? ")
                for idx2, x in enumerate(temp_list):
                    if x["no"] == inicio:
                        temp_list[idx2]["connections"].append(final)
                        if no_final in ["S", "s", "Y", "y"]:
                            print("aqui")
                            temp_list[idx2]["final"] = True

            filtered_list = []
            for x in temp_list:
                if x["connections"] != []:
                    filtered_list.append(x)

            print(filtered_list)
            
            filtered_grupo_controle = grupo_controle.copy()

            for x in filtered_list:
                if x["final"] == True:
                    print(x["no"])
                    f.write(self.letras[i] + "_" + str(x["no"]) + "(((" + str(x["no"]) + ")))" + "\n")
                    filtered_grupo_controle.remove(x["no"])

            for x in range(len(filtered_grupo_controle)):
                f.write(self.letras[i] + "_" + str(filtered_grupo_controle[x]) + "((" + str(filtered_grupo_controle[x]) + "))" + "\n")

            f.write(self.letras[i] + "_" + "INICIO" + "((S)) --> " + self.letras[i] + "_" + str(grupo_controle[0]) + "\n")
            
            for x in temp_list:
                for y in x["connections"]:
                    f.write(self.letras[i] + "_" + x["no"] + " -- " + "AAAA" +  " --> " + self.letras[i] + "_" + y + "\n")
      
        f.close()

# 2
# 1
# A
# F
# S
# J
# H
# N
# A
# G
# S
# A
# A
# N
# A
# J
# N
# G
# A
# N
# G
# H
# N
# FIM
                
main = Main()