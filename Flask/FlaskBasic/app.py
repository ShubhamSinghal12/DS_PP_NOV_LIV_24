from flask import Flask, render_template, request


app = Flask('__main__')


@app.route('/')
def start():
    # print('Hello World')
    # return '''<html>
    # <head>
    # <title> Home Page </title>
    # </head>

    # <body>
    # <h1> Hello World</h1>
    # </body>
    # </htlm>'''
    
    # print(render_template('start.html'))
    return render_template('start.html')


@app.route('/home')
def home():
    print(request.args)
    name = request.args.get('name')
    if name == None:
        name = 'Guest'
    return render_template('home.html',name=name,arr=[11,22,33,44,55,66,77])


@app.route('/form',methods = ['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        # print(request.form)
        digit_file = request.files.get('digit')
        digit_file.save('./file.png')
        return f"<html><head></head><body><h1>Thank you {request.form.get('fname')} </h1></body></html>"


if __name__ == '__main__':
    app.run(use_reloader = True,debug=True)





    