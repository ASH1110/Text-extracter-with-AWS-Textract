import tkinter as tk
from tkinter import filedialog
import boto3

# Function to handle the file upload and S3 upload
def upload_to_s3():
    file_path = filedialog.askopenfilename(title="Select a PDF file")
    if file_path:
        s3_object_key = entry.get()
        try:
            s3.upload_file(file_path, bucket_name,'async-doc-text/{}'.format(s3_object_key))
            status_label.config(text=f'Successfully uploaded {file_path} to {bucket_name}/{s3_object_key}')
        except Exception as e:
            status_label.config(text=f'Error uploading {file_path} to {bucket_name}/{s3_object_key}: {str(e)}')


aws_access_key = 'Enter the Access Key'
aws_secret_access_key = 'Enter the Secret Access Key'
bucket_name = 'Enter the Bucket Name'

#Initialize an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_access_key)

# Created a GUI window
window = tk.Tk()
window.title("PDF Upload to AWS S3")

# Entry widget for S3 object key
label = tk.Label(window, text="Enter S3 Object Key:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Button to open the file dialog
upload_button = tk.Button(window, text="Upload PDF to S3", command=upload_to_s3)
upload_button.pack()

# Label to display status
status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()
