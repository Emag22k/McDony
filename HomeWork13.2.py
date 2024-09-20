import sqlite3

conn=sqlite3.connect('bankdatabase.db')
sql=conn.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS users(name TEXT,p_number TEXT,balance REAL);')

def login (p_number):
    print(sql.execute('SELECT name,balance FROM users WHERE p_number=?;', (p_number,)).fetchone())


def registration(username,p_number,amount):
   sql.execute('INSERT INTO users(name,p_number,balance) VALUES (?,?,?);',(username,p_number,amount))

def get_user(username,p_number):
   print(sql.execute('SELECT name,p_number,balance FROM users WHERE name=? and p_number=?;',(username,p_number)).fetchone())

def my_balance(username):
    print(sql.execute('SELECT balance FROM users WHERE name=?;',(username,)).fetchone())

def hold(holding,long,proc):
    print((holding*proc)*long)

while True:

    acts = ["1.Регистрация","2.Войти в личный кабинет"]
    print('\n'.join(acts))
    act = input("Выберите действие: ")


    if act.lower()=='регистрация':
        username=input("Введите ваше ФИО: ")
        p_number=input("Введите ваш номер телефона: ")
        amount=float(input("Введите сумму первоначального взноса: "))
        registration(username,p_number,amount)
        conn.commit()
        print(f'{username}, Вы успешно созадли аккаунт!')

    elif act.lower()=='войти':
        p_number=input('Введите ваш номер телефона для входа: ')
        print(f"Добро пожаловать в личный кабинет!")
        login(p_number)
        acts2 = ["1.Найти пользователя", "2.Пополнить","3.Снять","4.Мой счет","5.Вклад под процент"]
        print('\n'.join(acts2))
        act2 = input("Выберите действие: ")

        if act2.lower()=="найти":
            username=input("Введите имя пользователя: ")
            p_number=input("Введите номер телеофна пользователя: ")
            get_user(username,p_number)


        elif act2.lower()=='пополнить':
            cash_amount=input('Введите сумму пополнения: ')
            sql.execute(f'UPDATE users SET balance="balance"+"{cash_amount}" WHERE p_number="{p_number}";')
            conn.commit()
            print(sql.execute(f'SELECT balance FROM users WHERE p_number="{p_number}";').fetchone())

        elif act2.lower()=='снять':
            caash=input('Введите сумму которую хотите снять')
            sql.execute(f'UPDATE users SET balance="balance"-"{caash}" WHERE p_number="{p_number}";')
            conn.commit()
            print(sql.execute(f'SELECT balance FROM users WHERE p_number="{p_number}";').fetchone())

        elif act2.lower()=="счет":
            username=input('Введите логин для подтверждения: ')
            my_balance(username)

        elif act2.lower()=="вклад":
            holding = float(input("Введите сумму вклада- "))
            long = float(input("Вы хотите взять вклад на 12/24/36 месяцев- "))
            hold(holding,long,proc=0.2)

