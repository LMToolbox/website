from flask import Flask, render_template, request
from flask_babel import Babel
from flask_babel import lazy_gettext as _

supported_langs = ['pl', 'en']

app = Flask(__name__)

# Handle locales by Babel
def get_locale():
    return request.accept_languages.best_match(supported_langs)
babel = Babel()
babel.init_app(app, locale_selector=get_locale)

# Set current_locale variable in html
@app.context_processor
def inject_locale():
    return dict(current_locale=get_locale())


# Home
@app.route("/")
def home():
    return render_template("home.html", title=_('home page title'))

# CV
@app.route("/privacy")
def cv():
    return render_template("privacy.html", title=_('privacy page title'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6600)