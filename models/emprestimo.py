from dataclasses import dataclass
from datetime import date


@dataclass
class Emprestimo:
    id: int
    equipamento_id: int
    usuario_nome: str
    usuario_email: str
    data_emprestimo: date
    data_devolucao: date
    devolvido: bool = False
