class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    # Getters
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_estoque(self):
        return self.__estoque

    # Setters
    def set_nome(self, nome: str):
        if isinstance(nome, str) and nome.strip():
            self.__nome = nome.strip()
        else:
            raise ValueError("Nome deve ser uma string não vazia.")

    def set_preco(self, preco: float):
        if isinstance(preco, (int, float)) and preco >= 0:
            self.__preco = float(preco)
        else:
            raise ValueError("Preço deve ser um número não negativo.")

    def set_estoque(self, estoque: int):
        if isinstance(estoque, int) and estoque >= 0:
            self.__estoque = estoque
        else:
            raise ValueError("Estoque deve ser um inteiro não negativo.")

    def __str__(self) -> str:
        return f"{self.__nome} - R${self.__preco:.2f}"

    def aplicar_desconto(self, valor: float = 10.0):
        if valor < 0:
            raise ValueError("Valor do desconto não pode ser negativo.")
        self.__preco = max(0.0, self.__preco - valor)

    def reduzir_estoque(self, qtd: int = 1):
        if qtd <= 0:
            raise ValueError("Quantidade deve ser positiva.")
        self.__estoque = max(0, self.__estoque - qtd)


class Cadeira(Produto):
    def __init__(self, nome: str, preco: float, estoque: int, material: str, altura: float):
        super().__init__(nome, preco, estoque)
        self.__material = material
        self.__altura = altura

    def get_material(self) -> str:
        return self.__material

    def set_material(self, material: str):
        if isinstance(material, str) and material.strip():
            self.__material = material.strip()
        else:
            raise ValueError("Material deve ser uma string não vazia.")

    def get_altura(self) -> float:
        return self.__altura

    def set_altura(self, altura: float):
        if isinstance(altura, (int, float)) and altura > 0:
            self.__altura = float(altura)
        else:
            raise ValueError("Altura deve ser positiva.")

    def __str__(self) -> str:
        return f"Cadeira: {super().__str__()} | Material: {self.__material} | Altura: {self.__altura:.2f}m"


class Biscoito(Produto):
    def __init__(self, nome: str, preco: float, estoque: int, sabor: str, peso_gramas: float):
        super().__init__(nome, preco, estoque)
        self.__sabor = sabor
        self.__peso_gramas = peso_gramas

    def get_sabor(self) -> str:
        return self.__sabor

    def set_sabor(self, sabor: str):
        if isinstance(sabor, str) and sabor.strip():
            self.__sabor = sabor.strip()
        else:
            raise ValueError("Sabor deve ser uma string não vazia.")

    def get_peso_gramas(self) -> float:
        return self.__peso_gramas

    def set_peso_gramas(self, peso: float):
        if isinstance(peso, (int, float)) and peso > 0:
            self.__peso_gramas = float(peso)
        else:
            raise ValueError("Peso deve ser positivo.")

    def __str__(self) -> str:
        return f"Biscoito: {super().__str__()} | Sabor: {self.__sabor} | Peso: {self.__peso_gramas:.1f}g"

if __name__ == "__main__":
    cadeira1 = Cadeira("Cadeira Ergonômica", 299.90, 50, "Madeira", 0.85)
    biscoito1 = Biscoito("Biscoito de Chocolate", 4.50, 200, "Chocolate", 150.0)

    print(cadeira1)
    print(biscoito1)

    print("\n→ Aplicando desconto de R$20 na cadeira:")
    cadeira1.aplicar_desconto(20.0)
    print(cadeira1)

    print("\n→ Reduzindo estoque do biscoito:")
    biscoito1.reduzir_estoque(5)
    print(f"Estoque restante: {biscoito1.get_estoque()}")

    print(f"\nNome da cadeira: {cadeira1.get_nome()}")
    print(f"Preço do biscoito: R${biscoito1.get_preco():.2f}")