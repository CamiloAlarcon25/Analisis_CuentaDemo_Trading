# Análisis de Rendimiento de Cuenta Demo de Trading (MT5 y Power BI)
## 1. Resumen y Objetivos
Este proyecto se centra en la extracción, procesamiento y análisis del rendimiento de una cuenta de trading de demostración (demo) operada en la plataforma MetaTrader 5 (MT5).
El objetivo principal es evaluar la eficacia de la estrategia de trading mediante la visualización de métricas financieras clave (Beneficio, Comisión, Swap) y estadísticas avanzadas de rendimiento (Factor de Beneficio, Ratio B/P, Tasa de Acierto). Se busca identificar la curva de capital, la consistencia de las ganancias y la distribución de los resultados.
## 2. Tecnologías y Herramientas
### MetaTrader 5: (MT5)	Fuente de datos inicial (exportación de registros de operaciones).
### Python:	Separación y preprocesamiento de las tres tablas de datos clave.
### Power BI:	Limpieza, modelado de datos (relacionamiento de tablas), creación de métricas DAX y visualización del dashboard.
## 3. Desarrollo y Modelado de Datos
El pipeline de datos se diseñó para manejar la estructura de exportación de MT5, que combina tres tipos de registros transaccionales en una única fuente: Órdenes, Posiciones y Transacciones.
### A. Preprocesamiento (Python)
Se implementa un script de Python para procesar el archivo exportado y realizar una separación fundamental, generando tres tablas de salida independientes:
#### 1.	Órdenes: Registros de entradas al mercado (pendientes/ejecutadas).
#### 2.	Posiciones: Registros de operaciones cerradas y su resultado.
#### 3.	Transacciones: Registros de depósitos, retiros y ajustes de cuenta.
### B. Modelado en Power BI
Las tres tablas se cargan en Power BI, donde se limpian y se establece la relación uno-a-muchos necesaria. La tabla Posiciones actúa como la tabla de hechos principal, conectando la información transaccional con las dimensiones de tiempo.
Adicionalmente, se creó una Tabla Calendario (utilizando DAX) para permitir el análisis de tendencias y la segmentación temporal (Mes)1.
## 4. Resultados y Análisis Clave
El dashboard proporciona las siguientes conclusiones sobre la cuenta demo:
### •	Rendimiento Acumulado: El rendimiento líquido de la cuenta es de $827,88 2, generado a partir de un Beneficio total de $1.472,75 3, tras deducir Comisiones ($-527,12) 4y Swap ($-117,75)5.
### •	Métricas de Estrategia:
#### o	Factor de Beneficio: El valor es de 1,196. Un valor superior a 1,0 indica que el Beneficio Bruto supera a las Pérdidas Brutas.
#### o	Ratio Beneficio/Pérdida (Ratio B/P): El ratio es de 1,527.
#### o	Tasa de Acierto (Win Rate): La estrategia registra una Tasa de Acierto del 43,92% (65 entradas positivas) 8888, lo que significa que el 56,08% de las operaciones fueron negativas (83 entradas negativas)9. La rentabilidad se mantiene gracias al alto Ratio B/P.
### •	Curva de Capital: La curva muestra una alta volatilidad 10, con un drawdown significativo en octubre 11, seguido por una fuerte recuperación en noviembre12, indicando que la estrategia es rentable pero no totalmente consistente mes a mes.
### •	Filtros de Análisis: Los filtros por Mes, Tipo de Operación (buy o sell) y Símbolo (EURUSD o GBPUSD) permiten una segmentación detallada del rendimiento.

Enlace de Dashboard en Formato PDF:
https://github.com/CamiloAlarcon25/An-lisis-de-Rendimiento-de-cuenta-demo-de-trading/blob/main/pbix_TradingDemo.pdf
