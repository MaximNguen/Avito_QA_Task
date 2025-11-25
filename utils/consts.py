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

    create_payload_no_sellerID = {
        "sellerID": 1231231231231231231231231,
        "name": "Tests lsasas",
        "price": 888888,
        "statistics": {
          "likes": Generator.likes,
          "viewCount": Generator.viewCount,
          "contacts": Generator.contacts
        }
    }

    create_payload_with_negative_price = {
        "sellerID": 12,
        "name": "Tests lsasas",
        "price": -888888,
        "statistics": {
          "likes": Generator.likes,
          "viewCount": Generator.viewCount,
          "contacts": Generator.contacts
        }
    }