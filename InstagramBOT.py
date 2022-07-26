from instabot import Bot

x = 0
y = 10

while x < y:
    bot = Bot()
    bot.login(username="UsuárioDoInstagram", password="SenhaDoInstagram")
    bot.send_message("Mensagem", ["usuarioY"]) # Mensagem é autoexplicativo - usuárioY é o destinatário 
    x += 1
