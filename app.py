# save this as app.py
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)




# a = 10
# b = 101

# print(a == b)  # Equal to: Checks if a is equal to b (False)
# print(a != b)  # Not equal to: Checks if a is not equal to b (True)
# print(a > b)   # Greater than: Checks if a is greater than b (False)
# print(a < b)   # Less than: Checks if a is less than b (True)
# print(a >= b)  # Greater than or equal to: Checks if a is greater than or equal to b (False)
# print(a <= b)  # Less than or equal to: Checks if a is less than or equal to b (True)

