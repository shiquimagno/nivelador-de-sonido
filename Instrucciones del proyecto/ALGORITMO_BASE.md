# 🧠 Lógica del Algoritmo Central (KNN + Volumen + Voz)

Este documento resume cómo funciona el "Cerebro" de nuestro Nivelador de Sonido. Pueden editar este archivo libremente para ajustar la lógica según las preferencias del equipo o los requisitos del profesor.

## 1. Funcionamiento Teórico (Concepto Base)

El sistema funciona mediante un bucle infinito que escucha constantemente el micrófono. Para evitar que el sistema se vuelva loco con ruidos aislados (ej. que se caiga un plato) y suba el volumen por accidente, NO usamos un simple medidor de decibeles. Usamos Inteligencia Artificial (KNN).

*   **Entrenamiento Previo:** El modelo KNN (K-Nearest Neighbors) "estudia" cientos de audios etiquetados (ej. 50 ejemplos de duchas, 50 de silencio, 50 de secadoras de pelo). La librería `librosa` convierte esos audios en números (coeficientes MFCC) y el KNN crea un "mapa" de sonidos.
*   **Ejecución en Vivo:** Cuando el micrófono capta un ruido en tiempo real, extrae sus números y busca a sus "K" vecinos más cercanos en el mapa. Si la mayoría de esos vecinos pertenecen a la categoría "Ducha", la IA clasifica el entorno como "Ducha", ignorando ruidos accidentales.

---

## 2. Pseudocódigo del Sistema Completo

A continuación, el pseudocódigo que une todas las piezas de Programación Orientada a Objetos (POO) en el archivo `main.py`. Es muy útil para colocarlo en su **informe técnico** o PPT.

```text
INICIO DEL SISTEMA

// 1. Inicialización de Clases (Objetos)
procesador = instanciar AudioProcessor()
ia_knn = instanciar NoiseClassifier()
oido_voz = instanciar VoiceListener()
control_volumen = instanciar VolumeController()

// 2. Carga y Entrenamiento (Solo se ejecuta una vez al iniciar la app)
datos_entrenamiento = procesador.cargar_dataset("ESC-50")
ia_knn.train_model(datos_entrenamiento)

// 3. Diccionario de Reglas de Volumen
perfiles_volumen = {
    "Ducha": 80%,
    "Silencio": 30%,
    "Conversacion_Normal": 50%,
    "Ruido_Calle": 90% // Definir límites de audio máximo y mínimoo y detectar si está con audífonos o no para bifurcar la lógica 
}

// 4. Bucle Principal (Se ejecuta siempre en segundo plano)
MIENTRAS el sistema este encendido:
    
    // A. Escuchar Comandos de Voz primero (Tienen la prioridad más alta)
    comando = oido_voz.listen_for_commands()
    SI comando == "Pausar sistema":
        ESPERAR hasta que diga "Reanudar"
        CONTINUAR
    
    SI comando == "Bajar volumen":
        control_volumen.smooth_volume_transition(20%)
        ESPERAR 10 segundos
        CONTINUAR

    // B. Si no hubo comandos de voz, analizar el ruido ambiente
    fragmento_audio = procesador.capturar_microfono(tiempo = 3_segundos)
    caracteristicas = procesador.extract_features(fragmento_audio)
    
    // C. Predicción con Inteligencia Artificial
    ambiente_detectado = ia_knn.predict(caracteristicas)
    
    // D. Ajuste de Volumen Suavizado (Anti-Estruendos)
    SI ambiente_detectado EXISTE EN perfiles_volumen:
        volumen_objetivo = perfiles_volumen[ambiente_detectado]
        
        SI volumen_actual ES DIFERENTE A volumen_objetivo:
            // Sube o baja progresivamente, sin asustar al usuario
            control_volumen.smooth_volume_transition(volumen_objetivo)
    
    // E. Enviar estado actual a la interfaz Web (Flask)
    actualizar_interfaz_web(ambiente_detectado, volumen_objetivo)
    
    // Pausa muy breve antes de volver a escuchar para no sobrecargar el procesador
    ESPERAR 0.1 segundos

FIN MIENTRAS
FIN DEL SISTEMA
```

---

## 3. ¿Qué pueden personalizar y editar en este algoritmo?

1.  **El Diccionario de Reglas (`perfiles_volumen`):** Como equipo, pueden inventar los entornos que quieran siempre y cuando existan en el dataset. Ej: "Licuadora", "Lluvia", "Ladrido de Perro".
2.  **Tiempo de escucha:** En el pseudocódigo se graban fragmentos de `3 segundos`. Si lo bajan a `1 segundo`, el sistema responde más rápido, pero consume más memoria de la computadora. Deben probar qué funciona mejor.
3.  **Lógica de Voz:** ¿Qué pasa si el usuario dice "Volumen al máximo"? Tendrían que agregar ese caso en el bloque de decisiones (Sección 4-A).
