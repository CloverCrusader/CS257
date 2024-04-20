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
        # query 1
        sql = "SELECT city, lat, lon FROM topcities WHERE city = 'Northfield';"
            
        cur.execute( sql )

        if cur.fetchone() is not None :
            print("Northfield: latitude = " + cur.fetchone()[1] + "; longitude = " + cur.fetchone()[2] + ";\n")
        else :
            print("Northfield is not a top city.\n")

        # query 2
        sql = "SELECT city FROM topcities ORDER BY citypop DESC;"
            
        cur.execute( sql )
        
        print("Largest population center: " + cur.fetchone()[0] + "\n")

        # query 3
        sql = "SELECT city FROM topcities WHERE statename = 'Minnesota' ORDER BY citypop DESC;"

        cur.execute( sql )

        print("The smallest Minnesota city to make the top 1000 US cities: " + cur.fetchone()[0] + "\n")
        
        # query 4
        sql = "SELECT city, statename FROM topcities ORDER BY lat DESC;" # get north

        cur.execute( sql )

        print("Northernmost city in the top 1000: " + cur.fetchone()[0] + ", " + cur.fetchone()[1] + "\n")

        sql = "SELECT city, statename FROM topcities ORDER BY lat;" # get south

        cur.execute( sql )

        print("Southernmost city in the top 1000: " + cur.fetchone()[0] + ", " + cur.fetchone()[1] + "\n")

        sql = "SELECT city, statename FROM topcities ORDER BY lon DESC;" # get east

        cur.execute( sql )

        print("Easternmost city in the top 1000: " + cur.fetchone()[0] + ", " + cur.fetchone()[1] + "\n")

        sql = "SELECT city, statename FROM topcities ORDER BY lon;" # get west

        cur.execute( sql )

        print("Westernmost city in the top 1000: " + cur.fetchone()[0] + ", " + cur.fetchone()[1] + "\n")

        # query 5
        state = input("Enter state name or abbreviation:\n")

        if len(state) == 2 : # converts abbreviation to statename
            state = state.upper()

            sql = "SELECT statename FROM statepopulation WHERE code = %s;"

            statedata = (state, )
            cur.execute( sql, statedata )
            
            if cur.fetchone() is not None:
                state = cur.fetchone()[0]
            else:
                print("That is not a valid abbreviation.\n")
                cur.close()
                conn.close()
                return None
        
        state = state.capitalize()

        sql = "SELECT citypop FROM topcities WHERE statename = %s;"

        statedata = (state, )
        cur.execute( sql, statedata )

        list = cur.fetchall()
        
        if cur.fetchall() is not None:
            tally = 0

            for row in list:
                tally = tally + row[0]

            print("The population of " + state + " that lives in the top 1000 US cities: " + str(tally) + "\n")
        
        else:
            print("That is not a valid state name.\n")
            
        cur.close()
        conn.close()

        return None

# run main
if __name__ == "__main__":
        main()
