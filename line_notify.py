import requests

url = 'https://notify-api.line.me/api/notify'
access_token = "A8KQc1kByq8Ev5nA11gzwWgpOW9H5DTgX7HeowMCMXR"

def send_line_notify(message, token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    data = {
        'message': message
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print('Notification sent successfully.')
    else:
        print('Failed to send notification.')

message = 'Hello, this is a test notification from Python!'
send_line_notify(message, access_token)

# def send_line_notify_with_table(table_data, token):
    # url = 'https://notify-api.line.me/api/notify'
    # headers = {
        # 'Authorization': f'Bearer {token}'
    # }
    # message = '\n'.join(['\t'.join(row) for row in table_data])
    # data = {
        # 'message': message
    # }
    # response = requests.post(url, headers=headers, data=data)
    # if response.status_code == 200:
        # print('Notification sent successfully.')
    # else:
        # print('Failed to send notification.')

# table_data = [
    # ['Column 1', 'Column 2', 'Column 3'],
    # ['Data 1', 'Data 2', 'Data 3'],
    # ['Data 4', 'Data 5', 'Data 6']
# ]
# # send_line_notify_with_table(table_data, access_token)

# def send_line_notify_with_sticker(message, sticker_package_id, sticker_id, token):
    # url = 'https://notify-api.line.me/api/notify'
    # headers = {
        # 'Authorization': f'Bearer {token}'
    # }
    # data = {
        # 'message': message,
        # 'stickerPackageId': sticker_package_id,
        # 'stickerId': sticker_id
    # }
    # response = requests.post(url, headers=headers, data=data)
    # if response.status_code == 200:
        # print('Notification sent successfully.')
    # else:
        # print('Failed to send notification.')

# message = 'Hello, this is a sticker notification!'
# sticker_package_id = 1  # Replace with the sticker package ID
# sticker_id = 2  # Replace with the sticker ID
# # send_line_notify_with_sticker(message, sticker_package_id, sticker_id, access_token)

