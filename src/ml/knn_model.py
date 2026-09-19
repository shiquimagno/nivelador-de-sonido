"""
=========================================================
🧑‍💻 ENCARGADO: Alessandro Cámara
📅 FECHAS LÍMITES:
   - Semana 1 (26 Sept): Investigar scikit-learn y correr este script.
   - Semana 2 (03 Oct): Implementar train_model() con datos de prueba.
   - Semana 3 (10 Oct): Ajustar KNN y lograr predicciones precisas.
=========================================================

Descripción:
Este archivo contiene la clase `NoiseClassifier`.
Entrena y utiliza el modelo K-Nearest Neighbors para clasificar ruido.
"""

class NoiseClassifier:
    def __init__(self):
        print("[Alessandro] Inicializando el Modelo KNN (K=5)...")
        # self.model = KNeighborsClassifier(n_neighbors=5)
        
    def train_model(self, X_train, y_train):
        # TODO: Entrenar el modelo
        print("[Alessandro] Entrenando el modelo con los datos proporcionados...")
        
    def predict(self, features):
        # TODO: Predecir el ambiente basado en las características
        print("[Alessandro] Analizando características...")
        return "Ducha"

# --- CÓDIGO DE PRUEBA INDIVIDUAL ---
if __name__ == "__main__":
    print("--- PRUEBA DE MÓDULO: MACHINE LEARNING ---")
    ia = NoiseClassifier()
    ia.train_model([], [])
    prediccion = ia.predict([0.1, 0.5, 0.2])
    print(f"El KNN predice que el ambiente es: {prediccion}")
