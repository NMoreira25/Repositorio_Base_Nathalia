import sqlite3


banco = sqlite3.connect('farmacia.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE Farmacia (remedio TEXT, preço REAL, fabricação INTEGER)")

cursor.execute("INSERT INTO Farmacia Values('Soro Fisiologico', 8.99, 2024)")
cursor.execute("INSERT INTO Farmacia Values('Esfoliante', 59.99, 2025 )")
cursor.execute("INSERT INTO Farmacia Values('Creme SalonLine', 23.68, 2024)")
cursor.execute("INSERT INTO Farmacia Values('Vitamina C', 23.11, 2025)")
cursor.execute("INSERT INTO Farmacia Values('Loratadina', 7.19, 2024)")


cursor.execute("SELECT * FROM Farmacia")
print(cursor.fetchall())


banco.commit()