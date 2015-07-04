__author__ = 'rotem'
import bcrypt


def hash_password(password_str, rounds=12):
    return bcrypt.hashpw(password_str, bcrypt.gensalt(rounds))


def check_password(password_str, hashed):
    return bcrypt.hashpw(password_str, hashed) == hashed

