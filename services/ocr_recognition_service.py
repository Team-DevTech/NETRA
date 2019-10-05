from google.cloud import vision
import io

def detect_text(path):
    """Detects text in the file."""
    
    client = vision.ImageAnnotatorClient()
    final = []
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    

    for text in texts:
        final.append(text.description.encode('utf-8'))
    return final

