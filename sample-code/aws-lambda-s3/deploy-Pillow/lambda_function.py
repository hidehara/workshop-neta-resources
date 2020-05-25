import json
from PIL import Image

def lambda_handler(event, context):

    print(type(Image))

    return {
        'statusCode': 200,
        'body': json.dumps('Ready to use PIL(Pillow) on Lambda!')
    }
