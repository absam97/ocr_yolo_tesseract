# ocr_yolo_tesseract
OCR is a technology that recognizes text within a digital image. It is commonly used to recognize text in scanned documents, but it serves many other purposes as well.  OCR software processes a digital image by locating and recognizing characters, such as letters, numbers, and symbols. 

**I acquired the data for this task from here - https://dataturks.com/projects/devika.mishra/Indian_Number_plates -**

**Images in this dataset looks like -** 

![](img_ex.jpg)

Steps - 
Instructions - Please make changes to the code input locations wherever required, for images mainly.   

1. Use Trained Model to generate text region with the help of the file generate_text_region.py from terminal you have to make changes to the location of input image. after doing this change run this code in your terminal - 
python generate_text_region.py

Output would look like - In you python file's directory look for licence0000.jpg


![](text_detected_200-objects/licence-00000.jpg)

2. Now Use this image to input in the check skew using this command in the terminal - 

deskew input.png

if skew is present use 
deskew --output output.png input.png

after deskewing image would look like - 

![](deskewed_200.jpg)

3. Use below command to generate text as output from finale deskewed image - 

python read_text.py

output would look like this - 

![](output_text.JPG)

You can convert this to text file as well using >'name.txt' in above python statement

For more information check out google colab notebook - 

https://colab.research.google.com/drive/1O43GwR5VFz7-TslFiCegL0ixn00zbAl4#scrollTo=ppTaAffN-lCW

**I made some changes to the repo - now you can just clone it and follow below steps to do ocr -**

1. change your current directory to the repo using terminal, git bash or anaconda prompt

2. run pip install -r requirements.txt

3. run python app.py

4. run localhost in your web browser

5. drag and drop an image following the instructions and voila you'll get a text output
