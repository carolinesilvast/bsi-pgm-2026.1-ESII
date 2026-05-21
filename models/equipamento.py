# Equipamento: representar os dados e calcular multa.

from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Equipamento(ABC):
    id: int
    nome: str
    tipo: str
    disponivel: bool = True

    @abstractmethod
    def calcular_multa(self, atraso):
        pass


@dataclass
class Notebook(Equipamento):

    def calcular_multa(self, atraso):
        return max(0, atraso * 10.0)


@dataclass
class Projetor(Equipamento):

    def calcular_multa(self, atraso):
        return max(0, atraso * 15.0)


@dataclass
class Cabo(Equipamento):

    def calcular_multa(self, atraso):
        return max(0, atraso * 2.0)
