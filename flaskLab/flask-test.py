import flask

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'

@app.route('/pop/<abbrev>')
def state_pop(abbrev):
    conn = psycopg2.connect(
                host="localhost",
                port=5432,   
                database="rapaczs",
                user="rapaczs",
                password="chip979bond")
        
        if conn is not None:
                print( "Connection Worked!" )
        else:
                print( "Problem with Connection" )
                conn.close()
                return None
              
        cur = conn.cursor()

        abbrev = abbrev.upper()

        sql = "SELECT pop FROM statepopulation WHERE code = %s;"

        statedata = (state, )
        cur.execute( sql, statedata )

        if cur.fetchone() is not None:
            pop = cur.fetchone[0]
            cur.close()
            conn.close()
            return pop
        else:
            cur.close()
            conn.close()
            return None

if __name__ == '__main__':
    my_port = 5123
    app.run(host = '0.0.0.0', port = my_port) 
