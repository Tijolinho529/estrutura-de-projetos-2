from enum import Enum

class Genero(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

    def __init__(self, nome: str, sigla : str) -> None:
        self.nome = nome
        self.sigla = sigla