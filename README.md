# Descubriendo las neuronas

En este repositorio vamos a descubrir el funcionamiento de una red neuronal desde una neuronal con 1 entrada hasta una neurona con 3 entradas y valor de sesgo

## Neurona de 1 entrada

[![ejemplo_neurona_1_entrada](https://subir-imagen.com/images/2023/01/10/Captura-de-pantalla-2023-01-10-102055.png "ejemplo_neurona_1_entrada")](https://subir-imagen.com/images/2023/01/10/Captura-de-pantalla-2023-01-10-102055.png "ejemplo_neurona_1_entrada")

El funcionamiento de esta neurona consiste en que recibe un parametro peso y un valor de entrada e internamente se multiplica esos 2 valores
quedando una formula como esta

$peso * input$

## Neurona de 2 entradas

[![red neuronal con 2 entradas](https://subir-imagen.com/images/2023/01/10/Captura-de-pantalla-2023-01-10-102743.png "red neuronal con 2 entradas")](https://subir-imagen.com/images/2023/01/10/Captura-de-pantalla-2023-01-10-102743.png "red neuronal con 2 entradas")

Esta neurona ahora procesa 2 entradas y internamente calcula el peso w0 con la entrada x0 y es sumado con el producto de peso w1 con entrada x1 que se resume en esta formula

$w0 * x0+$w1 * x1$

## Neurona de 3 entradas y un valor de sesgo

[![red neuronal con 2 entradas](https://subir-imagen.com/images/2023/01/10/Captura-de-pantalla-2023-01-10-103133.png "red neuronal con 3 entradas")](https://subir-imagen.com/images/2023/01/10/Captura-de-pantalla-2023-01-10-103133.png "red neuronal con 3 entradas")

[![Red neuronal 3 entradas parte 2](https://subir-imagen.com/images/2023/01/10/Captura-de-pantalla-2023-01-10-104148.png "Red neuronal 3 entradas parte 2")](https://subir-imagen.com/images/2023/01/10/Captura-de-pantalla-2023-01-10-104148.png "Red neuronal 3 entradas parte 2")

Esta neurona ahora trabaja con 3 entradas y internamente calcula el peso w0 con la entrada x0 y es sumado con el producto de peso w1 con entrada x1, el producto de w2 y x2 y el valor de sesgo mejor conocido como bias que se resume en esta formula

$w0 * x0 + $w1 * x1 + w2 * x2 * bias$
