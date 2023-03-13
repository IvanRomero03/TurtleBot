from flask import Flask, request, Response
from RedisDB import RedisDB
import json
import dotenv
import os
from Parser import Parser
from util import randomHash

dotenv.load_dotenv()

RedisClient = RedisDB(os.getenv("REDIS_HOST"), os.getenv("REDIS_PORT"), os.getenv("REDIS_DB"), os.getenv("REDIS_USERNAME"), os.getenv("REDIS_PASSWORD")) 
parser = Parser()

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST' :
        # Content-Type: application/json
        # {"text": "fd 100"}
        text = request.get_json()
        textInput = text["text"]
        print(textInput)
        query = parser.parse(textInput)
        parser.execute()
        parser.save("temp.svg")
        # Save Query to Redis DB to a hashed key
        hash = randomHash(10)
        RedisClient.set(hash, str(query))
        # read SVG file and return it
        with open("temp.svg", "r") as f:
            svg = f.read()
        return Response(svg, mimetype='image/svg+xml')

@app.route('/health', methods=['GET'])
def health():
    return "OK"


    

if __name__ == "__main__":
    app.run()