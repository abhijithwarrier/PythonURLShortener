# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI FOR SHORTENING OF USER-INPUT URLS USING TinyURL AND COPY TO THE CLIPBOARD.
#
# The Shortenend URL Can Be Copied To The Clipboard Using The pyperclip Library
#
# TinyURL is a URL Shortening Service. TinyURL has not officially released an API for Python.
# pyperclip is a cross-platform Python module for copy & paste clipboard functions. pyperclip
# Library currently handles plaintext.
# The module can be installed using the command - pip install pyperclip

# Importing the necessary libraries
import pyperclip
import tkinter as tk
from tkinter import *
from urllib.request import urlopen

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidget():
    iUrlLabel=Label(root, text="URL TO SHORTEN:", bg="skyblue4", font=('Comic Sans MS',15,'bold'))
    iUrlLabel.grid(row=0, column=1, padx=5, pady=5)

    iUrlEntry=Entry(root, textvariable=inputUrl, width=30, bg="azure3")
    iUrlEntry.grid(row=1, column=1, padx=5, pady=5)

    shortenButton=Button(root, text="Shorten URL", command=shortenUrl, width=10)
    shortenButton.grid(row=1, column=2, padx=5, pady=5)

    root.sMsgLabel=Label(root, bg="skyblue4")
    root.sMsgLabel.grid(row=2, column=1, padx=5, pady=5)

    shortUrlLabel=Label(root, text="SHORTENED URL:", bg="skyblue4", font=('Comic Sans MS',15,'bold'))
    shortUrlLabel.grid(row=3, column=1, padx=5, pady=5)

    root.shortUrl=Label(root, width=30, bg="azure3")
    root.shortUrl.grid(row=4, column=1, padx=5, pady=5)

    copybutton=Button(root, text="Copy URL", command=copyUrl, width=10)
    copybutton.grid(row=4, column=2, padx=5, pady=5)

    root.copyMsgLabel=Label(root, bg="skyblue4")
    root.copyMsgLabel.grid(row=5, column=1, padx=5, pady=5)

# Defining shortenUrl() to fetch user-input URL and shorten the entered URL
def shortenUrl():
    # Fetching and storing the user entered URL in a variable
    i_Url = inputUrl.get()
    # Concatenating user-input URL with TinyURL's API URL & storing the complete URL in tiny_url
    tinyurl_request = 'http://tinyurl.com/api-create.php?url=' + i_Url
    # Opening the tinyurl_request using the urlopen() and storing the response in url_response
    url_response = urlopen(tinyurl_request)
    # Since urlopen returns stream of bytes, url_response is decoded first using the decode()
    # method and then the read() method reads the decoded URL and stores it in shortened_url
    shortened_url = url_response.read().decode()
    # Setting the shortened URL to the text parameter of Label Widget using config() method
    root.shortUrl.config(text=shortened_url)
    # Displaying the final output message
    root.sMsgLabel.config(text="URL HAS BEEN SHORTENED")

# Defining copyUrl() to copy the shortened URL to the clipboard using pyperclip
def copyUrl():
    # Copying the shortened_url to clipboard using the pyperclip.copy() method
    pyperclip.copy(root.shortUrl.cget('text'))
    # Displaying the final output message
    root.copyMsgLabel.config(text="URL HAS BEEN COPIED")

# Creating object of tk class
root = tk.Tk()

# Setting the title, background color and disabling the resizing property
root.title("PythonURLShortener")
root.resizable(False, False)
root.config(background = "skyblue4")

# Creating tkinter variables
inputUrl = StringVar()

# Calling the CreateWidgets() function with argument bgColor
CreateWidget()

# Defining infinite loop to run application
root.mainloop()
