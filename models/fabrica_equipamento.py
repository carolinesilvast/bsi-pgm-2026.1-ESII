from models.equipamento import Equipamento, Notebook, Projetor, Cabo


class FabricaEquipamento:
    @staticmethod
    def criar(tipo: str, id: int, nome: str) -> Equipamento:
        if tipo == "notebook":
            return Notebook(id, nome, tipo)
        elif tipo == "projetor":
            return Projetor(id, nome, tipo)
        elif tipo == "cabo":
            return Cabo(id, nome, tipo)

        raise ValueError(f"Tipo desconhecido: {tipo}")
