# Script para Combinar PDFs

Este script combina todos los archivos PDF ubicados en una carpeta específica del escritorio del usuario en un único archivo PDF.

## Requisitos

- Python 3.x
- Biblioteca `PyPDF2`

## Instrucciones de Uso

### 1. Preparar el entorno

1. **Clonar o descargar el proyecto**: Coloca el script `combinar_pdfs.py` en una carpeta en tu escritorio.

### 2. Preparar las carpetas de entrada y salida

1. **Crear la carpeta de entrada**:
   - En tu escritorio, crea una carpeta llamada `PDF` si aún no existe.
   - Dentro de `PDF`, crea una subcarpeta llamada `DataIn`.
   - Coloca todos los archivos PDF que deseas combinar dentro de `DataIn`.

2. **La carpeta de salida se creará automáticamente**:
   - El script creará automáticamente una carpeta `DataOut` dentro de `PDF`, donde se guardará el PDF combinado.

### 3. Ejecutar el script

1. **Ejecuta el script**:
   - En la terminal o línea de comandos, asegúrate de estar en la carpeta donde se encuentra el script, y luego ejecuta:
     ```bash
     python combinar_pdfs.py
     ```

### 4. Verificar el resultado

- Una vez ejecutado el script, el archivo PDF combinado se guardará en la carpeta `DataOut` con el nombre `PDFGenerado.pdf`.
- Recibirás un mensaje en la terminal confirmando la ubicación del archivo combinado.

### Notas

- Asegúrate de que todos los archivos PDF en la carpeta `DataIn` sean archivos válidos y estén cerrados antes de ejecutar el script.
- Si deseas modificar las rutas de entrada o salida, puedes hacerlo dentro del script modificando las variables `input_dir` y `output_dir`.

¡Y eso es todo! Con estos simples pasos, podrás combinar tus PDFs de manera local,rápida y eficiente.
