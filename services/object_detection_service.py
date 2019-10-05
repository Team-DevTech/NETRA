from google.cloud import vision
import io

class ObjectDetect:

    def detect_labels(path):
        """Detects labels in the file."""
        labelArray= []
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.label_detection(image=image)
        labels = response.label_annotations
        print('Labels:')

        for label in labels:
            val = label.description
            labelArray.append(val.encode("utf-8"))
        return labelArray


