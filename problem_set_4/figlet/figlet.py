import sys
from pyfiglet import Figlet


def main():
    """
    Render ASCII art text using pyfiglet library.
    Usage:
    - Without arguments: Prompts for input and renders the text.
    - With -f or --font argument: Prompts for input and renders the text using the specified font.
    """
    try:
        figlet = Figlet()

        # No arguments
        if len(sys.argv) == 1:
            text = input("Input: ")
            print(figlet.renderText(text))

        # -f or --font argument
        elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
            font = sys.argv[2]
            if font in figlet.getFonts():
                figlet.setFont(font=font)
                text = input("Enter the text: ")
                print(figlet.renderText(text))
            # Invalid font
            else:
                raise ValueError("Invalid usage.")

        # Invalid usage
        else:
            raise ValueError("Invalid usage.")

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
