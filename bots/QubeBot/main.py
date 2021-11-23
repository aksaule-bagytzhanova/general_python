import config
import telebot

bot = telebot.TeleBot(config.TOKEN)
black_list_text = ['join', 'https://t.me/joinchat/', 'click on', 'join', 'follow', 'https://t.me/', 'https://nft-punks.net/']
while_list_text = ['https://theqube.cc', 'https://github.com/github-qubecs/documents/blob/main/qube-whitepaper-1.0.pdf',
                   'https://qubecs.com/', 'https://medium.com/@qubecryptospace', 'https://twitter.com/qubecryptospace',
                   'https://www.reddit.com/user/QUBE_cc', 'https://t.me/qubecryptospace', 'https://github.com/github-qubecs/'
                   'https://etherscan.io/address/0x3e9d6430144485873248251fcb92bd856e95d1cd#code',
                   'https://bscscan.com/address/0x3e9d6430144485873248251fCB92bD856E95D1CD#code']
while_list_username = ['nveretenov', 'just_aksi']


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    op = ''.join("%s" % ''.join(map(str, x)) for x in message.text)
    op = op.split(' ')
    if message.from_user.username not in while_list_username:
        for i in op:
            if i in black_list_text and i not in while_list_text:
                bot.delete_message(message.chat.id, message.message_id)
                break
            for io in black_list_text:
                if i.startswith(io) and i not in while_list_text:
                    bot.delete_message(message.chat.id, message.message_id)
                    break


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    user_name = message.new_chat_member.first_name
    user_surn = message.new_chat_member.last_name
    bot.send_message(message.chat.id, "Добро пожаловать, {0} {1}!".format(user_name, user_surn))
    #bot.send_message(message.from_user.id, "Добро пожаловать, {0}!".format(user_name))
    #bot.send_message(message.chat.id, op)



if __name__ == '__main__':
    bot.polling(none_stop=True)