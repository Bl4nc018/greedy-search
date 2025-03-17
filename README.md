# **Greedy Local & Global Search**  

En este nuevo repositorio, presento un **algoritmo de búsqueda voraz (greedy search)** para resolver un problema de **selección óptima de emisoras de radio**. El objetivo es cubrir un conjunto de estados de EE.UU. utilizando el menor número de emisoras de radio posible para que suene el nuevo disco de Beyoncé.  

El código está modularizado, facilitando su mantenimiento y escalabilidad. Además, incluye dos variantes del algoritmo:
- **Greedy Local Search:** Por un lado, en la variante local se selecciona, de forma aleatoria, una emisora que al menos cubra un estado sin cobertura.
- **Greedy Global Search:** Por otro lado, en la variante global se selecciona la emisora que cubre la mayor cantidad de estados en cada paso.

📌 **Lenguaje:**   Python  
📌 **Paradigma:**  Algoritmos voraces (**greedy algorithms**)  
📌 **Estructura:** Código modular dividido en archivos independientes.  

![Python Version](https://img.shields.io/badge/Python-3.10-blue)

---

## **Índice**
1. [Descripción del problema](#1-descripción-del-problema)
2. [Solución implementada](#2-solución-implementada)
3. [Estructura del proyecto](#3-estructura-del-proyecto)
4. [Instalación y ejecución](#4-instalación-y-ejecución)

---

## **1. Descripción del problema**
El objetivo a lograr de este problema es cubrir todos los estados de EE.UU. utilizando el menor número posible de emisoras de radio. Cada emisora cubre un subconjunto de estados, por lo que es necesario encontrar una lista óptima de emisoras que minimice la cantidad total mientras garantiza la cobertura completa.

### **Propiedades del problema**
| Propiedad            | Descripción |
|----------------------|------------|
| **Tipo de problema** | Optimización combinatoria |
| **Estrategia usada** | Algoritmos voraces (Greedy Search) |
| **Solución óptima garantizada** | ❌ No siempre |

En este caso, resolveremos el problema con dos variantes de la búsqueda voraz:
- **Greedy Local Search:** Selecciona aleatoriamente una emisora válida.
- **Greedy Global Search:** Escoge siempre la emisora con más estados sin cubrir.

---

## **2. Solución implementada**
### **🔹 Enfoque del algoritmo**
El algoritmo implementado está basado en una estrategia *greedy* para encontrar una selección eficiente de emisoras que cubran todos los estados requeridos. Para ello, mantiene un registro de los estados aún sin cobertura, evaluando en cada iteración qué emisora aporta el mayor beneficio en términos de cobertura.

Existen dos variantes del algoritmo:

-   Greedy Local Search, donde la selección de emisoras se realiza de manera aleatoria dentro de las opciones que cubren al menos un estado pendiente.
-   Greedy Global Search, que prioriza la emisora que abarca el mayor número de estados sin cubrir en cada paso.

A medida que se van seleccionando emisoras, la lista de estados pendientes es actualizada, retirando aquellos que han sido cubiertos. Este proceso continúa hasta garantizar la cobertura total con el menor número de emisoras posible, devolviendo como resultado la lista óptima seleccionada.

---

## **3. Estructura del proyecto**
El código sigue una **arquitectura modular**, dividiendo responsabilidades en distintos archivos:
```
📂 greedy-search 
│── 📂 src 
│ │── greedy_local_search.py # Implementación de búsqueda voraz local 
│ │── greedy_global_search.py # Implementación de búsqueda voraz global 
│ │── utils.py # Funciones auxiliares 
│ │── main.py # Archivo principal de ejecución 
│── README.md # Documentación del repositorio 
│── requirements.txt # Dependencias necesarias 
```

---

## **4. Instalación y ejecución**

### **1️⃣ Clonar el repositorio**
```sh
    git clone https://github.com/Bl4nc018/greedy-search.git
    cd greedy-search
```

### **2️⃣ Crear y activar un entorno virtual (Opcional/Recomendado)**

```sh
    python3 -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### **3️⃣ Instalar dependencias**

```sh
    pip install -r requirements.txt
```

### **4️⃣ Ejecutar el código**

Para probar el algoritmo con las dos variantes:

```sh
    python src/main.py
```

---

### Desarrollado por:

<p align="left">
   <a href="https://github.com/Bl4nc018">
      <img src="https://avatars.githubusercontent.com/u/92156488?s=400&u=1302f75511bad4df69803bf7b66443a1a8364b60&v=4" width=115><br>
      <sub>Ania</sub>
   </a>
</p>

**🚀 ¡Si ha gustado, no olvides darme una estrellita ⭐ en GitHub! 🚀**
