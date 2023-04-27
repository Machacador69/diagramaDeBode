import numpy as np
import matplotlib.pyplot as plt
import control

def plot_bode(tf):
    mag, phase, omega = control.bode_plot(tf, dB=True, plot=False)
    
    # Crear la figura y los ejes
    fig, (ax_mag, ax_phase) = plt.subplots(2, 1, figsize=(8, 6))
    
    # Graficar la magnitud
    ax_mag.semilogx(omega, 20 * np.log10(mag))
    ax_mag.set_title('Diagrama de Bode')
    ax_mag.set_ylabel('Magnitud [dB]')
    ax_mag.grid(which='both', axis='both')
    
    # Graficar la fase
    ax_phase.semilogx(omega, phase * 180 / np.pi)
    ax_phase.set_xlabel('Frecuencia [rad/s]')
    ax_phase.set_ylabel('Fase [grados]')
    ax_phase.grid(which='both', axis='both')

    # Mostrar la gráfica
    plt.show()

# Función de transferencia G(s) = 100(s+10) / ((s+1)(s+100))
numerator1 = [100, 1000]
denominator1 = [1, 101, 100]
# Función de transferencia G(s) = (5000(s+10)) / (s(s+50)(s+100))
numerator2 = [5000, 50000]
denominator2 = [1, 150, 5000, 0]
# Función de transferencia G(s) = (40(s+10)^2) / (s(s+1)(s+100))
numerator3 = [40, 800, 4000]
denominator3 = [1, 101, 100, 0]
# Función de transferencia G(s) = 25 / (s^2+2.4s+25)
numerator4 = [25]
denominator4 = [1, 2.4, 25]
# Función de transferencia G(s) = 74.25 ((s+30) / ((s+9)(s+90)(s^2+2.4s+25)))
numerator5 = [74.25, 2227.5]
denominator5 = [1, 101.4, 2672.25, 6726, 18000]


tf1 = control.TransferFunction(numerator1, denominator1)
plot_bode(tf1)

tf2 = control.TransferFunction(numerator2, denominator2)
plot_bode(tf2)

tf3 = control.TransferFunction(numerator3, denominator3)
plot_bode(tf3)

tf4 = control.TransferFunction(numerator4, denominator4)
plot_bode(tf4)

tf5 = control.TransferFunction(numerator5, denominator5)
plot_bode(tf5)

