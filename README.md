# Backend Practice with AWS

![Amazon AWS Badge](https://img.shields.io/badge/Amazon%20AWS-232F3E?logo=amazonaws&logoColor=fff&style=for-the-badge) ![Amazon API Gateway Badge](https://img.shields.io/badge/Amazon%20API%20Gateway-FF4F8B?logo=amazonapigateway&logoColor=fff&style=for-the-badge) ![AmazonDynamoDB](https://img.shields.io/badge/Amazon%20DynamoDB-4053D6?style=for-the-badge&logo=Amazon%20DynamoDB&logoColor=white) ![AWS Lambda Badge](https://img.shields.io/badge/AWS%20Lambda-F90?logo=awslambda&logoColor=fff&style=for-the-badge) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Serverless Badge](https://img.shields.io/badge/Serverless-FD5750?logo=serverless&logoColor=fff&style=for-the-badge)

This is a backend practice project utilizing AWS and Serverless framework with Python to build a REST API. It allows an organization to add as a favourite another one and list all its favourite ones.

## Add Favourite Organization

#### Request

- **Method:** `POST`
- **Endpoint:** `https://2bzdj9d9za.execute-api.us-east-1.amazonaws.com/dev/add-favourite`
- **Headers:** 
  - `x-api-key`: API key required, ask for it

#### Request Body Example

```json
{
    "org_id": 805,
    "favourite_org_id": 26
}
```

#### Response

- **Status Codes:**
  - `200 OK`: Organization added to favourites successfully
  - `400 Bad Request`: Missing parameters or invalid data
  - `500 Internal Server Error`: Unexpected error


## List Favourite Organizations

#### Request

- **Method:** `GET`
- **Endpoint:** `https://2bzdj9d9za.execute-api.us-east-1.amazonaws.com/dev/list-favourites`
- **Headers:** 
  - `x-api-key`: API key required, ask for it
- **Query Parameters:**
  - `org_id`: Numeric value indicating the organization id

#### Response

- **Status Codes:**
  - `200 OK`: Returns the list of favourite organizations
  - `400 Bad Request`: Missing or invalid org_id parameter
  - `404 Not Found`: No favourite organizations found for the given org_id
  - `500 Internal Server Error`: Unexpected error

```json
[
    {
    "org_id": 1,
    "date": "2024-03-21 23:48:26",
    "favourite_org_id": 33
    }
]
```
