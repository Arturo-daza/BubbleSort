def ordenamiento_burbuja(arr): 
    n = len(arr) 
    # Recorrer todos los elementos del arreglo
    for i in range(n): 
        # Ultimos i elementos ya estan en su lugar
        for j in range(0, n-i-1): 
            # Recorrer el arreglo de 0 a n-i-1
            # Intercambiar si el elemento encontrado es mayor que el siguiente
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
