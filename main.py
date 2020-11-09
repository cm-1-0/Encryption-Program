import os

from cryptography.fernet import Fernet

k1 = Fernet.generate_key()


def make_file():
    file1 = open("Key for Encryption Program", "wb")
    file1.write(k1)
    file1.close()


def read_file():
    file1 = open("Key for Encryption Program", "rb")
    file1.read()
    file1.close()


def remove_file():
    os.remove("Key for Encryption Program")


print("Welcome to the Encryption Program")

q1 = input("Would you like to start?: ")

if q1 == "Yes":
    make_file()
    print("Check the file to find key.")
    q2 = input("Would you like to encrypt a message?: ")

    if q2 == "Yes":
        k2 = k1.decode()
        print("Check the file for the key")
        q3 = input("Type the key: ")
        remove_file()

        if q3 == k2:
            message = input("Enter message: ")
            encode = message.encode()
            f1 = Fernet(k1)
            encrypt1 = f1.encrypt(encode)
            print(encrypt1)
            print("Welcome to the Decryption Program")
            q4 = input("Would you like to decrypt the byte?: ")

            if q4 == "Yes":
                start_key = Fernet(k1)
                decode = start_key.decrypt(encrypt1)
                print(decode)

            if q4 == "No":
                print("This program has ended")

        if q3 != k2:
            print("Wrong key")

    if q2 == "No":
        remove_file()
        print("This program has ended.")

if q1 == "No":
    print("This program has ended.")


