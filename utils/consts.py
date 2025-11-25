from utils.generators import Generator

class Payloads:
    create_payload = {
        "sellerID": 12,
        "name": "Tests lsasas",
        "price": 888888,
        "statistics": {
          "likes": Generator.likes,
          "viewCount": Generator.viewCount,
          "contacts": Generator.contacts
        }
    }
    create_payload_wrong = {
        "sellerID": 12,
        "name": "Tests lsasas",
        "price": "888888",
        "statistics": {
          "likes": Generator.likes,
          "viewCount": Generator.viewCount,
          "contacts": Generator.contacts
        }
    }