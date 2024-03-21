import control as ct
import numpy as np
import matplotlib.pyplot as plt

# Definição da planta
num = [5, 10]  # Coeficientes do numerador
den = [4, 7, 20]  # Coeficientes do denominador
sys = ct.TransferFunction(num, den)

# Calculando a resposta ao degrau
t, y = ct.input_output_response(sys)

# Plotando a saída
plt.plot(t, y)
plt.title('Resposta ao degrau da planta')
plt.xlabel('Tempo')
plt.ylabel('Saída')
plt.grid(True)
plt.show()