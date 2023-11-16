## Consideraciones

En el siguiente tp, en nuestro mayor esfuerzo por comprender y aprender las técnicas de RL vistas en clase recreamos el juego del snake utilizando Open-CV basandonos en el siguiente repo de github https://github.com/TheAILearner/Snake-Game-using-OpenCV-Python.

A partir del mismo buscamos implementar un modelo de aprendizaje por refuerzos visto en clase y transformar el juego en un entorno de stable-baselines esto lo hicimos apoyandonos en los tutoriales de sentdex creador de contenido en youtube sobre python e inteligencia artificial. 
link al canal: https://www.youtube.com/@sentdex


## Creación del entorno y ejecución de los archivos .py de entrenamiento

Para solucionar el clásico dilema de "en mi máquina funciona" el trabajo se encuentra en un container de Docker para el cual es necesario ejecutar la siguiente serie de pasos.

En primer lugar es necesario clonar el repositorio a nivel local 

```
git clone https://github.com/bonafepedro/ReinforcementLearningApp.git
```

En segundo lugar es necesario correr el docker build al Dockerfile para ello es necesario tener instalado docker previamente. 

En sistemas windows es necesario tener abierto Docker Desktop

```
cd ./ReinforcementLearningApp
docker build --tag rl_proyect .
```

Lanzamos el contenedor.

```
docker run -it rl_proyect
```

Finalmente una vez dentro del container tenemos dos archivos que son los ejecutables de la app env_snake_learning.py y training_model_snake_2.py el primero tiene establecido como Hiperparámetros TIMESTEPS = 10 y 10000 iteraciones de aprendizaje. En el segundo te pide que le indiques por consola los hiperparámetros y corre con los que le provees. 

## Problemas y errores 
Estuvimos teniendo algunos problemas vinculados al uso de gymnasium puntualmente por la necesidad de instalar el paquete box2d que al querer ejecutar la linea:
```
    pip3 install gym[box2d]   
    pip3 install gymnasium[box2d]   # probamos tanto con gym como con gymnasium
```
Nos saltaba el error de no poseer las weels. Buscando en stackoverflow vimos que necesitabamos instalar el paquete swing pero aun instalándolo esto no se solucionó. Intentamos también levantar una máquina virtual con virtualbox pero ocurrieron problemas vinculados al espacio en la computadora en que se ejecutó. 



Gracias y saludos

*Tania Trincheri y Pedro Bonafé*

