import logging

import azure.functions as func

import json
import os
import io

# Import helper script
from . import predict

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    image_url = req.params.get('img')

    if image_url == "" :
        return func.HttpResponse(
            "Please pass a link on the query string or in the request body",
            status_code=400
        )

    # Initialize model
    predict.initialize()

    
    # Scoring step
    results = predict.predict_url(image_url)

    if image_url:
        return json.dumps(results)
    else:
        return func.HttpResponse(
             "Please pass a link on the query string or in the request body",
             status_code=400
        )
