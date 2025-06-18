# NextLift IA



## Descripción

NextLift IA es una aplicación interactiva basada en Streamlit que recomienda de manera inteligente la siguiente carga de entrenamiento de fuerza para el usuario, utilizando su historial de series y un modelo de machine learning entrenado con datos reales y sintéticos.

## Características

- Registro de sesiones serie a serie (peso, repeticiones, RPE).
- Recomendación de carga siguiente basada en un modelo IA (Decision Tree / RandomForest / XGBoost).
- Wizard de 3 pasos: selección de ejercicio, registro de series y resumen con gráfica de progresión.
- Feedback integrado para mejorar la aplicación.

## Requisitos previos

- Python 3.8 o superior
- Git

## Instalación

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/danieghosa/NextLift-IA.git
   cd NextLift-IA
   ```
2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Archivos principales

- `app2.py`: script principal de Streamlit.
- `assets/logo.png`: logo de la aplicación.
- `nextlift_model.pkl`: modelo IA entrenado.
- `.streamlit/config.toml`: configuración del tema.
- `requirements.txt`: lista de dependencias.

## Uso

Ejecutar la aplicación:

```bash
streamlit run app2.py
```

1. Aparecerá el logo y se pedirá tu nombre.
2. Selecciona o ingresa un ejercicio.
3. Registra cada serie con peso, repeticiones y RPE.
4. Obtén la recomendación de la siguiente carga.
5. Finaliza para ver el resumen y la gráfica de progresión.
6. Rellena el formulario de feedback para ayudar a mejorar.

## Contribuciones

Las contribuciones son bienvenidas. Para sugerir mejoras o reportar errores, por favor abre un issue o envía un pull request.

## Licencia

MIT License

---

> **NextLift IA** · Desarrollado por Daniel Eghosa · [LinkedIn](https://www.linkedin.com/in/daniel-eghosa-omoruyi/)