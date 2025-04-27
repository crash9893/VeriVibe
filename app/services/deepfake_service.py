import subprocess
import os

def detect_deepfake_image(image_path):
    # Paths to model and classes
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'deepfake')
    model_path = os.path.join(base_dir, 'models', 'xception_model.pth')
    classes_path = os.path.join(base_dir, 'classes.txt')
    script_path = os.path.join(base_dir, 'image_prediction.py')
    result = subprocess.run(
        ['python', script_path, model_path, classes_path, image_path],
        capture_output=True, text=True
    )
    return result.stdout.strip() 