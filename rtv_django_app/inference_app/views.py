# inference_app/views.py
import json
import joblib  
from pathlib import Path
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view

# Configure logging
logger = logging.getLogger(__name__)
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the pre-trained model 
model = joblib.load(BASE_DIR/'inference_app'/'random_forest_model.joblib')

@csrf_exempt
@api_view(['POST'])
def predict(request):
    if request.method == 'POST':
        try:
            # Parse the request JSON input
            data = json.loads(request.body.decode('utf-8'))
            
        # Make predictions
            prediction = model.predict([data])

            # Log the request details and the prediction result
            logger.info(f"Request data: {data}")
            logger.info(f"Prediction: {prediction}")

            # Send the prediction as a response
            return JsonResponse({'prediction': prediction.tolist()})
        
        except ValueError as e:
            # Handle invalid input data
            logger.error(f"Error processing request: {str(e)}")
            return JsonResponse({'error': 'Invalid input data'}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            # Catch and log any other errors
            logger.error(f"Unexpected error: {str(e)}")
            return JsonResponse({'error': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
