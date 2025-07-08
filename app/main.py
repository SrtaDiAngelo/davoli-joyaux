from flask import Flask, render_template, request, redirect, url_for, session



app = Flask(__name__)
app.secret_key = 'davolichaveultrasecreta123'  # Pode personalizar, mas precisa ter

@app.route('/')
def home():
    return render_template('index.html')

   #Página de Prata                                            
@app.route('/prata')
def prata():
    return render_template('prata.html')

# Adicionar item ao carrinho
@app.route('/add_carrinho', methods=['POST'])
def add_carrinho():
    if 'carrinho' not in session:
        session['carrinho'] = []
    produto = request.form['produto']
    tam1 = request.form['tam1']
    tam2 = request.form['tam2']
    gravacao = request.form.get('gravacao', '')

    descricao = f"{produto} (Tamanhos: {tam1} e {tam2})"
    if gravacao:
        descricao += f" - Gravação: {gravacao}"

    session['carrinho'].append(descricao)
    session.modified = True
    return redirect(url_for('carrinho'))

# Ver carrinho
@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html', carrinho=session.get('carrinho', []))

# Finalizar pedido
@app.route('/finalizar', methods=['GET', 'POST'])
def finalizar():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        tamanho = request.form['tamanho']
        acabamento = request.form['acabamento']
        gravacao = request.form['gravacao']
        obs = request.form['obs']
        carrinho = session.get('carrinho', [])
        session.clear()
        return render_template('finalizado.html',
                               nome=nome,
                               telefone=telefone,
                               tamanho=tamanho,
                               acabamento=acabamento,
                               gravacao=gravacao,
                               obs=obs,
                               carrinho=carrinho)
    return render_template('finalizado.html')

@app.route('/moeda')
def moeda():
    return render_template('moeda.html')

@app.route('/ouro')
def ouro():
    return render_template('ouro.html')

if __name__=='__main__':
    app.run(debug=True)      