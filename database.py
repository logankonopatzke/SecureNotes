import csv

import crypt
import config

 ## Get a copy of the entire database with all fields in decrypted plaintext
def read():
    rows = [] ## List that will contain database with decrypted fields

    with open(config.DATABASE_NAME) as db: ## Open the database file
        reader = csv.reader(db)
        for entry in reader:
            entry[1] = crypt.decrypt(entry[1], "") ## Decrypt the password field
            entry[2] = crypt.decrypt(entry[2], "") ## Decrypt the data field
            rows.append(entry) ## 

    return rows ## Return the the database

def write_data(data): ## Write desired data to current user's entry in the database
    return

def read_data(): ## Read the current user's data and return a decrypted copy of it
    return