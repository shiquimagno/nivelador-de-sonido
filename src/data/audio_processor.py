"""
=========================================================
🧑‍💻 ENCARGADO: Shiquihno Tovar
📅 FECHAS LÍMITES:
   - Semana 1 (26 Sept): Investigar librosa y correr este script de prueba.
   - Semana 2 (03 Oct): Implementar extract_features() real.
   - Semana 3 (10 Oct): Procesamiento de audio en vivo.
=========================================================

Descripción:
Este archivo contiene la clase `AudioProcessor`.
Se encarga de leer el audio, limpiarlo y extraer características numéricas (MFCCs).
"""

class AudioProcessor:
    def __init__(self):
        print("[Shiquihno] Iniciando el Procesador de Audio...")
        
    def extract_features(self, audio_data):
        # TODO: Implementar lógica de librosa aquí
        print("[Shiquihno] Extrayendo características del audio...")
        return {"mfcc": [0.1, 0.5, 0.2]}

# --- CÓDIGO DE PRUEBA INDIVIDUAL ---
if __name__ == "__main__":
    print("--- PRUEBA DE MÓDULO: AUDIO ---")
    procesador = AudioProcessor()
    resultado = procesador.extract_features("dummy_audio.wav")
    print(f"Resultado de la extracción: {resultado}")
