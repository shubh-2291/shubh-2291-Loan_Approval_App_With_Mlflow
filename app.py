from app import application
from app.apis import *

if __name__ == "__main__":
    application.run(port = 8080)
    # application.run(debug = True, port = 8080)