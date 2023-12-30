import flet as ft
import random
import time

def main(page: ft.Page): 
    
    def create_containers(number):
        container_list=[]
        for _ in range(number): 
            container_list.append(ft.Container(
                content= ft.Text(value=random.randint(1,100)), 
                alignment=ft.alignment.center, 
                width = 50, 
                height = 50,
                bgcolor=ft.colors.ORANGE, 
                border_radius=25
            ))
        return container_list
    
    row = ft.Row(controls=create_containers(10))
    page.add(row)
    time.sleep(2)
    
    arr= row.controls
    
    n = len(arr) 
    
    
    # Recorrer todos los elementos del arreglo
    for i in range(n): 
        # Ultimos i elementos ya estan en su lugar
        for j in range(0, n-i-1): 
            arr[j].bgcolor= ft.colors.BLUE
            arr[j+1].bgcolor= ft.colors.BLUE
            time.sleep(0.5)
            page.update()
            # Recorrer el arreglo de 0 a n-i-1
            # Intercambiar si el elemento encontrado es mayor que el siguiente
            if arr[j].content.value > arr[j+1].content.value : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
            arr[j].bgcolor= ft.colors.ORANGE_ACCENT
            arr[j+1].bgcolor= ft.colors.ORANGE_ACCENT
        arr[n-i-1].bgcolor = ft.colors.GREEN
    page.update()



ft.app(target= main)