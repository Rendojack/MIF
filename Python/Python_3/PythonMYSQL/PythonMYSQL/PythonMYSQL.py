import mysql.connector

db = mysql.connector.connect(host='sql11.freemysqlhosting.net', database='sql11222975', 
    user='sql11222975', password='pMKKaeHBtT')

cursor = db.cursor()

#cursor.execute("""CREATE TABLE IF NOT EXISTS Studentas(
#    StudentoID INT PRIMARY KEY,
#    Vardas TEXT,
#    Pavarde TEXT,
#    Kursas INT)""")

#cursor.execute("""INSERT IGNORE INTO Studentas (studentoid, vardas, pavarde, kursas) 
#    values (%s, %s, %s, %s)""", (1510740, 'vardenis1', 'pavardenis1', 3))
#cursor.execute("""INSERT IGNORE INTO Studentas (studentoid, vardas, pavarde, kursas) 
#    values (%s, %s, %s, %s)""", (1510741, 'vardenis2', 'pavardenis2', 4))
#cursor.execute("""INSERT IGNORE INTO Studentas (studentoid, vardas, pavarde, kursas) 
#    values (%s, %s, %s, %s)""", (1510742, 'vardenis3', 'pavardenis3', 1))

#cursor.execute("""DELETE IGNORE FROM Studentas WHERE kursas = 3""")

#cursor.execute("""DELETE IGNORE FROM Studentas""")

#cursor.execute("""DROP TABLE IF EXISTS Studentas""")
db.commit()
    

