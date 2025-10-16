import sqlite3


banco = sqlite3.connect('Clinica_medica.db')

cursor = banco.cursor()

# cursor.execute("CREATE TABLE Clinica_Medica (medicos TEXT, especialidade TEXT, pacientes TEXT, consultas DATE )")

cursor.execute("INSERT INTO Clinica_Medica Values('Fabricio','Odontologia','Daniella Monteiro','10-10-2025')")
cursor.execute("INSERT INTO Clinica_Medica  Values('Samira','Cardiovalogista','Pedro Henrique','23-11-2025' )")
cursor.execute("INSERT INTO Clinica_Medica Values('Manuela','Dermatologista','Sarah Souza','12-12-2025')")
cursor.execute("INSERT INTO Clinica_Medica Values('Caio','Neurologista','Diego Rita','25-11-2025')")
cursor.execute("INSERT INTO Clinica_Medica Values('Pamela','Ortopedista','Camila Rita','07-11-2025')")


cursor.execute("SELECT * FROM Clinica_Medica")
print(cursor.fetchall())


banco.commit()