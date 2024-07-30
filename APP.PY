import tkinter as tk
from tkinter import messagebox
import time

def setup_window():
    root = tk.Tk()
    root.title("Binary Search Algorithm Visualizer")
    root.geometry("600x400")
    return root

def create_input_fields(root):
    tk.Label(root, text="Enter numbers (comma separated):").pack(pady=5)
    array_entry = tk.Entry(root, width=50)
    array_entry.pack(pady=5)

    tk.Label(root, text="Enter target number:").pack(pady=5)
    target_entry = tk.Entry(root, width=20)
    target_entry.pack(pady=5)

    return array_entry, target_entry

def create_buttons(root, start_search):
    search_button = tk.Button(root, text="Start Search", command=start_search)
    search_button.pack(pady=10)

    return search_button

def display_array(canvas, array, left, right, mid):
    canvas.delete("all")
    width = 500 / len(array)
    for i, num in enumerate(array):
        x0 = i * width
        x1 = (i + 1) * width
        color = "white"
        if i == mid:
            color = "green"
        elif i >= left and i <= right:
            color = "yellow"
        canvas.create_rectangle(x0, 50, x1, 100, fill=color)
        canvas.create_text((x0 + x1) / 2, 75, text=str(num), fill="black")
    canvas.update()

def binary_search_visualize(array, target, canvas):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        display_array(canvas, array, left, right, mid)
        time.sleep(1)  # Pause to visualize the step
        if array[mid] == target:
            messagebox.showinfo("Result", f"Target {target} found at index {mid}")
            return
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    messagebox.showinfo("Result", f"Target {target} not found in the array")

def start_search(array_entry, target_entry, canvas):
    array_str = array_entry.get()
    target_str = target_entry.get()
    
    if not array_str or not target_str:
        messagebox.showwarning("Input Error", "Please enter both array and target.")
        return
    
    try:
        array = list(map(int, array_str.split(',')))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid array of integers.")
        return

    try:
        target = int(target_str)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid target integer.")
        return
    
    array.sort()  # Binary search requires a sorted array
    binary_search_visualize(array, target, canvas)

def main():
    root = setup_window()

    array_entry, target_entry = create_input_fields(root)

    canvas = tk.Canvas(root, width=500, height=150, bg="white")
    canvas.pack(pady=20)

    start_search_callback = lambda: start_search(array_entry, target_entry, canvas)
    create_buttons(root, start_search_callback)

    root.mainloop()

if __name__ == "__main__":
    main()
