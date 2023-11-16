## Consideraciones

En el siguiente tp, en nuestro mayor esfuerzo por comprender y aprender las técnicas de RL vistas en clase recreamos el juego del snake utilizando Open-CV basandonos en el siguiente repo de github https://github.com/TheAILearner/Snake-Game-using-OpenCV-Python.

A partir del mismo buscamos implementar un modelo de aprendizaje por refuerzos visto en clase y transformar el juego en un entorno de stable-baselines esto lo hicimos apoyandonos en los tutoriales de sentdex creador de contenido en youtube sobre python e inteligencia artificial. 
link al canal: https://www.youtube.com/@sentdex

## Problemas y errores 
Estuvimos teniendo algunos problemas vinculados al uso de gymnasium puntualmente por la necesidad de instalar el paquete box2d que al querer ejecutar la linea:
```
    pip3 install gym[box2d]   
    pip3 install gymnasium[box2d]   # probamos tanto con gym como con gymnasium
```
Nos saltaba el error de no poseer las weels. Buscando en stackoverflow vimos que necesitabamos instalar el paquete swing pero aun instalándolo esto no se solucionó. Intentamos también levantar una máquina virtual con virtualbox pero ocurrieron problemas vinculados al espacio en la computadora en que se ejecutó. 

## Proximos pasos
El paso siguiente es encapsular en un conteiner de docker todo el programa y las herramientas necesarias para poder usarlo así se puede disponibilizar en cualquier ambiente.

Sin más esperamos que sea correcto y cualquier corrección o sugerencia de mejora se agradece. 

Gracias y saludos

*Tania Trincheri y Pedro Bonafé*

