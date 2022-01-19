import cv2
import numpy as np
import os

def detect_object(frame):
    #cfg_path = os.path.abspath('yolo/yolov4-custom.cfg')
    #weights_path = os.path.abspath('yolov4.weights')
    #names_path = os.path.abspath('yolo/obj.names')

    # Load Yolo
    net = cv2.dnn_DetectionModel('yolov4-custom_last.weights','yolov4-custom.cfg')
    #net = cv2.dnn_DetectionModel(weights_path,cfg_path)
    net.setInputSize(256, 256)
    net.setInputScale(1.0 / 255)
    net.setInputSwapRB(True)

    # frame = cv2.imread('sample1.jpg')
    # print(type(frame))
    # Resize the image
    frame = cv2.resize(frame, dsize=(256, 256), interpolation=cv2.INTER_AREA)

    # with open('coco.names', 'rt') as f:
    with open('obj.names', 'rt') as f:
        names = f.read().rstrip('\n').split('\n')

    classes, confidences, boxes = net.detect(frame, confThreshold=0.1, nmsThreshold=0.4)
    # print("Cl:", classes)
    # print("Co:", confidences)
    # print("Clf:", classes.flatten())
    # print("Cof:", confidences.flatten())
    instances = []
    conf = []
    try:
        # print(type(classes))
        for classId, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
            # print(classId, confidence, box)
            label = '%.2f' % confidence
            label = '%s: %s' % (names[classId], label)
            labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1) # fontScale: 0.5, thickness: 1
            # print(labelSize, baseLine)
            left, top, width, height = box
            # print("T:", top)
            top = max(top, labelSize[1])
            # print("MT:", top)
            cv2.rectangle(frame, box, color=(0, 255, 0), thickness=3)
            # Draw rectangle for labels
            cv2.rectangle(frame, (left, top - labelSize[1]), (left + labelSize[0], top + baseLine),
                        (255, 255, 255), cv2.FILLED)
            instances.append(label)
            conf.append(confidence)
            cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    except:
        pass

    return frame, instances, conf
    # cv2.imshow('out', frame)
    # cv2.waitKey()
