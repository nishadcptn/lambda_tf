import json
import random


def scramble(body: str) -> str:
    text = json.loads(body)
    return "".join(random.sample(text["text"], len(text["text"])))


def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"result": scramble(event["body"])}),
    }


if __name__ == "__main__":
    pass