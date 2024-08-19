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
    file_name = 'Output3.txt'  # Adjust the file name as needed
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            braille_output, letter_output = convert_to_braille(file_content)
            
            window = tk.Tk()
            window.title("Braille Display")
            
            # Calculate window position to center it
            window_x = (screen_width - window.winfo_reqwidth()) // 2
            window_y = (screen_height - window.winfo_reqheight()) // 2
            window.geometry(f"+{window_x}+{window_y}")
            
            braille_font_size = calculate_font_size(len(braille_output))
            
            # Calculate the number of characters per row for grid-like arrangement
            characters_per_row = 10  # Adjust this as needed
            
            # Create individual frames for each Braille character with its corresponding letter
            for i, (braille_char, letter_char) in enumerate(zip(braille_output, letter_output)):
                frame = tk.Frame(window, width=braille_font_size * 2, height=braille_font_size * 4, bd=2, relief="solid")
                row = i // characters_per_row
                col = i % characters_per_row
                frame.grid(row=row, column=col, padx=5, pady=5)
                
                braille_label = tk.Label(frame, text=braille_char, font=('Courier', braille_font_size))
                braille_label.pack(side="top")
                
                letter_label = tk.Label(frame, text=letter_char, font=('Courier', braille_font_size))
                letter_label.pack(side="bottom")

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
