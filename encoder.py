#pip install pyjwt

import jwt
key = "laper"
encoded = jwt.encode({"a": 7, "b": 4}, key, algorithm="HS256")
print(encoded)
#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhIjo3LCJiIjo0fQ.0rxwOjzvcOrI8QBxqnMtfX2VL9coCpeR5yRUZ5AO5po
