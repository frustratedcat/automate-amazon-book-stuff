Automating Amazon eBook Library Download
========================================

This application is a simple web automation to download my ebook library from Amazon since they make you do it one by one. The application uses Python and Selenium. As Amazon requires multiple clicks to make a download, this application will take a while to finish running. 

To Run
------
1. Fork and clone repo
2. Create a virtual environment:
    `python3.<python-version> -m venv <desired-name>`
3. Activate virtual environment:
    `source <desired-name>/bin/activate`
4. Install requirements:
    `pip install -r requirements.txt`
5. Run:
    `python main.py`

Please note that if you use options 2 when you run the application you will more than likely get an error. This is due to a specific ID for the desired list to search. To fix this on your end:
1. Navigate to the "Your Lists" page on Amazon
2. Right click on the list you want to use and click "Inspect" to bring up the dev tools
3. On the <span> element of the list you selected you'll have an ID that should begin with "wl-list-entry-title-" followed by a string of letters and numbers
4. In the main.py file, find the function "nav_to_book_list" and replace the XPATH with the ID for your specific list
5. Save the code and run it as shown in Step 5 above and it should work
