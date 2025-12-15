from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

@app.route('/about')
def about():
    title='About Us'
    name='Ittiphat Phusa'
    email='ppap@example.com'
    phone='123-456-7890'
    return render_template('about.html', 
                            title=title, 
                            name=name,
                            email=email, 
                            phone=phone)

@app.route('/favorite/food')
def favorite_food():
    title='My Favorite Foods'
    foods = ['เนื้อ', 'น้ำพริก', 'ส้มตำ', 'ต้มยำ', 'กะเพรา', 'ไก่ย่าง','ไก่ทอด']
    return render_template('favorite_food.html', title=title, foods=foods)

@app.route('/favorite/sport')
def favorite_sport():
    title='My Favorite Sports'
    sports = ['ฟุตบอล', 'บาสเกตบอล', 'เทนนิส', 'ว่ายน้ำ', 'วิ่ง']
    return render_template('favorite_sport.html', title=title, sports=sports)

@app.route('/greeting/<name>')
def greeting(name):
    title='Welcome Page'
    return render_template('welcome.html', 
                           title=title, 
                           name=name)