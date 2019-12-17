import logging
import collections
import multiprocessing
from pprint import pprint

import azure.functions as func
import time


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

    def transform(x):
        time.sleep(1)
        res = {'last': x.last, 'first': x.first, 'email': x.email}
        return res
    
    teammate = collections.namedtuple('teammate', [
            'first',
            'last',
            'position',
            'email', ])

    Team = (
        teammate(first='Nneka', last='Ede', position='Automation Anaylst', email='nneka.ede@chevron.com'),
        teammate(first='Nivea', last='Tejada', position='Automation Anaylst', email='nivea.tejada@chevron.com'),
        teammate(first='Kieth', last='Keller', position='Automation Anaylst', email='keith.keller@chevron.com'),
        teammate(first='Alvina', last='Fletcher', position='Automation Anaylst', email='nneka.ede@chevron.com'),
        teammate(first='Carlito', last='Vedan', position='Automation Anaylst', email='nneka.ede@chevron.com'),
    )

    start = time.time()
    
    pool = multiprocessing.Pool()
    result = pool.map(transform, Team)

    result = tuple(map(
        transform,
        Team
    ))

    end = time.time()
    
    if name:
        return {f'Time to complete {end - start}'}
    else:
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body",
            status_code=400
        )
