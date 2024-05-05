from tkinter import *

# Function to encrypt or decrypt text
def caesar_cipher(text, shift, mode):
  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  new_text = ''
  for char in text:
    if char not in alphabet:
      new_text += char
      continue
    index = alphabet.find(char)
    new_index = (index + shift) % len(alphabet)
    new_char = alphabet[new_index]
    new_text += new_char if mode == 'encrypt' else alphabet[(new_index - shift) % len(alphabet)]
  return new_text

# Function to handle button clicks
def handle_click():
  message = message_entry.get()
  shift = int(shift_entry.get())
  result_text.delete(0.0, END)
  result_text.insert(END, caesar_cipher(message, shift, var.get()))

# Create the main window
root = Tk()
root.title("Caesar Cipher")

# Create labels and entry fields
message_label = Label(root, text="Enter message:")
message_label.pack()

message_entry = Entry(root, width=50)
message_entry.pack()

shift_label = Label(root, text="Enter shift value:")
shift_label.pack()

shift_entry = Entry(root, width=5)
shift_entry.pack()

# Create radio buttons for encryption/decryption mode
var = StringVar()
var.set("encrypt")

encrypt_radio = Radiobutton(root, text="Encrypt", variable=var, value="encrypt")
encrypt_radio.pack()

decrypt_radio = Radiobutton(root, text="Decrypt", variable=var, value="decrypt")
decrypt_radio.pack()

# Create button and result text box
button = Button(root, text="Run", command=handle_click)
button.pack()

result_label = Label(root, text="Result:")
result_label.pack()

result_text = Text(root, height=5, width=50)
result_text.pack()

root.mainloop()
