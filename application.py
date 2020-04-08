import os
import os
import psycopg2

DATABASE_URL = os.environ['postgres://uproifqruttsfk:55353a88f46ed271746bbbe67ce0426f3ba979e96bc987a9e4f0e41b53ad6bda@ec2-34-206-252-187.compute-1.amazonaws.com:5432/d9oqhrkjof2h64']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__Saket__)

# Check for environment variable
if not os.getenv("postgres://uproifqruttsfk:55353a88f46ed271746bbbe67ce0426f3ba979e96bc987a9e4f0e41b53ad6bda@ec2-34-206-252-187.compute-1.amazonaws.com:5432/d9oqhrkjof2h64"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("postgres://uproifqruttsfk:55353a88f46ed271746bbbe67ce0426f3ba979e96bc987a9e4f0e41b53ad6bda@ec2-34-206-252-187.compute-1.amazonaws.com:5432/d9oqhrkjof2h64"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"

import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "of9H3ORO18UZNES6gbCNw", "isbns": "9781632168146"})
print(res.json())

{'books': [{
                'id': 29207858,
                'isbn': '1632168146',
                'isbn13': '9781632168146',
                'ratings_count': 0,
                'reviews_count': 1,
                'text_reviews_count': 0,
                'work_ratings_count': 26,
                'work_reviews_count': 113,
                'work_text_reviews_count': 10,
                'average_rating': '4.04'
            }]
}
