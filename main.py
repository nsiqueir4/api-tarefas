from flask import Flask, request
from tarefa import Tarefa

app = Flask(__name__)

tarefas = [
    Tarefa(task_id=1,
           titulo="Estudar JavaScript",
           descricao="Estudar JavaScript para aprender a construir evento",
           status="em andamento",
           prazo="2025-03-10",
           prioridade="Alta",
           responsavel="Nicolas"),
    Tarefa(task_id=2,
           titulo="Estudar JavaScript",
           descricao="Estudar JavaScript para aprender a construir evento",
           status="em andamento",
           prazo="2025-03-10",
           prioridade="Alta",
           responsavel="Nicolas")
]
tarefas = [
    {
        "id": 1,
        "titulo": "Estudar JavaScript",
        "descricao": "Estudar JavaScript para aprender a construir evento",
        "status": "em andamento",
        "prazo": "2025-03-10",
        "prioridade": "Alta",
        "responsavel": "Nicolas"
    },
    {
        "id": 2,
        "titulo": "Estudar Flask",
        "descricao": "Estudar Flask para aprender sobre Web Services",
        "status": "Nao iniciado",
        "prazo": "2025-03-18",
        "prioridade": "Baixa",
        "responsavel": "Nicolas"
    }
]
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return tarefas

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') ==task_id:
            return tarefa

    return 'Tarefa não encontrada'

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1
    task['id'] = ultimo_id
    tarefas.append(task)
    return task

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa

    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['prazo'] = task_body.get('prazo')
    task_search['prioridade'] = task_body.get('prioridade')
    task_search['responsavel'] = task_body.get('responsavel')

    return task_search
#Explicação do que aconteceu: primeiro criei a rota e coloquei o metodo 'delete'. O global é só para falar que mudaremos a tarefa no código inteiro, ou seja, não será uma modificação local. Depois usei o for e o in para criar uma listaque exclui a tarefa de acordo como id. Depois só coloquei um JSON pra falar que foi deletado. De resto eu coloquei no insomnia
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa.get('id') != task_id]
    return {'message': 'Tarefa excluída com sucesso'}

if __name__ == '__main__':
    app.run(debug=True)