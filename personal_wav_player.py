#005800765 Ivonne Aquino
# Final Project: Personal WAV Music Player using Tkinter and winsound

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import winsound


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple WAV Player (Tkinter + winsound)")

        self.current_file = None

        # For background image
        self.bg_image = None
        self.bg_label = None

        # ===== Window setup =====
        self.root.configure(bg="#FEF7FF")
        self.root.geometry("500x260")

        # ===== Title Label (customized) =====
        self.title_label = tk.Label(
            root,
            text="♡ Personal WAV Music Player ♡",
            font=("Arial", 20, "bold"),
            fg="#FF99E7",
            bg="#FFDEFC",
            padx=10,
            pady=10
        )
        self.title_label.pack(fill="x")

        # ===== Current Song Label =====
        self.song_label = tk.Label(
            root,
            text="No song loaded...",
            font=("Arial", 12),
            fg="#FF99E7",
            bg="#FFDEFC",
            anchor="w",
            padx=10
        )
        self.song_label.pack(fill="x", pady=(0, 10))

        # ===== Buttons Frame =====
        btn_frame = tk.Frame(root, bg="#FEF7FF")
        btn_frame.pack(pady=10)

        # Load Button
        self.load_btn = tk.Button(
            btn_frame,
            text="Load WAV",
            font=("Arial", 12, "bold"),
            width=10,
            bg="#4CAF50",
            fg="white",
            activebackground="#66BB6A",
            command=self.load_song
        )
        self.load_btn.grid(row=0, column=0, padx=5)

        # Play Button
        self.play_btn = tk.Button(
            btn_frame,
            text="Play",
            font=("Arial", 12, "bold"),
            width=10,
            bg="#2196F3",
            fg="white",
            activebackground="#42A5F5",
            command=self.play_song
        )
        self.play_btn.grid(row=0, column=1, padx=5)

        # Stop Button
        self.stop_btn = tk.Button(
            btn_frame,
            text="Stop",
            font=("Arial", 12, "bold"),
            width=10,
            bg="#F44336",
            fg="white",
            activebackground="#E57373",
            command=self.stop_song
        )
        self.stop_btn.grid(row=0, column=2, padx=5)

        # ===== Background Image Button =====
        self.bg_btn = tk.Button(
            root,
            text="Set Background Image",
            font=("Arial", 11, "bold"),
            bg="#FF99E7",
            fg="white",
            activebackground="#FF99E7",
            command=self.set_background_image
        )
        self.bg_btn.pack(pady=10)

        # Small info label
        self.info_label = tk.Label(
            root,
            text="Tip: This version supports .wav audio and .png/.gif background images.",
            font=("Arial", 9),
            fg="#FF99E7",
            bg="#FEF7FF"
        )
        self.info_label.pack(pady=(5, 0))

    # ===== File loading =====
    def load_song(self):
        filetypes = (
            ("WAV audio", "*.wav"),
            ("All files", "*.*"),
        )
        filename = filedialog.askopenfilename(
            title="Open WAV file",
            filetypes=filetypes
        )
        if filename:
            self.current_file = filename
            song_name = os.path.basename(filename)
            self.song_label.config(text=f"♫⋆｡♪ ₊˚♬ ﾟ Loaded: {song_name}")

    # ===== Playback controls =====
    def play_song(self):
        if self.current_file:
            # Play asynchronously so the GUI stays responsive
            winsound.PlaySound(
                self.current_file,
                winsound.SND_FILENAME | winsound.SND_ASYNC
            )
        else:
            messagebox.showinfo("No file", "Please load a WAV file first.")

    def stop_song(self):
        # Stop any playing sound
        winsound.PlaySound(None, winsound.SND_PURGE)

    # ===== Background image handling =====
    def set_background_image(self):
        filetypes = (
            ("Image files", "*.png *.gif"),
            ("All files", "*.*"),
        )
        filename = filedialog.askopenfilename(
            title="Choose background image",
            filetypes=filetypes
        )
        if not filename:
            return

        try:
            img = tk.PhotoImage(file=filename)
        except Exception as e:
            messagebox.showerror(
                "Image Error",
                f"Could not load that image.\n\n"
                f"Tip: Use .png or .gif files.\n\nDetails:\n{e}"
            )
            return

        # Keep a reference so the image isn't garbage-collected
        self.bg_image = img

        # If background label doesn't exist yet, create it
        if self.bg_label is None:
            self.bg_label = tk.Label(self.root, image=self.bg_image)
            # Stretch over the whole window
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        else:
            # Just change the image
            self.bg_label.configure(image=self.bg_image)

        # Send background label to the back so other widgets sit on top
        self.bg_label.lower()


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
