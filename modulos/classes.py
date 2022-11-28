class Produto:
    contador: int = 1

    def __init__(self: object, nome: str, preco: float, estoque: int) -> None:
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        self.__estoque: int = estoque
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> float:
        return self.__preco

    @property
    def estoque(self: object) -> int:
        return self.__estoque

    def estoqueSet(self, value):
        self.__estoque = value

    def diminui_estoque(self):
        self.__estoque = self.estoque - 1

    def __str__(self) -> str:
        return f'Codigo: {self.codigo}\nNome: {self.nome}\nPreço: {formata_float_str_moeda(self.preco)}'


class Pessoa:
    def __init__(self: object, nome: str, aniv: str, senha: str) -> None:
        self.__senha: str = senha
        self.__nome: str = nome
        self.__aniv: str = aniv

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def aniv(self: object) -> str:
        return self.__aniv

    @property
    def senha(self: object) -> str:
        return self.__senha


class Cliente(Pessoa):
    def __init__(self: object, nome, aniv, senha, email: str) -> None:
        super().__init__(nome, aniv, senha)
        self.__email: str = email

    @property
    def email(self):
        return self.__email

class Funcionario(Pessoa):
    def __init__(self: object, nome, aniv, senha,  cargo: str) -> None:
        super().__init__(nome, aniv, senha)
        self.__cargo: str = cargo

    @property
    def cargo(self):
        return self.__cargo


def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'