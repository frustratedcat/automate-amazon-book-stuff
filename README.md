Automating Amazon eBook Library Download
========================================

This application is a simple web automation to download my ebook library from Amazon since they make you do it one by one. The application uses Python and Selenium. As Amazon requires multiple clicks to make a download, this application will take a while to finish running. 

Please note that this is a work in progress and still has a few small bugs to fix.

To Run
------
1. Fork and clone repo
2. Create a virtual environment:
    `python3.<python-version> -m venv <desired-name>`
3. Activate virtual environment:
    `source <desired-name>/bin/activate`
4. Install requirements:
    `pip install -r requirements.txt`

You will now be able to run the application. Please be aware that if you have expired library loans in your eBook library you'll get an exception as I haven't coded the fix yet. Please check back here for when I get around to fixing that. 