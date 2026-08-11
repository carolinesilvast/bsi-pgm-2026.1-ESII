from models.equipamento import Equipamento, Notebook, Projetor, Cabo
from models.multa_strategy import MultaPorDia


class FabricaEquipamento:
    _registro = {
        "notebook": (Notebook, MultaPorDia(10.0)),
        "projetor": (Projetor, MultaPorDia(15.0)),
        "cabo": (Cabo, MultaPorDia(2.0)),
    }

    @classmethod
    def criar(cls, tipo: str, id: int, nome: str) -> Equipamento:
        classe, strategy = cls._registro.get(tipo, (None, None))
        if classe is None:
            raise ValueError(f"Tipo desconhecido: {tipo}")
        return classe(id, nome, tipo, strategy)
