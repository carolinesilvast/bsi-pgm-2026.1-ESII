from abc import ABC, abstractmethod
from typing import Optional
from models.equipamento import Equipamento
from models.emprestimo import Emprestimo


class IRepositorioEmprestimo(ABC):
    @abstractmethod
    def buscar_equipamento(self, id: int) -> Optional[Equipamento]:
        pass

    @abstractmethod
    def salvar_emprestimo(self, emprestimo: Emprestimo) -> None:
        pass

    @abstractmethod
    def buscar_emprestimo(self, id: int) -> Optional[Emprestimo]:
        pass

    @abstractmethod
    def marcar_indisponivel(self, equip_id: int) -> None:
        pass

    @abstractmethod
    def marcar_disponivel(self, equip_id: int) -> None:
        pass

    @abstractmethod
    def marcar_devolvido(self, emprestimo_id: int) -> None:
        pass

    @abstractmethod
    def listar_em_atraso(self) -> list:
        pass

    @abstractmethod
    def proximo_id_emprestimo(self) -> int:
        pass
