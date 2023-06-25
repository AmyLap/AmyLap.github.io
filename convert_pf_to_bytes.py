import base64
import pyperclip

# Read the PDF file as binary data
with open('Amy_Lap_CV.pdf', 'rb') as file:
    pdf_data = file.read()

# Convert the binary data to base64
base64_pdf = base64.b64encode(pdf_data).decode('utf-8')

# Create the download link in your HTML
download_link = f'<a href="data:application/pdf;base64,{base64_pdf}" download>Download CV</a>'

# Output the download link
print(download_link)

# Copy the variable's value to the clipboard
pyperclip.copy(download_link)