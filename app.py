from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/multiplication')
def multiplication():
    return render_template('multiplication.html', title='Multiplication')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/create-account')
def create_account():
    return render_template('create-account.html', title='Create Account')

@app.route('/profile')
def profile():
    return render_template('profile.html', title='Profile')

@app.route('/darab-2-digit')
def darab2digit():
    return render_template('darab/darab-2-digit.html', title='Darab 2 Digit')


# Add routes for bahagi pages
@app.route('/bahagi-2-digit')
def bahagi2digit():
    return render_template('bahagi/bahagi-2-digit.html', title='Bahagi 2 Digit')


@app.route('/bahagi-4-digit')
def bahagi4digit():
    return render_template('bahagi/bahagi-4-digit.html', title='Bahagi 4 Digit')


@app.route('/bahagi-kehidupan-seharian')
def bahagiKehidupanSeharian():
    return render_template('bahagi/bahagi-kehidupan-seharian.html', title='Bahagi Kehidupan Seharian')


@app.route('/bahagi-masalah')
def bahagiMasalah():
    return render_template('bahagi/bahagi-masalah.html', title='Bahagi Masalah')


@app.route('/bahagi-titik-perpuluhan')
def bahagiTitikPerpuluhan():
    return render_template('bahagi/bahagi-titik-perpuluhan.html', title='Bahagi Titik Perpuluhan')


# Add routes for darab pages
@app.route('/darab-3-digit')
def darab3digit():
    return render_template('darab/darab-3-digit.html', title='Darab 3 Digit')


@app.route('/darab-kehidupan-seharian')
def darabKehidupanSeharian():
    return render_template('darab/darab-kehidupan-seharian.html', title='Darab Kehidupan Seharian')


@app.route('/darab-masalah')
def darabMasalah():
    return render_template('darab/darab-masalah.html', title='Darab Masalah')


@app.route('/darab-titik-perpuluhan')
def darabTitikPerpuluhan():
    return render_template('darab/darab-titik-perpuluhan.html', title='Darab Titik Perpuluhan')


# Add routes for matematik-pengguna/kredit-hutang pages
@app.route('/matematik-pengguna/kredit-hutang/definisi-kredit-hutang')
def definisiKreditHutang():
    return render_template('matematik-pengguna/kredit-hutang/definisi-kredit-hutang.html',
                           title='Definisi Kredit Hutang')


@app.route('/matematik-pengguna/kredit-hutang/faedah-atas-baki')
def faedahAtasBaki():
    return render_template('matematik-pengguna/kredit-hutang/faedah-atas-baki.html', title='Faedah Atas Baki')


@app.route('/matematik-pengguna/kredit-hutang/faedah-sama-rata')
def faedahSamaRata():
    return render_template('matematik-pengguna/kredit-hutang/faedah-sama-rata.html', title='Faedah Sama Rata')


@app.route('/matematik-pengguna/kredit-hutang/kira-kredit')
def kiraKredit():
    return render_template('matematik-pengguna/kredit-hutang/kira-kredit.html', title='Kira Kredit')


@app.route('/matematik-pengguna/kredit-hutang/kredit-masalah')
def kreditMasalah():
    return render_template('matematik-pengguna/kredit-hutang/kredit-masalah.html', title='Kredit Masalah')


@app.route('/matematik-pengguna/kredit-hutang/pinjaman-masalah')
def pinjamanMasalah():
    return render_template('matematik-pengguna/kredit-hutang/pinjaman-masalah.html', title='Pinjaman Masalah')


# Add routes for matematik-pengguna/simpanan-pelaburan pages
@app.route('/matematik-pengguna/simpanan-pelaburan/amanah-saham')
def amanahSaham():
    return render_template('matematik-pengguna/simpanan-pelaburan/amanah-saham.html', title='Amanah Saham')


@app.route('/matematik-pengguna/simpanan-pelaburan/faedah-kompaun')
def faedahKompaun():
    return render_template('matematik-pengguna/simpanan-pelaburan/faedah-kompaun.html', title='Faedah Kompaun')


@app.route('/matematik-pengguna/simpanan-pelaburan/faedah-mudah')
def faedahMudah():
    return render_template('matematik-pengguna/simpanan-pelaburan/faedah-mudah.html', title='Faedah Mudah')


@app.route('/matematik-pengguna/simpanan-pelaburan/roi')
def roi():
    return render_template('matematik-pengguna/simpanan-pelaburan/roi.html', title='ROI')


@app.route('/matematik-pengguna/simpanan-pelaburan/simpanan-dan-pelaburan')
def simpananDanPelaburan():
    return render_template('matematik-pengguna/simpanan-pelaburan/simpanan-dan-pelaburan.html',
                           title='Simpanan dan Pelaburan')


@app.route('/matematik-pengguna/simpanan-pelaburan/simpanan-masalah')
def simpananMasalah():
    return render_template('matematik-pengguna/simpanan-pelaburan/simpanan-masalah.html', title='Simpanan Masalah')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
