import json
import boto3
from datetime import datetime
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("favourite_orgs")


def add_favourite(event, context):
    try:
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
    except KeyError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Request with missing params: {str(e)}"}),
        }
    except ValueError as e:
        return {
            "statusCode": 400,
            "body": json.dumps(
                {"error": f"org_id and favourite_org_id must be integers: {str(e)}"}
            ),
        }
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"AWS client error: {str(e)}"}),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Unexpected error: {str(e)}"}),
        }


def list_favourites(event, context):
    try:
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
                        "error": "The organization does not have any favorite organizations"
                    }
                ),
            }

        # Convert possible Decimal types to int, for JSON serialization
        for item in favorites:
            item["org_id"] = int(item["org_id"])
            item["favourite_org_id"] = int(item["favourite_org_id"])

        return {"statusCode": 200, "body": json.dumps(favorites)}
    except KeyError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "org_id param required"}),
        }
    except ValueError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "org_id must be an integer"}),
        }
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"AWS client error: {str(e)}"}),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Unexpected error: {str(e)}"}),
        }
