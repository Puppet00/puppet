import os 


def get_user_agents():
    uagent_file = open("user-agents.txt", "r")
    uagent = [ line.replace("\n", "") for line in uagent_file ]
    uagent_file.close()
    return uagent


def get_headers_data():
    headers_file = open("headers.txt", "r")
    data = headers_file.read()
    headers_file.close()
    return data

def get_my_bots():
    bots_file = open("bots.txt", "r")
    bots = [ line.replace("\n", "") for line in bots_file ]
    bots_file.close()
    return bots
