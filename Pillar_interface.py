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





def display_logo(name):
    # Get the terminal dimensions
    terminal_size = shutil.get_terminal_size()
    terminal_width = terminal_size.columns

    # Create the PyFiglet logo
    logo = pyfiglet.figlet_format("PILLAR3")

    # Center the logo horizontally
    centered_logo = "\n".join(line.center(terminal_width) for line in logo.splitlines())

    # Align the name to the right
    right_aligned_name = name.rjust(terminal_width)

    # Print everything
    print(centered_logo)  # Print the logo centered
    print("\n" * 2)       # Add some spacing
    print(right_aligned_name)  # Print the name on the right





