import smtplib
from email.mime.text import MIMEText
import config
import datetime
from faker import Faker
import sqlite3

### DB part
#
conn = sqlite3.connect('ex03.sqlite3')

cursor = conn.cursor()

def create_table():
    query = '''CREATE TABLE IF NOT EXISTS my_users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname VARCHAR(50),
    middle_name VARCHAR(50),
    usr_name VARCHAR(50),
    birthday REAL,
    email VARCHAR(50)
    );
    '''
    cursor.execute(query)

def add_users(surname: str, middle_name: str, name: str,  birthday: datetime.date, email:str):
    query = '''INSERT INTO my_users (surname, middle_name, usr_name, birthday, email) VALUES (?, ?, ?, ?, ?);'''
    cursor.execute(query, [surname, middle_name, name, birthday, email])
    conn.commit()

def find_users(f_email: str):
    query = f'''SELECT *
    FROM my_users 
    WHERE email = ?;
    '''
    result = cursor.execute(query, [f_email])
    return result.fetchone()


## Email part


def send_email(usr_neme : str ='empty', email: str ='empty@empty.com'):
    sender_email = config.sender_email
    receiver_email = email
    # Plain text content
    text = f"""\
        Congratulation {usr_neme}
    """

    message = MIMEText(text, "plain")
    message["Subject"] = "Plain text email"
    message["From"] = sender_email
    message["To"] = receiver_email

    with smtplib.SMTP(config.smtp_server, config.port) as server:
        server.starttls()
        server.login(config.login, config.password)
        server.sendmail(sender_email, receiver_email, message.as_string())


class User:
    def __init__(self, surname: str, middle_name: str, name: str,  birthday: datetime.date, email: str):
        self.surname = surname
        self.middle_name = middle_name
        self.name = name
        self.birthday = birthday
        self.email = email

    def get_age(self):
        return (f'{self.surname}'
                f' {self.middle_name} '
                f'{self.name} має {int(datetime.date.today().year) - int(self.birthday.year)} років')

    def __str__(self):
        return f'{self.surname} {self.middle_name} {self.name} {self.birthday}'


fake = Faker('uk_UA')


def main():
    create_table()
    for _ in range(21):
        usr = User(fake.name().split()[1], fake.middle_name(), fake.name().split()[0], fake.date_of_birth(), fake.email())
        add_users(usr.surname, usr.middle_name, usr.name, usr.birthday, usr.email)
    send_email(usr.email, usr.name)
    print(find_users('iaryna67@example.net'))



if __name__ == '__main__':
    main()
