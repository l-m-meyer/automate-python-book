#! python3
# mcb.pyw = Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb_x.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb_x.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb_x.pyw list - Loads all keywords to clipboard.
#        py.exe mcb_x.pyw delete <keyword> - Deletes a keyword from the shelf.
#        py.exe mcb_x.pyw delete - Deletes all keywords from the shelf.


import shelve, pyperclip, sys


def start():
    mcbShelf = shelve.open('mcb_x')
    process(mcbShelf)
    mcbShelf.close()


def process(file):
    # Save clipboard content.
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        file[sys.argv[2]] = pyperclip.paste()
    
    if len(sys.argv) == 2:
        # List keywords.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(file.keys())))
        
        # Load content.
        if sys.argv[1] in file:
            pyperclip.copy(file[sys.argv[1]])
        
        # Delete all keywords.
        if sys.argv[1].lower() == 'delete':
            for key in list(file.keys()):
                del file[key]
    
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        # Deletes a keyword from the shelf.
        del file[sys.argv[2]]


if __name__ == '__main__':
    start()