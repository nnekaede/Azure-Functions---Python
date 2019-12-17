import logging

import azure.functions as func

import json
import os
import io
#import sys
#from os import path
#sys.path.append('C:\Users\neua\source\repos\Azure Functions - Python - ACOEPython\dog-classfication')
#sys.path.append('/home/site/wwwroot') 
#sys.path.append(path.dirname(path.dirname(__file__)))
#from __app__.SharedCode import predict
# Import helper script
#from predict import initialize
from . import predict
#from predit import initialize

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    from . import predict
    image_url = req.params.get('img')

    if image_url == "" :
        return func.HttpResponse(
            "Please pass a link on the query string or in the request body",
            status_code=400
        )
    else:
        # Initialize model
        predict.initialize()

        
        # Scoring step
        results = predict.predict_url(image_url)
        return json.dumps(results)

