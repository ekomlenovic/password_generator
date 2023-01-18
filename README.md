# Password Generator  

This code is a password generator written in Python using the Tkinter library to create a graphical user interface (GUI). It allows the user to choose the password length, the types of characters to include (uppercase, lowercase, digits, and symbols), and other options such as automatic copying of the generated password to the clipboard and saving the generated passwords to a CSV file.  

## Main Function
The main function is **`generate_password()`** which is triggered when the user clicks the password generation button. The function uses the user's inputs to generate a random password using the **`random`** library. The function also handles displaying the generated password on the GUI, automatic copying of the generated password to the clipboard, and saving of the generated passwords to a CSV file.  

## Other functions  
- **`open_github()`** is called when the user clicks on the Github icon to open the Github page of the project.  
- **`resource_path()`** is used to handle resource paths when the script is run using PyInstaller.    

## Libraries used  
The libraries used in this code are **`tkinter`** for creating the GUI, **`random`** for generating random passwords, **`string`** for the character sets used to generate the passwords, **`pyperclip`** for automatic copying of generated passwords to the clipboard, **`PIL`** for image manipulation, **`webbrowser`** for opening link and **`csv`** for csv file handling.  
