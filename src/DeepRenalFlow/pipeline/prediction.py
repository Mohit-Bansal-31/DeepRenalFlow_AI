import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from pathlib import Path
import os


class PredictionPipeline:
    def __init__(self,filename):
        self.filename = filename
        
    def predict(self):
        model = load_model(os.path.join("model","final_model.h5"))
        
        imagename = self.filename
        test_image = image.load_img(imagename, target_size =(224,224))
        test_image = image.img_to_array(test_image)
        test_image = test_image/255.0
        test_image = np.expand_dims(test_image, axis=0)
        prediction_probabilities = model.predict(test_image)
        confidence_score = np.max(prediction_probabilities)
        predicted_class_index = np.argmax(prediction_probabilities)
        
        class_map ={0: "Cyst", 1: "Normal", 2: "Stone",3: "Tumor"}
        
        predicted_class_name =class_map.get(predicted_class_index, "Unknown")
        
        result ={
            "predicted_class" : predicted_class_name,
            "confidence" : float(confidence_score)*100
        }
        print(prediction_probabilities)
        print(confidence_score)
        print(predicted_class_index)
        
        print(result)
        return result
    
    
if __name__ == "__main__":
    obj=PredictionPipeline(Path("artifacts\data_ingestion\CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone\Cyst\Cyst- (7).jpg"))
    obj.predict()

        
