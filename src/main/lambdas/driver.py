import json
from src.main.lambdas.utils.aws import update_item_status_dynamo,get_secret,update_item_data_dynamo
from src.main.lambdas.utils.logs import logger
from src.main.lambdas.utils.google import search_image

def lambda_handler(event,context):
    if event:
        try:
            raw_message = event['Records'][0]['Sns']['Message']
            message = json.loads(raw_message)
            query = message['query']
            execution_id = message['execution_id']

            update_item_status_dynamo(execution_id,'puppy','executing')

            google_secrets = get_secret('google_search_engine')

            link = search_image(google_secrets,query)

            link_map = {
                'link': link
            }

            update_item_data_dynamo(execution_id,'puppy',link_map)


        except Exception as e:
            update_item_status_dynamo(execution_id,'puppy','failed')
            logger.error(str(e))
        else:
            update_item_status_dynamo(execution_id,'puppy','loaded')
