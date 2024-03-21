import json
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("favourite_orgs")


def add_favourite(event, context):
    body = json.loads(event["body"])
    org_id = int(body["org_id"])
    favourite_org_id = int(body["favourite_org_id"])
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    response = table.put_item(
        Item={"org_id": org_id, "favourite_org_id": favourite_org_id, "date": date},
        ConditionExpression="attribute_not_exists(org_id) OR attribute_not_exists(favourite_org_id)",
    )

    return {
        "statusCode": 200,
        "body": json.dumps("Organization added to favourites successfully"),
    }


def list_favourites(event, context):
    org_id = int(event["queryStringParameters"]["org_id"])

    response = table.scan(
        FilterExpression=boto3.dynamodb.conditions.Attr("org_id").eq(org_id)
    )

    favorites = response["Items"]

    if not favorites:
        return {
            "statusCode": 404,
            "body": json.dumps(
                {
                    "error": "No favourite organizations found for the given org_id: " + str(org_id)
                }
            ),
        }

    return {"statusCode": 200, "body": json.dumps(favorites)}
