from flask import Flask, render_template
import os
import subprocess

app = Flask(__name__)

# Rota para renderizar o template HTML
@app.route('/')
def home():
    return render_template('template.html')

# Rota para controlar o notebook (ligar, desligar, abrir, fechar aplicativos)
@app.route('/comando/<string:comando>')
def controlar_notebook(comando):
    try:
        if comando == 'ligar':
            # Lógica para ligar o notebook (Wake-on-LAN)
            return 'Comando para ligar o notebook enviado.'
        elif comando == 'desligar':
            os.system("shutdown /s /t 1")  # Comando para desligar o notebook
            return 'Notebook desligando...'
        elif comando == 'abrir_app':
            subprocess.Popen(['notepad.exe'])  # Exemplo: abre o Bloco de Notas
            return 'Aplicativo aberto.'
        elif comando == 'fechar_app':
            subprocess.call(['taskkill', '/F', '/IM', 'notepad.exe'])  # Fecha o Bloco de Notas
            return 'Aplicativo fechado.'
        else:
            return 'Comando não reconhecido.'
    except Exception as e:
        return f"Erro ao executar o comando: {e}"

if __name__ == '__main__':
    app.run(debug=True)
