from imageai.Detection.Custom import CustomObjectDetection

def generate_text_region(model_path, json_file_path, input_image, output_image):
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_path)
    detector.setJsonPath(json_file_path)
    detector.loadModel()
    detections, extracted_objects_array = detector.detectObjectsFromImage(input_image=input_image, output_image_path=output_image+'.jpg', 
                                             minimum_percentage_probability=10, 
                                             display_percentage_probability=False, 
                                             display_object_name=True,
                                             extract_detected_objects=True)
    detection_box_points = []
    object_path_arr = []
    for detection, object_path in zip(detections, extracted_objects_array):
        object_path_arr.append(object_path)
        detection_box_points.append(detection["box_points"])

    return detection_box_points, object_path
