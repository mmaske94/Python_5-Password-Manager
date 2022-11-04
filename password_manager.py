
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split('|')
            print('User:',user, 'Password:',password)

def add():
    usser_name = input('User Name: ' )
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(user_name + '|' + pwd + '\n')

while True:
    mode = input('Would You Like to Add a New Password, View Current Passwords, or Quit? (add/view/q): ').lower()


    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    elif mode == 'q':
        break
    else:
        print('Invalid Mode')
        continue