# =============================================================================
#  FARMTECH SOLUTIONS — Sistema de Gestão de Agricultura Digital
#  Culturas: Cana-de-Açúcar (Área A) | Milho (Área B)
# =============================================================================

import os

figura_area_a = "trapezio"    # Área A — Escolhida para Cana-de-Açúcar
figura_area_b = "retangulo"   # Área B — Escolhida para Milho

cultura_area_a = "Cana-de-Acucar"
cultura_area_b = "Milho"

dim_area_a = [0.0, 0.0, 0.0]
dim_area_b = [0.0, 0.0]

areaCultivada_m2 = [0.0, 0.0]   # vetor com as duas áreas calculadas

num_ruas    = [0, 0]
comp_rua    = [0.0, 0.0]
dose_ins1   = [0.0, 0.0]    # Insumo 1 — Ureia (mL/m2) para ambas as culturas
dose_ins2   = [0.0, 0.0]    # Insumo 2 — Vinhaca (mL/m2) Cana | MAP (mL/m2) Milho
total_ins1  = [0.0, 0.0]
total_ins2  = [0.0, 0.0]


def calcular_area(idx):
    if idx == 0:  # area_trapézio
        areaCultivada_m2[idx] = ((dim_area_a[0] + dim_area_a[1]) / 2) * dim_area_a[2]
    else:         # area_retângulo
        areaCultivada_m2[idx] = dim_area_b[0] * dim_area_b[1]

def calcular_insumos(idx):
    # Ambos os insumos agora em mL/m2 — total = dose * area
    total_ins1[idx] = dose_ins1[idx] * areaCultivada_m2[idx]
    total_ins2[idx] = dose_ins2[idx] * areaCultivada_m2[idx]


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPressione ENTER para voltar ao menu...")

def cabecalho():
    limpar()
    print("=" * 55)
    print("  FARMTECH SOLUTIONS — Agricultura Digital")
    print("=" * 55)
    print(f"  Area A: {cultura_area_a} ({figura_area_a})")
    print(f"  Area B: {cultura_area_b} ({figura_area_b})")
    print("=" * 55)
    print()

def label_ins1(idx):
    return "Ureia-N (mL/m2)"  # Ureia para ambas as culturas

def label_ins2(idx):
    return "Vinhaca (mL/m2)" if idx == 0 else "MAP/Fosfato (mL/m2)"

def selecionar_area():
    print("  [0] Area A —", cultura_area_a)
    print("  [1] Area B —", cultura_area_b)
    try:
        idx = int(input("\n  Area: "))
        if idx not in [0, 1]:
            raise ValueError
        return idx
    except ValueError:
        print("  Opcao invalida.")
        return None


# OPÇÃO_MENU - RECEBER DADOS
def entrada():
    cabecalho()
    print("  ENTRADA DE DADOS\n")
    idx = selecionar_area()
    if idx is None:  # Se o usuário não digitar valor válido.
        pausar()
        return

    print()
    try:
        if idx == 0:
            dim_area_a[0] = float(input("  Base maior (m): "))
            dim_area_a[1] = float(input("  Base menor (m): "))
            dim_area_a[2] = float(input("  Altura (m):     "))
        else:
            dim_area_b[0] = float(input("  Comprimento (m): "))
            dim_area_b[1] = float(input("  Largura (m):     "))

        num_ruas[idx]  = int(input("  Numero de ruas:              "))
        comp_rua[idx]  = float(input("  Comprimento de cada rua (m): "))
        dose_ins1[idx] = float(input(f"  Dose {label_ins1(idx)}: "))
        dose_ins2[idx] = float(input(f"  Dose {label_ins2(idx)}: "))

        calcular_area(idx)
        calcular_insumos(idx)
        print("\n  Dados salvos com sucesso!")

    except ValueError:
        print("\n  Valor invalido.")

    pausar()


# OPÇÃO_MENU - SAÍDA DE DADOS
def saida():
    cabecalho()
    print("  SAIDA DE DADOS\n")

    nomes   = [cultura_area_a, cultura_area_b]
    figuras = [figura_area_a,  figura_area_b]

    for idx in range(2):
        print(f"  --- Area {'A' if idx == 0 else 'B'} | {nomes[idx]} | {figuras[idx]} ---")  # Mostra o nome da área e seu formato geométrico.

        if idx == 0:
            print(f"  Base maior : {dim_area_a[0]:.2f} m")
            print(f"  Base menor : {dim_area_a[1]:.2f} m")
            print(f"  Altura     : {dim_area_a[2]:.2f} m")
        else:
            print(f"  Comprimento: {dim_area_b[0]:.2f} m")
            print(f"  Largura    : {dim_area_b[1]:.2f} m")

        print(f"  Area       : {areaCultivada_m2[idx]:.2f} m2")
        print(f"  Ruas       : {num_ruas[idx]} x {comp_rua[idx]:.1f} m")
        print(f"  {label_ins1(idx)}: dose {dose_ins1[idx]:.2f} -> total {total_ins1[idx]:.2f} mL")
        print(f"  {label_ins2(idx)}: dose {dose_ins2[idx]:.2f} -> total {total_ins2[idx]:.2f} mL")
        print()

    pausar()


# OPÇÃO_MENU - ATUALIZAR DADOS
def atualizar():
    cabecalho()
    print("  ATUALIZACAO DE DADOS\n")
    idx = selecionar_area()
    if idx is None:
        pausar()
        return

    print()
    print("  [1] Dimensoes do talhao")
    print("  [2] Numero de ruas")
    print("  [3] Comprimento das ruas")
    print("  [4] Dose", label_ins1(idx))
    print("  [5] Dose", label_ins2(idx))

    try:
        campo_alterado = int(input("\n  Campo: "))
        if campo_alterado == 1:
            if idx == 0:
                dim_area_a[0] = float(input("  Nova base maior (m): "))
                dim_area_a[1] = float(input("  Nova base menor (m): "))
                dim_area_a[2] = float(input("  Nova altura (m):     "))
            else:
                dim_area_b[0] = float(input("  Novo comprimento (m): "))
                dim_area_b[1] = float(input("  Nova largura (m):     "))
        elif campo_alterado == 2:
            num_ruas[idx] = int(input("  Novo numero de ruas: "))
        elif campo_alterado == 3:
            comp_rua[idx] = float(input("  Novo comprimento de rua (m): "))
        elif campo_alterado == 4:
            dose_ins1[idx] = float(input(f"  Nova dose {label_ins1(idx)}: "))
        elif campo_alterado == 5:
            dose_ins2[idx] = float(input(f"  Nova dose {label_ins2(idx)}: "))
        else:
            print("  Escolha invalida.")
            pausar()
            return

        calcular_area(idx)
        calcular_insumos(idx)
        print("\n  Dados atualizados!")

    except ValueError:
        print("\n  Valor invalido.")

    pausar()


# OPÇÃO_MENU - DELEÇÃO
def deletar():
    cabecalho()
    print("  DELECAO DE DADOS\n")
    idx = selecionar_area()
    if idx is None:
        pausar()
        return

    confirm = input("\n  Confirma exclusao? (s/n): ").strip().lower()
    if confirm != 's':
        print("  Cancelado.")
        pausar()
        return

    if idx == 0:
        dim_area_a[:] = [0.0, 0.0, 0.0]
    else:
        dim_area_b[:] = [0.0, 0.0]

    areaCultivada_m2[idx] = 0.0
    num_ruas[idx]         = 0
    comp_rua[idx]         = 0.0
    dose_ins1[idx]        = 0.0
    dose_ins2[idx]        = 0.0
    total_ins1[idx]       = 0.0
    total_ins2[idx]       = 0.0

    print("  Dados apagados.")
    pausar()


# OPCAO_MENU - EXPORTAR CSV
def exportar_csv():
    cabecalho()
    print("  EXPORTAR DADOS PARA R\n")

    # Salva na mesma pasta do script, onde o R vai procurar o arquivo
    nome_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "farmtech_dados.csv")
    culturas = [cultura_area_a, cultura_area_b]
    figuras  = [figura_area_a,  figura_area_b]

    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:  # Comando de escrita dos dados
            f.write("area,cultura,figura,area_m2,"
                    "num_ruas,comp_rua,"
                    "insumo1,dose_ins1,total_ins1,"
                    "insumo2,dose_ins2,total_ins2\n")

            for idx in range(2):
                f.write(
                    f"{'A' if idx == 0 else 'B'},"
                    f"{culturas[idx]},"
                    f"{figuras[idx]},"
                    f"{areaCultivada_m2[idx]:.2f},"
                    f"{num_ruas[idx]},"
                    f"{comp_rua[idx]:.2f},"
                    f"{label_ins1(idx)},"
                    f"{dose_ins1[idx]:.2f},"
                    f"{total_ins1[idx]:.2f},"
                    f"{label_ins2(idx)},"
                    f"{dose_ins2[idx]:.2f},"
                    f"{total_ins2[idx]:.2f}\n"
                )

        print(f"  Arquivo '{os.path.basename(nome_arquivo)}' exportado com sucesso!")
    except Exception as e:
        print(f"  Falha ao exportar: {e}")

    pausar()


# MENU PRINCIPAL
def menu():
    while True:
        cabecalho()
        print("  [1] Entrada de dados")
        print("  [2] Saida de dados")
        print("  [3] Atualizar dados")
        print("  [4] Deletar dados")
        print("  [5] Exportar relatorio em CSV")
        print("  [0] Sair")
        print()

        try:
            op = int(input("  Selecione a opcao que deseja para continuar: "))
        except ValueError:
            continue

        if   op == 1: entrada()
        elif op == 2: saida()
        elif op == 3: atualizar()
        elif op == 4: deletar()
        elif op == 5: exportar_csv()
        elif op == 0:
            print("\n  Encerrando FarmTech. Ate logo!\n")
            break

if __name__ == "__main__":
    menu()