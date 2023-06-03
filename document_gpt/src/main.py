from flask import Flask, request

from document_gpt.helper.conversation import create_conversation
from document_gpt.helper.messenger_api import send_message

from config import config

qa = create_conversation()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'OK', 200

@app.route('/facebook', methods=['GET'])
def facebook_verify():
    args = request.args.to_dict()

    mode = args['hub.mode']
    verify_token = args['hub.verify_token']
    challenge = args['hub.challenge']

    if mode == 'subscribe' and verify_token == config.FB_VERIFY_TOKEN:
        print('Webhook verified.')
        return challenge, 200
    else:
        return 'BAD_REQUEST', 403
    

@app.route('/facebook', methods=['POST'])
def facebook_messenger():
    try:
        # TODO
        # Get the sender id and query from the request
        body = request.get_json()
        sender_id = body['entry'][0]['messaging'][0]['sender']['id']
        query = body['entry'][0]['messaging'][0]['message']['text']
        print(sender_id, query)
        # TODO
        # get the user
        # if not create
        # create chat_history from the previous conversations
        res = qa(
            {
            'question': query,
            'chat_history': {}
            }
        )
        print(res)
        # TODO
        # send message
        send_message(sender_id, res['answer'])
    except:
        pass

    return 'OK', 200
