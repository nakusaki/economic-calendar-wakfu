import matplotlib.pyplot as plt
import requests
from io import BytesIO

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plotting the graph
plt.plot(x, y)
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Example Plot')

# Save the plot as a BytesIO object
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)

# Prepare headers and data for LINE notification
url = 'https://notify-api.line.me/api/notify'
access_token = "A8KQc1kByq8Ev5nA11gzwWgpOW9H5DTgX7HeowMCMXR"

def send_line_notify_with_image(message, token, image):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    data = {
        'message': message
    }
    files = {
        'imageFile': image
    }
    response = requests.post(url, headers=headers, data=data, files=files)
    if response.status_code == 200:
        print('Notification sent successfully.')
    else:
        print('Failed to send notification.')

# Send the plot along with a message
send_line_notify_with_image("Here's the plot!", access_token, buffer)
