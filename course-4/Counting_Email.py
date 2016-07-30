import sqlite3
import re

conn = sqlite3.connect('org.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From:') : continue
    org = re.findall("@(.+)",line)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org[0].strip(), ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES ( ?, 1 )''', (org[0].strip(), ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (org[0].strip(), ))

conn.commit()
cur.close()
