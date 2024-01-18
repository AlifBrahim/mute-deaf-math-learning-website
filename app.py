from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8b4fTgOZ9fRpv6F0TP970kdE8XJvF0Ly'

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://doadmin:AVNS_7KPMC3xu3yCp_jz_WfT@uumevents-do-user-14295301-0.b.db.ondigitalocean.com:25060/mathgenius'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(512))
    fullname = db.Column(db.String(256))  # Add this line

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/multiplication')
def multiplication():
    return render_template('multiplication.html', title='Multiplication')


@app.route('/create-account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        # Create a new instance of the User class
        user = User(username=username, fullname=fullname)
        user.set_password(password)
        # Add the new user to the database
        db.session.add(user)
        db.session.commit()
        # Log the user in after registering
        login_user(user)
        return redirect(url_for('profile'))
    return render_template('create-account.html', title='Create Account')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            error = 'Invalid username or password. Please try again.'
        else:
            login_user(user)
            return redirect(url_for('profile'))
    return render_template('login.html', title='Login', error=error)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile')


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.String(255))
    content = db.Column(db.Text(length=4294967295))


@app.route('/save-content', methods=['POST'])
def save_content():
    print("save_content")
    content = request.form['content']
    page = request.form['page']
    # Create a new instance of the Content class
    content_instance = Content(content=content, page=page)
    # Add the new content to the database
    db.session.add(content_instance)
    db.session.commit()
    return jsonify(success=True)



@app.route('/darab-2-digit')
def darab2digit():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='darab-2-digit').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('darab/darab-2-digit.html', title='Darab 2 Digit', content=content, page='darab-2-digit')


# Add routes for bahagi pages
@app.route('/bahagi-2-digit')
def bahagi2digit():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='bahagi-2-digit').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('bahagi/bahagi-2-digit.html', title='Bahagi 2 Digit', content=content, page='bahagi-2-digit')


@app.route('/bahagi-4-digit')
def bahagi4digit():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='bahagi-4-digit').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('bahagi/bahagi-4-digit.html', title='Bahagi 4 Digit', content=content, page='bahagi-4-digit')


@app.route('/bahagi-kehidupan-seharian')
def bahagiKehidupanSeharian():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='bahagi-kehidupan-seharian').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('bahagi/bahagi-kehidupan-seharian.html', title='Bahagi Kehidupan Seharian', content=content, page='bahagi-kehidupan-seharian')


@app.route('/bahagi-masalah')
def bahagiMasalah():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='bahagi-masalah').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('bahagi/bahagi-masalah.html', title='Bahagi Masalah', content=content, page='bahagi-masalah')


@app.route('/bahagi-titik-perpuluhan')
def bahagiTitikPerpuluhan():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='bahagi-titik-perpuluhan').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('bahagi/bahagi-titik-perpuluhan.html', title='Bahagi Titik Perpuluhan', content=content, page='bahagi-titik-perpuluhan')


# Add routes for darab pages
@app.route('/darab-3-digit')
def darab3digit():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='darab-3-digit').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('darab/darab-3-digit.html', title='Darab 3 Digit', content=content, page='darab-3-digit')



@app.route('/darab-kehidupan-seharian')
def darabKehidupanSeharian():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='darab-kehidupan-seharian').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('darab/darab-kehidupan-seharian.html', title='Darab Kehidupan Seharian', content=content, page='darab-kehidupan-seharian')


@app.route('/darab-masalah')
def darabMasalah():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='darab-masalah').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('darab/darab-masalah.html', title='Darab Masalah', content=content, page='darab-masalah')


@app.route('/darab-titik-perpuluhan')
def darabTitikPerpuluhan():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='darab-titik-perpuluhan').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('darab/darab-titik-perpuluhan.html', title='Darab Titik Perpuluhan', content=content, page='darab-titik-perpuluhan')


# Add routes for matematik-pengguna/kredit-hutang pages
@app.route('/matematik-pengguna/kredit-hutang/definisi-kredit-hutang')
def definisiKreditHutang():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='definisi-kredit-hutang').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('matematik-pengguna/kredit-hutang/definisi-kredit-hutang.html',
                           title='Definisi Kredit Hutang',
                           content=content, page='definisi-kredit-hutang')


@app.route('/matematik-pengguna/kredit-hutang/faedah-atas-baki')
def faedahAtasBaki():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='faedah-atas-baki').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('matematik-pengguna/kredit-hutang/faedah-atas-baki.html', title='Faedah Atas Baki', content=content, page='faedah-atas-baki')


@app.route('/matematik-pengguna/kredit-hutang/faedah-sama-rata')
def faedahSamaRata():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='faedah-sama-rata').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('matematik-pengguna/kredit-hutang/faedah-sama-rata.html', title='Faedah Sama Rata', content=content, page='faedah-sama-rata')


@app.route('/matematik-pengguna/kredit-hutang/kira-kredit')
def kiraKredit():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='kira-kredit').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('matematik-pengguna/kredit-hutang/kira-kredit.html', title='Kira Kredit', content=content, page='kira-kredit')


@app.route('/matematik-pengguna/kredit-hutang/kredit-masalah')
def kreditMasalah():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='kredit-masalah').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('matematik-pengguna/kredit-hutang/kredit-masalah.html', title='Kredit Masalah', content=content, page='kredit-masalah')


@app.route('/matematik-pengguna/kredit-hutang/pinjaman-masalah')
def pinjamanMasalah():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='pinjaman-masalah').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('matematik-pengguna/kredit-hutang/pinjaman-masalah.html', title='Pinjaman Masalah', content=content, page='pinjaman-masalah')


# Add routes for matematik-pengguna/simpanan-pelaburan pages
@app.route('/matematik-pengguna/simpanan-pelaburan/amanah-saham')
def amanahSaham():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='amanah-saham').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('matematik-pengguna/simpanan-pelaburan/amanah-saham.html', title='Amanah Saham', content=content, page='amanah-saham')


@app.route('/matematik-pengguna/simpanan-pelaburan/faedah-kompaun')
def faedahKompaun():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='faedah-kompaun').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('matematik-pengguna/simpanan-pelaburan/faedah-kompaun.html', title='Faedah Kompaun', content=content, page='faedah-kompaun')


@app.route('/matematik-pengguna/simpanan-pelaburan/faedah-mudah')
def faedahMudah():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='faedah-mudah').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('matematik-pengguna/simpanan-pelaburan/faedah-mudah.html', title='Faedah Mudah', content=content, page='faedah-mudah')


@app.route('/matematik-pengguna/simpanan-pelaburan/roi')
def roi():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='roi').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('matematik-pengguna/simpanan-pelaburan/roi.html', title='ROI', content=content, page='roi')


@app.route('/matematik-pengguna/simpanan-pelaburan/simpanan-dan-pelaburan')
def simpananDanPelaburan():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='simpanan-dan-pelaburan').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('matematik-pengguna/simpanan-pelaburan/simpanan-dan-pelaburan.html',
                           title='Simpanan dan Pelaburan', content=content, page='simpanan-dan-pelaburan')


@app.route('/matematik-pengguna/simpanan-pelaburan/simpanan-masalah')
def simpananMasalah():
    # Get the last saved content from the database
    content_instance = Content.query.filter_by(page='simpanan-masalah').order_by(Content.id.desc()).first()
    content = content_instance.content if content_instance else ''
    return render_template('matematik-pengguna/simpanan-pelaburan/simpanan-masalah.html', title='Simpanan Masalah', content=content, page='simpanan-masalah')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/game-darab')
def gameDarab():
    return render_template('darab/game-darab.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
