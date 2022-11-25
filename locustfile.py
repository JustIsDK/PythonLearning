from locust import HttpUser,task

class BridgeDemo(HttpUser):
    @task
    def GetChain(self):
        self.client.get("/bridge/chains")
