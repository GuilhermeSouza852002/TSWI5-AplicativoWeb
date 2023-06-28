# locust -f teste_sistema.py --host=http://localhost:5000
#Importação
from locust import HttpUser, task, between

#classe representa um usuário simulado que fará as requisições HTTP.
class MyUser(HttpUser):
    wait_time = between(1, 3)   #define o tempo de espera entre as tarefas executadas pelo usuário

    #é uma tarefa que o usuário simulado executará
    @task
    def my_task(self):
        response = self.client.get('/my_endpoint')  #envia uma requisição GET para o endpoint /my_endpoint usando o cliente HTTP fornecido pela classe
        if response.status_code == 200:
            #evento de sucesso
            self.locust.events.request_success.fire(
                request_type="GET",
                name="/my_endpoint",
                response_time=response.elapsed.total_seconds() * 1000,
                response_length=len(response.content)
            )
        else:
            #evento de falha
            self.locust.events.request_failure.fire(
                request_type="GET",
                name="/my_endpoint",
                response_time=response.elapsed.total_seconds() * 1000,
                exception=response.raise_for_status()
            )

#Ambos os eventos registram métricas como o tipo de requisição, o tempo de resposta e o tamanho da resposta