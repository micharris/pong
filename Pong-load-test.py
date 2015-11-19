from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):

    @task(1)
    def task1(self):
        self.client.get("events?assetId=00000&eventType=pageView&referal=twitter.com&platform=desktop")

    @task(1)
    def task2(self):
        self.client.get("events?assetId=00000&eventType=pageView&referal=twitter.com&platform=native")

    @task(1)
    def task3(self):
        self.client.get("events?assetId=00000&eventType=pageView&referal=twitter.com&platform=mobile")

    @task(1)
    def task4(self):
        self.client.get("events?assetId=00000&eventType=share&referal=twitter.com&platform=desktop")

    @task(1)
    def task5(self):
        self.client.get("events?assetId=00000&eventType=share&referal=twitter.com&platform=native")

    @task(1)
    def task6(self):
        self.client.get("events?assetId=00000&eventType=share&referal=twitter.com&platform=mobile")



class MyLocust(HttpLocust):
    task_set = MyTaskSet


