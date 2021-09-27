## Read Me Please

### 1. Instructions How to run this progam

		1. First please install Python3.8

		2. Please install below: plugin by pip3
			1. pip3 install matplotlib
			2. pip3 install beautifulsoup4
			3. pip install urllib3

		3. Run the script:
			1. MacOS : python3 App.py
			2. Windows: py App.py (Maybe it depends on what you setting in your environment)

### 2. About this progam and my assumptions

		I using python to do this program, the main reason because python have Beautiful soup and matoplotlib can very easy to get HTML source and generator the chart image.

		the part I assumptions about is "find numeric column" so what I did is:

			1. My progam will find sortable table first , if there are not sortable table it will find wiki table.
			2. I find first table td cell
			3. then I find each table td cell has numeric number if i find numeric number in this cell, i will using this column as numeric column and get all the number value plot to the chart. 
			But there are lots chance tables doesn't have any numeric number. So I did other assumptions about if it doesn't have any numeric numbers, I will split the string to array and find each element has numeric number if it contain a numeric number it will save that number. eg "24 May 2000" 24 is numeric number so "24" will save into plot number array
			4. plot to chat. normally I will plot x and y to the chat. for this progam request I just plot number to y line

### 3. More about get Numeric number

		Only harder part of this program is get Numberic Number. a lots of table are inconsistent.		 
		To build this progam can solve all different table structures it will have some more logic functions to solve inconsistent issues. like: transfer these table to the python panda frame. so python panda can easy to mangent this table values, columns and rows

### 4. Reference

	   This program should run like this
	   1. run script and input url:
			https://prnt.sc/1tvjs51
	   2. after run the script plot image will showing in the same folder of this progam called polt.png
	   		https://prnt.sc/1tvjx0j
			https://prnt.sc/1tvk0vw
			

	    



