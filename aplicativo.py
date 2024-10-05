import random

adjetivos = ["Inovadora", "Sustentável", "Ágil", "Inteligente", "Global", "Criativa", "Digital"]
substantivos = ["Soluções", "Tecnologia", "Serviços", "Desenvolvimento", "Consultoria", "Produção", "Design"]

def gerar_nome_empresa():
    adjetivo = random.choice(adjetivos)
    substantivo = random.choice(substantivos)
    return f"{adjetivo} {substantivo}"

def main():
    print("Bem-vindo ao Gerador de Nomes de Empresas!")
    while True:
        gerar = input("Deseja gerar um nome de empresa? (s/n): ").lower()
        if gerar == 's':
            nome_empresa = gerar_nome_empresa()
            print(f"Nome gerado: {nome_empresa}")
        elif gerar == 'n':
            print("Saindo...")
            break
        else:
            print("Por favor, responda com 's' para sim ou 'n' para não.")

if __name__ == "__main__":
    main()