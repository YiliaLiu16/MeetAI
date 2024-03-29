import requests

# URL of your FastAPI application
url = "http://localhost:8001/recognize_gesture"

# Path to the image file you want to upload
image_path = "./thumbs_up.jpg"

# Open the image file in binary mode
with open(image_path, "rb") as image_file:
    # Define the multipart/form-data payload with the correct field name
    files = {
        "image_file": (image_path, image_file, "image/jpeg")  # Ensure the field name matches the server's expectation
    }

    # Send the POST request
    response = requests.post(url, files=files)

# Print the response from the server
print(response.text)
