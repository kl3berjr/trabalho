from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'seu_segredo_aqui'  # Necessário para flash messages

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        senha = request.form['senha']
        confirmar_senha = request.form['confirmar_senha']
        if senha != confirmar_senha:
            flash('As senhas não coincidem!', 'error')
            return redirect(url_for('cadastro'))
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('login'))
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)
