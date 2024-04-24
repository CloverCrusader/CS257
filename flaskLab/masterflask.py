import flask
import random
import psycopg2

app = flask.Flask(__name__)

# Hellow World
@app.route('/hello')
def my_function():
    return "Hello World!"

# Two words
@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

# Colored word
@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:#121a40">' + word1 + '</h1>'

# Add two numbers
@app.route('/add/<num1>/<num2>')
def add_num(num1, num2):
    return str(int(num1) + int(num2))

# State population
@app.route('/pop/<abbrev>')
def state_pop(abbrev):
    conn = psycopg2.connect(
                host="localhost",
                port=5432,   
                database="rapaczs",
                user="rapaczs",
                password="chip979bond")
        
    if conn is None:
        conn.close()
        return None
            
    cur = conn.cursor()

    abbrev = abbrev.upper()

    sql = "SELECT pop FROM statepopulation WHERE code = %s;"

    statedata = (abbrev, )
    cur.execute( sql, statedata )

    if cur.fetchone() is not None:
        pop = cur.fetchone()[0]
        cur.close()
        conn.close()
        return str(pop)
    else:
        cur.close()
        conn.close()
        return None

# Random number
@app.route('/rand/<low>/<high>')
def rand(low, high):
    #Input values that come from a URL (i.e., @app.route)
    #   are always strings so I need to convert the type to int
    low_int = int(low)
    high_int = int(high)
    
    num = random.randint(low_int, high_int)
    return flask.render_template("random.html", randNum = num)

@app.route('/random')
def welcome():
    return flask.render_template("newrandom.html")

# A frog
@app.route('/frog')
def frog():
    return flask.render_template("frog.html")

if __name__ == '__main__':
    my_port = 5123
    app.run(host = '0.0.0.0', port = my_port)