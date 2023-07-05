from flask import Flask, request, g
from prediction_model import *
from utility import *

app = Flask(__name__)
interpreter_details = []


interpreter_list = []


@app.before_first_request
def load_model():

    global interpreter_list
    interpreter_list = initialisation()

    return

# @app.route('/img/<img>',  methods=['POST', 'GET'])
# def processImg(img):

@app.route('/img',  methods=['POST', 'GET'])
def processImg():
    if request.method == 'POST':
        img = request.files["img"]
        result = predict(interpreter_list[0], interpreter_list[1],
                            interpreter_list[2], interpreter_list[3], interpreter_list[4], img)
        print(img)
        # return img.filename
        print(result)
        return {"prediction": result}

@app.route('/predict', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        # result = predict(g.interpreter_list[0], g.interpreter_list[1], g.interpreter_list[2], g.interpreter_list[3], g.interpreter_list[4])
        # access the data in the request body

        image = request.files["img"]

        result = predict(interpreter_list[0], interpreter_list[1],
                         interpreter_list[2], interpreter_list[3], interpreter_list[4], image)

        # print(result)
        return {"prediction": result}

    else:
        # if request.method == "GET":
        #     image = request.files["img"]
        #     result = predict(interpreter_list[0], interpreter_list[1],
        #                     interpreter_list[2], interpreter_list[3], interpreter_list[4], image)
        #     return {"prediction": result}
        # else:
        return "This app is running on port 3000"

@app.route('/query-example')
def query_example():
    runtimeMemoryUsage = request.args.get('runtimeMemoryUsage')
    heapUsage = request.args['heapUsage']
    cpuTemperature = request.args.get('cpuTemperature')
    filename = "stats.csv"
    dataArray = [runtimeMemoryUsage,heapUsage,cpuTemperature]
    
    appendCSV( filename=filename, dataArray=dataArray)

    return '''
              <h1>runtimeMemoryUsage: {}</h1>
              <h1>heapUsage: {}</h1>
              <h1>cpuTemperature: {}'''.format(runtimeMemoryUsage, heapUsage, cpuTemperature)


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
