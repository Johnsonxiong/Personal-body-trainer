import os, slackclient

PBTCB_SLACK_NAME = os.environ.get('PBTCB_SLACK_NAME')
PBTCB_SLACK_TOKEN = os.environ.get('PBTCB_SLACK_TOKEN')

# initialize slack client
PBTCB_slack_client = slackclient.SlackClient(PBTCB_SLACK_TOKEN)

# check if everything is alright
print(PBTCB_SLACK_NAME)
print(PBTCB_SLACK_TOKEN)
is_ok = PBTCB_slack_client.api_call("users.list").get('ok')
print(is_ok)

# find the id of our slack bot
if(is_ok):
    for user in PBTCB_slack_client.api_call("users.list").get('members'):
        if user.get('name') == PBTCB_SLACK_NAME:
            print(user.get('id'))
