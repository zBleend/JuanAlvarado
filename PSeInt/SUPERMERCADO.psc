Algoritmo CompraProductos
    Limpiar Pantalla
    Escribir "*******************************"
    Escribir "Bienvenido, elija sus productos"
    Escribir "*******************************"
    Escribir " "
    Escribir "1.- Pan $500"
    Escribir "2.- Leche $1500"
    Escribir "3.- Carne $4000"
    Escribir "Escriba fin para terminar la compra."
    
    Definir prod Como Cadena
    Definir totalProductos, totalPagar Como Entero
    
    totalProductos <- 0
    totalPagar <- 0
    Repetir
        Escribir "Ingrese un producto o escriba fin para terminar:"
        Leer prod
        prod <- Minusculas(prod)  
        
        
        Si prod = "fin" Entonces
            Escribir "Compra finalizada."
        Sino
         
            Si prod = "pan" Entonces
                Escribir "Usted lleva Pan"
                totalProductos <- totalProductos + 1
                totalPagar <- totalPagar + 500
            Sino
                Si prod = "leche" Entonces
                    Escribir "Usted lleva Leche"
                    totalProductos <- totalProductos + 1
                    totalPagar <- totalPagar + 1500
                Sino
                    Si prod = "carne" Entonces
                        Escribir "Usted lleva Carne"
                        totalProductos <- totalProductos + 1
                        totalPagar <- totalPagar + 4000
                    Sino
                        Escribir "Error, seleccione un producto válido."
                    FinSi
                FinSi
            FinSi
        FinSi
        
    Hasta Que prod = "fin"
    Escribir "*******************************"
    Escribir "Resumen de compra:"
    Escribir "Cantidad de productos: ", totalProductos
    Escribir "Total a pagar: $", totalPagar
    Escribir "Gracias por su compra."
    Escribir "*******************************"
	
FinAlgoritmo
