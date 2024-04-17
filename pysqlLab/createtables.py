import psycopg2

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
          return None
      
cur = conn.cursor()

sql = "DROP TABLE IF EXISTS statepopulation; CREATE TABLE statepopulation (code text, statename text, pop real); DROP TABLE IF EXISTS topcities; CREATE TABLE topcities (city text, statename text, citypop real, lat real, lon real);"
    
cur.execute( sql )

return None
