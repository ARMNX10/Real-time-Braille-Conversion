import tkinter as tk
import ctypes

# Get screen width and height
user32 = ctypes.windll.user32
screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Braille dictionary mapping characters to Braille patterns (capital letters)
braille_dict = {
    'A': '⠁', 'B': '⠃', 'C': '⠉', 'D': '⠙', 'E': '⠑',
    'F': '⠋', 'G': '⠛', 'H': '⠓', 'I': '⠊', 'J': '⠚',
    'K': '⠅', 'L': '⠇', 'M': '⠍', 'N': '⠝', 'O': '⠕',
    'P': '⠏', 'Q': '⠟', 'R': '⠗', 'S': '⠎', 'T': '⠞',
    'U': '⠥', 'V': '⠧', 'W': '⠺', 'X': '⠭', 'Y': '⠽',
    'Z': '⠵', ' ': '⠀'
}

def convert_to_braille(text):
    braille_text = ''
    letter_text = ''
    
    for char in text.upper():
        if char in braille_dict:
            braille_text += braille_dict[char] + ' '
            letter_text += char + ' '
    
    return braille_text, letter_text

def calculate_font_size(text_length):
    base_font_size = 36
    max_text_length = 1000  # Define your maximum text length for adjustments
    
    if text_length > max_text_length:
        return base_font_size - int((text_length - max_text_length) / 10)  # Adjust font size dynamically
    else:
        return base_font_size

def display_braille():
    file_name = 'output3.txt'  # Adjust the file name as needed
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            braille_output, letter_output = convert_to_braille(file_content)
            
            window = tk.Tk()
            window.title("Braille Display")
            window.attributes('-fullscreen', True)
           
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)
            
            braille_font_size = calculate_font_size(len(braille_output))
            letter_font_size = calculate_font_size(len(letter_output))
            
            braille_label = tk.Label(window, text=braille_output, font=('Courier', braille_font_size))
            braille_label.place(x=center_x - braille_label.winfo_reqwidth() / 2, y=center_y - braille_font_size * 2)
            
            letter_label = tk.Label(window, text=letter_output, font=('Courier', letter_font_size))
            letter_label.place(x=center_x - letter_label.winfo_reqwidth() / 2, y=center_y)
            
            def close_window(event):
                if event.keysym == 'e' or event.keysym == 'E':
                    window.destroy()
            
            window.bind('<Key>', close_window)
            window.mainloop()

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

display_braille()
