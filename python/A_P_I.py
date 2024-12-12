# import requests
from flask import Flask,jsonify,render_template,request
'''
C -> Create ->  POST
R -> Read -> GET
U -> Update -> PUT
D -> delete -> DELETE
'''
app=Flask(__name__)
courses=[
    {
        'courseID':1 ,
        'courseName':"Python Programming"
    },
    {
        'courseID': 2,
        'courseName':"Machine Learning"
    },
    {
        'courseID': 3,
        'courseName':"Data Science"
    },
    {
        'courseID': 4,
        'courseName':"Artificial Intelligent"
    },
]


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/app/A_P_I /courses/all') # type: ignore
def id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Unknown Request"

    result=[]
    for course in courses:
        if course['courseID']== id:
            result.append(course)
        return jsonify(result)
    
if __name__ =="__main__":
    app.run(debug=True)