from flask import Flask

from interfaces.livros_controller import livros_bp

app = Flask(__name__)
app.register_blueprint(livros_bp)

if __name__ == '__main__':
    app.run(debug=True)
