import json

# "banco de dados" em memória
tasks = [
    {"id": 1, "task": "Estudar Python", "done": False},
    {"id": 2, "task": "Deploy na Vercel", "done": True},
]

def handler(request):
    # GET → lista tarefas
    if request["method"] == "GET":
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(tasks)
        }
    
    # POST → cria nova tarefa
    if request["method"] == "POST":
        try:
            data = json.loads(request["body"])
            new_task = {
                "id": len(tasks) + 1,
                "task": data.get("task"),
                "done": False
            }
            tasks.append(new_task)
            return {
                "statusCode": 201,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps(new_task)
            }
        except Exception as e:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": str(e)})
            }

    return {
        "statusCode": 405,
        "body": json.dumps({"error": "Método não permitido"})
    }
