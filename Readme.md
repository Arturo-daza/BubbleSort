# Sorting Visualizer with Flet

This Python script uses the `flet` library to create a simple sorting visualizer. The script generates a row of containers, each containing a randomly generated number. It then visually demonstrates the sorting process using the Bubble Sort algorithm.

## Usage

### Prerequisites

* Python > 3.7
* Install dependencies with `pip install flet`

### How to Use

1. Run the script using the command `python bubble.py` 
2. The script will create a row of containers, each displaying a random number.
3. The Bubble Sort algorithm will be applied, and the sorting process will be visually represented.

### Flet Library

* The script utilizes the `flet` library for creating GUI components and handling visual elements.
* For more information on the `flet` library, refer to the [official documentation](https://flet.dev/docs/).

## Script Details

The `main` function within the script performs the following:

1. Creates a row of containers, each containing a random number.
2. Applies the Bubble Sort algorithm to visually demonstrate the sorting process.
3. Updates the Flet page to reflect the changes during the sorting process.

```python
import flet as ft
import random
import time

def main(page: ft.Page): 
    # Function to create a list of containers with random numbers
    def create_containers(number):
        container_list = []
        for _ in range(number): 
            container_list.append(ft.Container(
                content=ft.Text(value=random.randint(1, 100)), 
                alignment=ft.alignment.center, 
                width=50, 
                height=50,
                bgcolor=ft.colors.ORANGE, 
                border_radius=25
            ))
        return container_list
    
    # Create a row of containers
    row = ft.Row(controls=create_containers(10))
    page.add(row)
    time.sleep(2)
    
    # Get the list of containers
    arr = row.controls
    
    n = len(arr) 
    
    # Bubble Sort algorithm for visual representation
    for i in range(n): 
        for j in range(0, n-i-1): 
            arr[j].bgcolor = ft.colors.BLUE
            arr[j+1].bgcolor = ft.colors.BLUE
            time.sleep(0.5)
            page.update()
            if arr[j].content.value > arr[j+1].content.value : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
            arr[j].bgcolor = ft.colors.ORANGE_ACCENT
            arr[j+1].bgcolor = ft.colors.ORANGE_ACCENT
        arr[n-i-1].bgcolor = ft.colors.GREEN
    page.update()

# Run the Flet app with the main function as the target
ft.app(target=main)
```

Feel free to customize the script or extend it with additional features based on your needs.