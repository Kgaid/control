#  <u>Url Analyzer program: </u> 

This program implements the functionality to parse HTML pages. You can run the program: 
1. Run directly the script with IDE
2. Run script with parameters
3. Run script from terminal with input from the console of the url once the program asks for it.
<hr> 
The link for a requirements file you can f ind here: [...]
<hr>
    
The program performs the following tasks:
    
    - Validation of the URL to ensure it is well-formed. 
    - Finding all the links on the page and checking their validity.
    - Saving the links with a status code of 200 to a separate file valid_links.txt.
    - Saving all other links to a file named broken_links.txt.
<hr>
Please note that the program requires the requests library to be installed. You can install it using the following command:

    pip install requests