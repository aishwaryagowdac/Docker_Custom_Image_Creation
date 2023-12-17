from datetime import datetime

#fucntion to change the index.html file
def modify_index_html(name):
    #get the current date using the datetime library that is imported and store it in date_today
    date_today = datetime.now().strftime("%Y-%m-%d")
    #content that has to changed in index.html
    #Here, I tried to name from the main function as an addtional feature
    content = f"""
    <html>
        <header><title>CY5001 Assignment Summer 2020</title></header>
        <body>
            I am {name} and this is my CY5001 assignment on {date_today}.
        </body>
    </html>
    """
    #open and write this content into the index.html file present in the path given
    with open('/usr/local/apache2/htdocs/index.html', 'w') as f:
        f.write(content)

def main():
    # Set your name
    your_name = "Aishwarya Channappaji"

    # calling the Modify_index_html file and replace the name with your name
    modify_index_html(your_name)
    #print that the content is changed successfully
    print ("Container successfully modified with index.html file")
	
if __name__ == "__main__":
    main()

