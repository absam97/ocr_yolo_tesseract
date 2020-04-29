from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("training_data\\detection_model-ex-009--loss-0003.916.h5") 
detector.setJsonPath("training_data\\detection_config.json")
detector.loadModel()
detections, extracted_objects_array = detector.detectObjectsFromImage(input_image="image_200.jpg", output_image_path='text_detected_200.jpg', 
                                             minimum_percentage_probability=10, 
                                             display_percentage_probability=False, 
                                             display_object_name=True,
                                             extract_detected_objects=True)

for detection, object_path in zip(detections, extracted_objects_array):
    print(object_path)
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
    print("---------------")
