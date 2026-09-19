"""
=========================================================
🧑‍💻 ENCARGADO: Rangel
📅 FECHAS LÍMITES:
   - Semana 1 (26 Sept): Instalar SpeechRecognition y correr prueba.
   - Semana 2 (03 Oct): Implementar listen_for_commands().
   - Semana 3 (10 Oct): Implementar filtros para ruido de fondo.
=========================================================

Descripción:
Este archivo contiene la clase `VoiceListener`.
Escucha el micrófono y detecta comandos verbales.
"""

class VoiceListener:
    def __init__(self):
        print("[Rangel] Inicializando el Reconocedor de Voz...")
        
    def listen_for_commands(self):
        # TODO: Lógica de SpeechRecognition
        print("[Rangel] Escuchando el micrófono...")
        return "bajar volumen"
        
    def adjust_for_ambient_noise(self):
        print("[Rangel] Calibrando el micrófono al ruido ambiente...")

# --- CÓDIGO DE PRUEBA INDIVIDUAL ---
if __name__ == "__main__":
    print("--- PRUEBA DE MÓDULO: VOZ ---")
    oido = VoiceListener()
    oido.adjust_for_ambient_noise()
    comando = oido.listen_for_commands()
    print(f"El usuario dijo el comando: '{comando}'")
