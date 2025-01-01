import os
import shutil
import pyfiglet
def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For MacOS/Linux
    else:
        os.system('clear')


logo = pyfiglet.figlet_format("PILLAR3")

def display_pillar3_intro():
    """
    Displays a brief introduction for Pillar3.
    """
    # ANSI color codes (optional)
    blue = "\033[34m"
    reset = "\033[0m"

    # Intro message
    message = f"""
    {blue}🌟 Welcome to Pillar3! 🌟{reset}

    We're here to combine fun and purpose by bringing you engaging games 
    that support meaningful causes. Together, let's make a difference, one word at a time!
    """
    print(message)

# Example usage



def display_logo(name):
    # Get the terminal dimensions
    terminal_size = shutil.get_terminal_size()
    terminal_width = terminal_size.columns

    # Create the PyFiglet logo

    # Center the logo horizontally
    centered_logo = "\n".join(line.center(terminal_width) for line in logo.splitlines())

    # Align the name to the right
    right_aligned_name = name.rjust(terminal_width)

    # Print everything
    print(centered_logo)  # Print the logo centered
    print("\n" * 2)       # Add some spacing
    print(right_aligned_name)  # Print the name on the right





