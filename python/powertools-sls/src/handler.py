import boto3
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import *
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger(service="TestApp")
tracer = Tracer(service="TestApp")
app = APIGatewayHttpResolver()

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('inventory')


@app.get("/hello/<name>")
@tracer.capture_method
def hello_name(name):
    tracer.put_annotation(key="User", value=name)
    logger.info(f"Request from {name} received")
    return {"message": f"hello {name}!"}


@app.get("/hello")
@tracer.capture_method
def hello():
    tracer.put_annotation(key="User", value="unknown")
    logger.info("Request from unknown received")
    return {"message": "hello unknown!"}


@app.post("/add")
@tracer.capture_method
def addToDynamo():
    to_add: dict = app.current_event.json_body
    tracer.put_annotation(key="Add Post", value=str(to_add))
    logger.info("Add Request received with object", to_add)

    # check for malformed json in toAdd
    item_dict = {
        'pk': to_add['pk'],
        'sk': f"{to_add['uuid']}",
    }

    for key in to_add.keys():
        if key == 'PK' or key == 'uuid': continue
        item_dict[key] = to_add[key]

    res = table.put_item(Item=item_dict)
    return res

@app.get("/")
@tracer.capture_method
def defaultMethod():
    return {
        "statusCode": 200,
        "body": {
            "message": "Congratulations! You have deployed and tested a Lambda using DiBs"
        }
    }


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST, log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return app.resolve(event, context)