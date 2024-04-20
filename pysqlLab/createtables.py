import psycopg2

def main():
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
        
        sql = "DROP TABLE IF EXISTS statepopulation; CREATE TABLE statepopulation (code text, statename text, pop real); DROP TABLE IF EXISTS topcities; CREATE TABLE topcities (city text, statename text, citypop real, lat real, lon real);"
            
        cur.execute( sql )
        
        cur.close()
        conn.close()

        return None

# run main
if __name__ == "__main__":
        main()
