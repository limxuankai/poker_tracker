import sqlite3, datetime

def sqlquery(query, params=None):
    con = sqlite3.connect('Clients.db')
    cur = con.cursor()
    
    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)
        
    if "SELECT" in query.upper():  
        res = cur.fetchall()
    else:
        res = None

    con.commit()
    cur.close()  
    con.close()
    return res