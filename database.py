import csv

import crypt
import auth
import config

 ## Get a copy of the entire database
def read():
    rows = [] ## List that will contain database with decrypted fields

    with open(config.DATABASE_NAME) as db: ## Open the database file
        reader = csv.reader(db)
        for entry in reader:
            rows.append(entry)

    return rows ## Return the the database

def get_row(username, password):
    database = read()
    for (idx, row) in enumerate(database):
        if row[0] == username and row[1] == crypt.encrypt(password, password):
            return (idx, row)

    return -1

def write_data(data): ## Write desired data to current user's entry in the database
    (current_idx, current_row) = get_row(auth.get_current_user(), auth.get_current_pass())
    database = read()

    database[current_idx][2] = crypt.encrypt(data, auth.get_current_pass())

    with open(config.DATABASE_NAME, 'w') as dbfile: ## Open the database file
        writer = csv.writer(dbfile)
        writer.writerows(database)

    return True

def read_data(): ## Read the current user's data and return a decrypted copy of it
    (current_idx, current_row) = get_row(auth.get_current_user(), auth.get_current_pass())

    return crypt.decrypt(current_row[2], auth.get_current_pass())