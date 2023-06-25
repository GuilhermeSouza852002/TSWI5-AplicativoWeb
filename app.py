from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista para armazenar os usuários cadastrados
users = []

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users.append({'username': username, 'password': password})
        return redirect('/users')
    return render_template('register.html')

@app.route('/users')
def users_list():
    return render_template('users.html', users=users)

@app.route('/users/edit/<username>', methods=['GET', 'POST'])
def edit_user(username):
    for user in users:
        if user['username'] == username:
            if request.method == 'POST':
                new_username = request.form['username']
                new_password = request.form['password']
                user['username'] = new_username
                user['password'] = new_password
                return redirect('/users')
            return render_template('edit.html', user=user)
    return redirect('/users')

@app.route('/users/delete/<username>', methods=['GET', 'POST'])
def delete_user(username):
    for user in users:
        if user['username'] == username:
            users.remove(user)
            return redirect('/users')
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)
