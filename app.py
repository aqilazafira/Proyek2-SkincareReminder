from flask import Flask, render_template

app = Flask(__name__)

# Route untuk Admin Dashboard
@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

# Route untuk User Dashboard
@app.route('/user')
def user_dashboard():
    return render_template('user_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)

# Route untuk Admin Rekomendasi
@app.route('/admin/rekomendasi')
def admin_rekomendasi():
    return render_template('admin_rekomendasi.html')
