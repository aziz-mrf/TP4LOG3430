import os

# Define your commits here (bad = tests fail, good = tests pass)
BAD_COMMIT = "1d8748281263e8e7efe7b85c828cd3f600d96bfc"
GOOD_COMMIT = "a9f20e8a511665d81967342e7829e737395944d3"

os.system(f"git bisect start {BAD_COMMIT} {GOOD_COMMIT}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")