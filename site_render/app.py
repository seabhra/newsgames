

from flask import Flask, render_template, send_from_directory, jsonify
import os

# Criar a aplicação Flask
app = Flask(__name__)

# Configurações
app.config['2ae2a3ee342c47d9351c7ef900c4b902'] = 'your-secret-key-here'

# Página inicial
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gold NewsGames - Análise de Mídias e Tráfego Pago</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #1a1a1a; color: #fff; }
            .container { max-width: 1200px; margin: 0 auto; }
            .header { text-align: center; padding: 50px 0; }
            .logo { font-size: 3em; color: #ffd700; margin-bottom: 10px; }
            .subtitle { font-size: 1.2em; color: #ccc; }
            .news-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 40px; }
            .news-card { background: #2a2a2a; padding: 20px; border-radius: 10px; }
            .news-title { color: #ffd700; font-size: 1.3em; margin-bottom: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="logo">🎮 Gold NewsGames</div>
                <div class="subtitle">O melhor portal de análise de mídias</div>
            </div>
            
            <div class="news-grid">
                <div class="news-card">
                    <div class="news-title">Últimas Notícias</div>
                    <p>Fique por dentro das novidades do mundo dos games!</p>
                </div>
                
                <div class="news-card">
                    <div class="news-title">Reviews</div>
                    <p>Análises completas dos jogos mais aguardados.</p>
                </div>
                
                <div class="news-card">
                    <div class="news-title">eSports</div>
                    <p>Cobertura completa dos campeonatos e torneios.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''

# Página sobre
@app.route('/sobre')
def about():
    return '''
    <h1>Sobre o Gold NewsGames</h1>
    <p>Portal dedicado à análise de mídias e tráfego pago.</p>
    <p>Domínio: newsgame.com.br</p>
    '''

# API para verificar status
@app.route('/api/status')
def api_status():
    return jsonify({
        'status': 'online',
        'site': 'Gold NewsGames',
        'domain': 'newsgame.com.br',
        'version': '1.0'
    })

# Health check para o Render
@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

# Página 404
@app.errorhandler(404)
def not_found(error):
    return '''
    <h1>Página não encontrada</h1>
    <p>A página que você procura não existe.</p>
    <a href="/">Voltar ao início</a>
    ''', 404

# Configuração para produção
if __name__ == '__main__':
    # Obter porta do ambiente (Render usa variável PORT)
    port = int(os.environ.get('PORT', 5000))
    # Determinar se está em produção
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    
    app.run(host='0.0.0.0', port=port, debug=debug_mode)