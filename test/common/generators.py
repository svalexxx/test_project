"""Generators for tests"""

from random import choice, randint
from string import ascii_letters, digits, punctuation, ascii_lowercase, ascii_uppercase
from faker import Faker
from datetime import datetime, timedelta

cyrillic_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

max_int = 2147483647


def letters_string(count):
    return ''.join(choice(ascii_letters) for _ in range(count))


def lowercase_string(count):
    return ''.join(choice(ascii_lowercase) for _ in range(count))


def uppercase_string(count):
    return ''.join(choice(ascii_uppercase) for _ in range(count))


def digits_string(count):
    return ''.join(choice(digits) for _ in range(count))


def mixed_string(count):
    return ''.join(choice(ascii_letters + digits) for _ in range(count))


def first_digit_string(count):
    return str(randint(0, 9)) + mixed_string(count)


def punctuation_string(count):
    return ''.join(choice(punctuation) for _ in range(count))


def whitespace_string(count):
    return ''.join(' ' for _ in range(count))


def fake_full_name():
    faker = Faker(locale='RU')
    return faker.name()


def fake_surname():
    faker = Faker(locale='RU')
    return faker.name().split()[0]


def fake_name():
    faker = Faker(locale='RU')
    return faker.name().split()[1]


phone_numbers = ['76961466965', '76755210009', '76468402397', '79494553521',
                 '79973201905', '78180559470', '74506647869', '77837323756',
                 '73324889015', '78208242530', '79319709920', '78933487203',
                 '78108310760', '77797714572', '72613231370', '75427918262', '74071176418',
                 '74927967079', '73788871978', '70596257107', '78504607845',
                 '73178633559', '78038516662', '79021483152', '75735111148', '72601101348',
                 '71741817921', '76787505723', '75453154727', '70302303287']


def fake_phone_number():
    return choice(phone_numbers)


def fake_address():
    faker = Faker(locale='RU')
    return faker.address()


def fake_big_email(count):
    count = count - 5
    return mixed_string(count // 2) + '@' + mixed_string(count // 2 + count % 2) + '.com'


def cyrillic_string(count):
    return ''.join(choice(cyrillic_letters) for _ in range(count))


def digit_from_range(first, last):
    return randint(first, last)


def datetime_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def date_now():
    return datetime.now().strftime("%Y-%m-%d")


def time_now():
    return datetime.now().strftime("%H:%M:%S")


def datetime_delta(days_count):
    return (datetime.now() + timedelta(days=days_count)).strftime("%Y-%m-%d %H:%M:%S")


def date_delta(days_count):
    return (datetime.now() + timedelta(days=days_count)).strftime("%Y-%m-%d")
