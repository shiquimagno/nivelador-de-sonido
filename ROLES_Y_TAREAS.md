# 📌 Asignación de Roles y Tareas (Semana 1)

Este documento es para que nos dividamos el trabajo del proyecto "Nivelador de Sonido Dinámico". Escriban su nombre al lado del rol que van a tomar en este archivo.

## 👥 Roles del Equipo (6 Integrantes)

- [ ] **Ingeniero de Datos de Audio:** `[Shiquihno Tovar]`
- [ ] **Especialista en Machine Learning (KNN):** `[Alessandro Cámara]`
- [ ] **Especialista en Voz (NLP):** `[Escribe tu nombre aquí]`
- [ ] **Desarrollador Backend (Volumen/POO):** `[Escribe tu nombre aquí]`
- [ ] **Desarrollador Full-Stack (Web):** `[Escribe tu nombre aquí]`
- [ ] **Project Manager y QA:** `[Escribe tu nombre aquí]`

---

## 🚀 Primeras Misiones Individuales (Semana 1)
Una vez asignados los nombres, esta es la tarea de investigación y prueba que cada uno debe completar esta semana para poder arrancar con el código fuerte la siguiente:

### Ingeniero de Datos
- [ ] Descargar el dataset **"ESC-50"** (es un dataset público y gratuito de audios para machine learning).
- [ ] Investigar cómo instalar y usar la librería `librosa` de Python para leer un archivo de audio `.wav`.

### Especialista ML (KNN)
- [ ] Investigar la documentación oficial de `scikit-learn` en Python, específicamente la clase `KNeighborsClassifier`. Entender qué parámetros necesita para clasificar datos.

### Especialista en Voz
- [ ] Instalar en tu computadora las librerías `SpeechRecognition` y `PyAudio` (comando: `pip install SpeechRecognition pyaudio`).
- [ ] Escribir un pequeño script de 10 líneas que capture tu voz por el micrófono de la laptop y la imprima como texto en la consola.

### Desarrollador Backend
- [ ] Investigar cómo subir o bajar el volumen de Windows usando un script de Python (Librería recomendada para investigar: `pycaw`).
- [ ] Hacer un pequeño script de prueba aislado que cambie el volumen de la PC.

### Desarrollador Full-Stack
- [ ] Instalar el framework web `Flask` (`pip install Flask`).
- [ ] Escribir un archivo `app.py` básico que al ejecutarlo levante una página web en blanco que diga "Sistema de Audio" en `localhost:5000`.

## 🗓️ Cronograma General y Tareas (Semanas 2 a 8)

### 📅 Semana 2: Procesamiento y Pruebas Iniciales
*   **Ing. de Datos:** Escribir el script en Python para leer los audios del dataset y extraer sus características matemáticas (MFCCs).
*   **Especialista ML:** Cargar los datos limpios y hacer el primer entrenamiento básico del modelo KNN.
*   **Especialista Voz:** Crear un script que entienda 3 comandos básicos clave (ej. "Subir", "Bajar", "Pausar").
*   **Desarrollador Backend:** Programar la lógica base para controlar el volumen en Windows (`pycaw`).
*   **Desarrollador Full-Stack:** Diseñar el boceto de la interfaz web (HTML/CSS) y conectarlo con su servidor Flask.
*   **Project Manager/QA:** Validar que los scripts iniciales de todos funcionen bien por separado y subirlos a la carpeta `src/`.

### 📅 Semana 3: Algoritmos y Ajustes
*   **Ing. de Datos:** Optimizar la extracción matemática para que el programa trabaje rápido y sin retraso en tiempo real.
*   **Especialista ML:** Ajustar el valor de "K" y otros parámetros del modelo para subir el porcentaje de precisión de la IA.
*   **Especialista Voz:** Implementar filtros para que la voz se entienda correctamente a pesar de que haya ruido de fondo.
*   **Desarrollador Backend:** Programar el algoritmo "Anti-Estruendos" (subida gradual de volumen 20% -> 80% en 5 segundos).
*   **Desarrollador Full-Stack:** Crear botones interactivos en la web que le envíen instrucciones al backend (AJAX).
*   **Project Manager/QA:** Iniciar redacción de Capítulos 1 y 2 del informe académico.

### 📅 Semana 4: Integraciones Clave
*   **Ing. Datos + Especialista ML:** Conectar el micrófono en vivo al modelo KNN para que la PC escuche y clasifique el ruido sola cada cierto tiempo.
*   **Especialista Voz + Backend:** Conectar los comandos de voz hablados para que interactúen con el control de volumen real de la PC.
*   **Desarrollador Full-Stack:** Hacer que la página web muestre en la pantalla lo que la PC está escuchando (ej. *"Estado: Ducha detectada"*).

### 📅 Semana 5: Ensamblaje Total (POO)
*   **Todo el equipo:** Convertir su código en Clases (Programación Orientada a Objetos) y unirlo en un solo archivo principal `main.py` bajo la coordinación del Project Manager. El sistema ya debe poder escuchar voz y analizar ruidos simultáneamente usando Hilos (Multithreading).

### 📅 Semana 6: Pruebas de Estrés (Testing)
*   **Todo el equipo:** Poner a prueba el sistema reproduciendo música fuerte y ruidos falsos (ej. audios de youtube de gritos o agua) para cazar y documentar errores. Corregir cualquier bug encontrado.
*   **Desarrollador Full-Stack:** Validar que la interfaz web sea responsiva y se pueda manejar cómodamente desde el celular.

### 📅 Semana 7: Documentación Académica
*   **Todo el equipo:** Redactar la parte técnica correspondiente en el informe (Capítulo 4 de Implementación y 5 de Resultados) explicando el código de cada uno.
*   **Project Manager/QA:** Compilar el documento, darle formato APA y redactar las conclusiones.

### 📅 Semana 8: Entrega Final
*   **Todo el equipo:** Ensayar las 8 diapositivas del PPT. 
*   **Project Manager/QA:** Entrega oficial del código final en GitHub y del informe en PDF para el profesor.
