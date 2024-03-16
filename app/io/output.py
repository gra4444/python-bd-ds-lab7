

def console_output(out_str):
    """
    Outputs the given string to the console.

    Args:
         out_str (str): the string to output.

    Returns:
        None

    """
    print(out_str)
    return None


def file_output_default(out_str, filename):
    """
    Writes the given string to a file.

    Args:
        out_str (str): the string to write.
        filename (str): the name of the file to write to.

    Returns:
        None

    """
    with open(filename, 'w') as file:
        file.write(out_str)
    return None
