import crypt
import config
import csv
import database

print("New User Generator")

print("Username: ", end='')
username = input()

print("Password: ", end='')
password = input()

print("Data: ", end='')
data = input()

db = database.read()

db.append([username, crypt.encrypt(password, password), crypt.encrypt(data, password)])

with open(config.DATABASE_NAME, 'w') as dbfile:
    writer = csv.writer(dbfile)
    writer.writerows(db)

print("Done!")