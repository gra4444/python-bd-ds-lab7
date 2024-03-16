import pandas as pd


def console_input():
    """
    Takes user input from console and returns it as a string.

    Returns:
        str: user input.
    
    """
    user_input = input("Input: ")
    return user_input


def read_file_default(filename):
    """
    Reads a file using tools provided by Python.

    Args:
        filename (str): the name of the file to read.

    Returns:
        str: the content of the file as a string.

    """
    try:
        with open(filename, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f'File {filename} was not found')


def read_file_pd(filename):
    """
    Reads a CSV file using pandas package.

    Args:
        filename (str): the name of the file to read.

    Returns:
        str: the content of the file as a string.

    """
    try:
        file_content = pd.read_csv(filename)
        return file_content
    except FileNotFoundError:
        print(f'File {filename} was not found')
