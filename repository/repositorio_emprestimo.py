# RepositorioEmprestimo: armazenar e recuperar dados.

from models.equipamento import Equipamento
from models.emprestimo import Emprestimo


class RepositorioEmprestimo:

    def __init__(self):
        self.equipamentos = [
            Equipamento(1, "Notebook Dell", "notebook"),
            Equipamento(2, "Projetor Epson", "projetor"),
            Equipamento(3, "Cabo HDMI", "cabo")
        ]

        self.emprestimos = []

    def buscar_equipamento(self, equipamento_id):
        for e in self.equipamentos:
            if e.id == equipamento_id:
                return e
        return None

    def salvar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def buscar_emprestimo(self, emprestimo_id):
        for e in self.emprestimos:
            if e.id == emprestimo_id:
                return e
        return None

    def listar_emprestimos(self):
        return self.emprestimos
