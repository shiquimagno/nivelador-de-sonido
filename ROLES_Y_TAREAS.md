# 📌 Asignación de Roles y Tareas

Este documento centraliza el trabajo del proyecto "Nivelador de Sonido Dinámico". El proyecto está dividido para 5 integrantes utilizando el paradigma de **Programación Orientada a Objetos (POO)**. Cada integrante será dueño exclusivo de una **Clase (`Class`)** en Python.

## 👥 Equipo y Responsabilidad de Código (POO)

1. **Ingeniero de Datos (Shiquihno Tovar):** 
   - **Clase asignada:** `AudioProcessor` (Ubicada en `src/data/audio_processor.py`)
   - **Responsabilidad:** Leer audio del micrófono, limpiarlo y extraer números (MFCCs).
2. **Especialista ML/KNN (Alessandro Cámara):**
   - **Clase asignada:** `NoiseClassifier` (Ubicada en `src/ml/knn_model.py`)
   - **Responsabilidad:** Entrenar el algoritmo KNN y predecir en qué entorno estamos.
3. **Especialista Voz/NLP (Rangel):**
   - **Clase asignada:** `VoiceListener` (Ubicada en `src/voice/voice_recognizer.py`)
   - **Responsabilidad:** Escuchar micrófono en paralelo y reconocer comandos verbales.
4. **Desarrollador Backend (Carlos Manrique):**
   - **Clase asignada:** `VolumeController` (Ubicada en `src/core/volume_controller.py`)
   - **Responsabilidad:** Alterar el volumen general de Windows de manera progresiva.
5. **Desarrollador Full-Stack (Diego Tello):**
   - **Clase asignada:** `WebApp` (Ubicada en `src/web/app.py`)
   - **Responsabilidad:** Crear la interfaz web visual (HTML/CSS) y el servidor (Flask).

---

## 🚀 Primeras Misiones Individuales (Semana 1)

*   **Shiquihno:** Descargar el dataset **"ESC-50"** e investigar cómo instalar y usar la librería `librosa`.
*   **Alessandro:** Investigar la clase `KNeighborsClassifier` de `scikit-learn`.
*   **Rangel:** Instalar las librerías `SpeechRecognition` y `PyAudio`, y probar que capten su voz.
*   **Carlos:** Investigar la librería `pycaw` para controlar volumen de Windows mediante código.
*   **Diego:** Instalar `Flask` y lograr levantar una página web "Hola Mundo" en `localhost:5000`.

---

## 🗓️ Cronograma General Enfocado en POO (Semanas 2 a 8)

### 📅 Semana 2: Constructores y Métodos Básicos
*   **Shiquihno:** Programar el método `__init__()` y `extract_features(audio_path)` en su clase `AudioProcessor`.
*   **Alessandro:** Programar el método `train_model(dataset)` en su clase `NoiseClassifier`.
*   **Rangel:** Programar el método `listen_for_commands()` en su clase `VoiceListener`.
*   **Carlos:** Programar el método `set_system_volume(nivel)` en su clase `VolumeController`.
*   **Diego:** Diseñar la maqueta web en HTML (carpeta `src/web/templates/`) y conectarla a Flask.

### 📅 Semana 3: Lógica Avanzada (El cerebro y los músculos)
*   **Shiquihno:** Crear método para procesar audio "en vivo" desde el micrófono.
*   **Alessandro:** Ajustar hiperparámetros del KNN y crear método `predict(audio_features)`.
*   **Rangel:** Añadir un filtro para que `VoiceListener` evite el ruido de fondo (método `adjust_for_ambient_noise()`).
*   **Carlos:** Programar el método complejo `smooth_volume_transition(target_level)` para que el cambio no aturda (ej. Subir volumen en 5 segundos mediante un bucle).
*   **Diego:** Crear botones interactivos en la web que envíen peticiones al servidor web.

### 📅 Semana 4: Integración Parcial
*   **Shiquihno + Alessandro:** Instanciar sus clases juntas. Que un Objeto `AudioProcessor` le mande las características en vivo al Objeto `NoiseClassifier` para que decida qué ambiente es.
*   **Rangel + Carlos:** Conectar comandos de voz: Si el Objeto `VoiceListener` escucha "Bajar Volumen", que llame al método del Objeto `VolumeController`.

### 📅 Semana 5: Ensamblaje Total (El Archivo main.py)
*   **Todo el equipo:** Trabajar en el archivo central `src/main.py`. Aquí se importarán y crearán los 5 Objetos:
    ```python
    procesador = AudioProcessor()
    ia_knn = NoiseClassifier()
    oido_voz = VoiceListener()
    control_volumen = VolumeController()
    interfaz = WebApp()
    ```
    Se usarán **Hilos (`threading`)** para que el servidor web, el KNN y el escuchador de voz funcionen al mismo tiempo sin que la aplicación se "cuelgue".

### 📅 Semana 6: Pruebas de Estrés (Testing)
*   **Todo el equipo:** Correr `main.py` en vivo. Reproducir música real en Spotify e intentar simular duchas o ruidos fuertes. Cazar bugs, afinar el modelo KNN y asegurar que todo fluya.

### 📅 Semana 7: Documentación Académica (El Informe)
*   **Carlos y Shiquihno:** Redactar Capítulos 1, 2 y 3 (Introducción, Metodología, Arquitectura y Clases).
*   **Todos:** Redactar su parte técnica en el Capítulo 4 (Implementación), pegando fragmentos de sus Clases y explicando su lógica de POO.
*   **Diego y Alessandro:** Redactar Capítulos 5 y 6 (Pruebas, Capturas de la Interfaz Web, Precisión del KNN y Conclusiones).

### 📅 Semana 8: Entrega Final
*   **Rangel:** Liderar la creación de las 8 diapositivas PPT extrayendo lo mejor del informe.
*   **Todos:** Ensayar PPT, revisar que el código esté limpio en GitHub y entregar PDF del informe.

---

## 📚 Recursos y Documentación Oficial (Links Clave)

Para acelerar el desarrollo, aquí tienen los links oficiales de las herramientas que cada uno debe dominar:

*   **Ing. de Datos (Shiquihno):** 
    *   Dataset ESC-50: [GitHub de ESC-50](https://github.com/karolpiczak/ESC-50)
    *   Tutorial Librosa (Extracción MFCC): [Librosa Feature Extraction](https://librosa.org/doc/latest/feature.html)
*   **Especialista ML (Alessandro):** 
    *   Documentación de KNN: [Scikit-learn KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
*   **Voz (Rangel):** 
    *   Documentación de Voz: [SpeechRecognition PyPI](https://pypi.org/project/SpeechRecognition/)
*   **Backend (Carlos):** 
    *   Controlar audio en Windows: [PyCaw GitHub](https://github.com/AndreMiras/pycaw)
*   **Full-Stack (Diego):** 
    *   Tutorial Flask: [Flask Quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
