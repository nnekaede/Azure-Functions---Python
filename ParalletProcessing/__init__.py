import logging
import collections
from pprint import import pprint

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    teammate = collections.namedtuple('teammate', [
            'first',
            'last',
            'position',
            'email', ])
    Team = (
        teammate(first='Nneka', last='Ede', position='Automation Anaylst', email='nneka.ede@chevron.com'),
        teammate(first='Nivea', last='Tejada', position='Automation Anaylst', email='nneka.ede@chevron.com'),
        teammate(first='Kieth', last='Keller', position='Automation Anaylst', email='nneka.ede@chevron.com'),
        teammate(first='Alvina', last='Fletcher', position='Automation Anaylst', email='nneka.ede@chevron.com'),
        teammate(first='Carlito', last='Vedan', position='Automation Anaylst', email='nneka.ede@chevron.com'),
    )

    import time

    def transform(x):
        return {'last': x.last, 'first': x.first}

    result = tuple(map(
        transform,
        team
    ))

    if name:
        return func.HttpResponse("result")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
