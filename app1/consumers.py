from channels.generic.websocket import AsyncWebsocketConsumer

class YourConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Identifiez l'utilisateur connecté
        user = self.scope['user']

        # Faites quelque chose avec les informations de l'utilisateur connecté
        print(f"L'utilisateur {user} s'est connecté.")

        await self.accept()

    async def disconnect(self, close_code):
        # Identifiez l'utilisateur déconnecté
        user = self.scope['user']

        # Faites quelque chose avec les informations de l'utilisateur déconnecté
        print(f"L'utilisateur {user} s'est déconnecté.")

        # Appelez la méthode parent pour gérer la déconnexion
        await super().disconnect(close_code)
