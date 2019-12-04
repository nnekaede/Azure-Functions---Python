import logging

import azure.functions as func
import mimetypes
from bs4 import BeautifulSoup
import urllib.request


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

    htmlfile = open("/home/site/repository/demohtml.html", 'r', encoding='utf-8')
    source = htmlfile.read()
    #print(source)
    soup = BeautifulSoup(source, 'html.parser')
    greeting = soup.find(id='greeting')
    print("COMMENTS BELOW:")
    print(greeting)
    greeting.string.replace_with('Hi '+ name)
    greeting = soup.find(id = 'greeting')
    #print(source)
    with open("/home/site/repository/demohtml.html", "w") as file:
        file.write(str(soup))
    htmlfile.close()
    if name:
        #return func.HttpResponse(f"Hello {name}!")
        path = "/home/site/repository/demohtml.html" # or other paths under `MyFunctionProj`
        filename = f"{path}"
        #filename = f"{path}/{name}"
        with open(filename, 'rb') as f:
            mimetype = mimetypes.guess_type(filename)
            return func.HttpResponse(f.read(), mimetype=mimetype[0])
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
# C:\Users\neua\OneDrive - Chevron\Documents\azurefunctionsunavalible.html