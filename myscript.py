import os

# Define your commits here (bad = tests fail, good = tests pass)
BAD_COMMIT = "c1a4be04b972b6c17db242fc37752ad517c29402"
GOOD_COMMIT = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

os.system(f"git bisect start {BAD_COMMIT} {GOOD_COMMIT}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")