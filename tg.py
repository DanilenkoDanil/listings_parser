from telethon.sync import TelegramClient
from telethon import events
import json
import re
import time
import random
import check

with open("setting.json", 'r', encoding='utf8') as out:
    setting = json.load(out)

    client = TelegramClient(
        setting['account']['session'],
        setting['account']['api_id'],
        setting['account']['api_hash']
    )

    client.start()

dialogs = client.get_dialogs()

for index, dialog in enumerate(dialogs):
    print(f'[{index}] {dialog.name}')


first_channel = dialogs[int(input("First channel index: "))]
second_channel = dialogs[int(input("Second channel index: "))]
output_channel = dialogs[int(input("Output channel index: "))]


@client.on(events.NewMessage(chats=first_channel))
async def handler_first(event):
    print(event.message.text.split('Contract')[1].split("`")[1])
    contract_address = event.message.text.split('Contract')[1].split("`")[1]
    network = event.message.text.split('Platform')[1].split("`")[1]
    print(network)

    result_bs = check.scan_bs(contract_address, network)
    if check.scan_watcher(contract_address) and result_bs is not False:
        time.sleep(random.uniform(0, 3))
        message_for_output = event.message + '\n'
        try:
            for i in event.reply_markup.rows:
                message_for_output += i.buttons[0].url + '\n'
        except Exception as e:
            print(e)
        message_for_output += result_bs[0] + '\n'
        message_for_output += result_bs[1] + '\n'
        await client.send_message(output_channel, message_for_output)
        print("Сообщение отправлено")


@client.on(events.NewMessage(chats=second_channel))
async def handler_first(event):

    print(event.message.text.split('Contract')[1].split("`")[1])
    contract_address = event.message.text.split('Contract')[1].split("`")[1]
    network = event.message.text.split('Platform')[1].split("`")[1]
    print(network)

    result_bs = check.scan_bs(contract_address, network)
    if check.scan_watcher(contract_address) and result_bs is not False:
        time.sleep(random.uniform(0, 3))
        message_for_output = event.message + '\n'
        try:
            for i in event.reply_markup.rows:
                message_for_output += i.buttons[0].url + '\n'
        except Exception as e:
            print(e)
        message_for_output += result_bs[0] + '\n'
        message_for_output += result_bs[1] + '\n'
        await client.send_message(output_channel, message_for_output)
        print("Сообщение отправлено")

client.run_until_disconnected()
