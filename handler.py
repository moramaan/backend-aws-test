import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('nombre_de_la_tabla_en_dynamodb')

# def add_favorite(event, context):
    # Code to add a favorite company

# def list_favorites(event, context):
    # Code to list favorite companies