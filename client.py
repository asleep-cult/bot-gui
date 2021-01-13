import threading
import mainscreen
from lib import Client


class Client(Client):
    def __init__(self):
        self.window = mainscreen.MainWindow(self)
        super().__init__()

    def start(self, token):
        self.thread = threading.Thread(
            target=super().start,
            args=(token,),
            daemon=True
        )
        self.thread.start()

    async def guild_create(self, guild):
        print(guild.id)


if __name__ == '__main__':
    client = Client()
    client.window.start()
