class Tarefa:
    def __init__(self, task_id, titulo, descricao, status, prazo, prioridade, responsavel):
        self.task_id = task_id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.prazo = prazo
        self.prioridade = prioridade
        self.responsavel = responsavel

    def to_json(self):
        return {
            "task_id": self.task_id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "prazo":self.prazo,
            "prioridade": self.prioridade,
            "responsavel": self.responsavel
        }