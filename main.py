import json
import os

directories = os.listdir()
channels = []
id = None

directories.remove("index.json")
directories.remove("main.py")
directories.remove("discord-checkpoint-scuffed")

tempId = None
tempNumber = None
tempIndexJsonFile = None
type = None
counter = 0
totalMsg = 0

results_servers = []
results_dm = []

year = input("Hello, please input a year (YYYY format) : ")


print("---------")
print("Might take a second.. hang on tight.. (stream TWICE while you're at it)")
for directory in directories:
    channelString = directory + "/channel.json"
    messagesString = directory + "/messages.json"
    # print(f"trying to read {channelString} and {messagesString}")
    with open(messagesString, "r", encoding="utf-8") as file:
        msgJson = json.load(file)
        # print(f"{len(msgJson)} messages found")
        counter = 0
        for line in msgJson:
            if line["Timestamp"][0:4] == year:
                counter += 1
    with open(channelString, "r", encoding="utf-8") as file:
        jsonfile = json.load(file)
        id = jsonfile["id"]
        tempId = jsonfile["id"]
        type = jsonfile["type"]
    with open("index.json", "r", encoding="utf-8") as file:
        indexJsonFile = json.load(file)
        # print(f"{indexJsonFile[id]}")
        tempIndexJsonFile = indexJsonFile[id]
    if counter != 0:
        totalMsg += counter
        if type in ["GUILD_VOICE", "PUBLIC_THREAD", "GUILD_TEXT"]:
            results_servers.append((counter, tempIndexJsonFile))
        elif type == "DM":
            results_dm.append((counter, tempIndexJsonFile))
print("---------")

results_servers.sort(key=lambda x: x[0], reverse=True)
results_dm.sort(key=lambda x: x[0], reverse=True)

print("--- SERVERS ---")
for result in results_servers:
    print(f"{result[1]} | {result[0]} messages")
print("--- DMs ---")
for result in results_dm:
    print(f"{result[1]} | {result[0]} messages")
print(f"You have sent {totalMsg}...")
