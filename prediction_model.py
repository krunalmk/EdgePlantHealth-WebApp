import tensorflow.lite as tflite
import cv2
import numpy as np
import json
from time import sleep


def initialisation():
    # Load TFLite model and allocate tensors.
    interpreter = tflite.Interpreter(model_path='plant_disease_model.tflite')

    # allocate the tensors
    interpreter.allocate_tensors()

    # Get input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    input_shape = input_details[0]['shape']

    input_index = interpreter.get_input_details()[0]["index"]

    return([interpreter, input_details, output_details, input_shape,input_index])

def image_preprocessing(image):
    # img = cv2.imread(image_path)
    # img = img.astype(np.float32)
    # img = cv2.resize(img,(224, 224))
    # print(np.shape(img))
    # return img
    
    # read image data
    image_data = np.asarray(bytearray(image.read()))

    # convert to cv2 image
    cv2_image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
    cv2_image = cv2_image.astype(np.float32) / 255
    cv2_image = cv2.resize(cv2_image,(224, 224))
    
    # show the photo in a console
    # cv2.imshow("Image", cv2_image)
    # cv2.waitKey(0)

    return cv2_image


def predict(interpreter, input_details, output_details, input_shape, input_index, image):
    
    img = image_preprocessing(image)

    #Preprocess the image to required size and cast
    input_tensor= np.array(np.expand_dims(img,0))

    # Set the tensor to point to the input data to be inferred, then run the inference
    interpreter.set_tensor(input_index, input_tensor)
    interpreter.invoke()
    output_details = interpreter.get_output_details()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    # print(output_data)
    pred = np.squeeze(output_data)

    # print(pred)

    with open('categories.json', 'r') as f:
        cat_to_name = json.load(f)
        classes = list(cat_to_name.values())

    class_idx = np.argmax(pred)
        
    # print({classes[class_idx]: pred[class_idx]})
    return {classes[class_idx]: float(pred[class_idx])}

if __name__ =='__main__':
    init = initialisation()
    predict(init[0], init[1], init[2], init[3], init[4], "output1.png")
    sleep(5)
    # predict(init[0], init[1], init[2], init[3], init[4], "0d97bbcf-f322-410a-984d-935e8d2bb5d0___Com.G_TgS_FL 0748.JPG")
