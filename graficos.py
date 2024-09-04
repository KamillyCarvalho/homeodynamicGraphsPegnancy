import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# def plotarGrafico(vetor, indices, nome, nome2, cor):
#     spline = make_interp_spline(indices, vetor)
#     x_smooth = np.linspace(indices.min(), indices.max(), 200)
#     y_smooth = spline(x_smooth)
#     fig, ax = plt.subplots(figsize=(10, 5))
#     plt.plot(x_smooth, y_smooth, marker='o', linestyle='-', color=cor)
#     plt.xlabel('Time (weeks)', fontsize=11)
#     plt.xticks(x_smooth)
#     plt.ylabel(r'{}'.format(nome2), fontsize=11)
#     plt.grid(color='w', linestyle='-', linewidth=0.15)
#     legendas = ["E$_0$", "E$_1$", "E$_2$", "E$_3$"]
#     for i, txt in enumerate(vetor):
#         plt.annotate(legendas[i], (x_smooth[i], y_smooth[i]), textcoords="offset points", xytext=(1,-10), ha='left', fontsize=15)
#     name = nome + '.png'
#     plt.savefig(name, format='png')
#     plt.close(fig)  # Fecha a figura após salvá-la para liberar memória
    # return 0

def plotarGrafico(vetor, indices, nome, nome2, cor):
    # Aplica a suavização por spline nos dados de entrada
    spline = make_interp_spline(indices, vetor)
    x_smooth = np.linspace(indices[0], indices[-1], 300)
    y_smooth = spline(x_smooth)
    
    # Cria a figura e o plot
    fig, ax = plt.subplots(figsize=(10, 7))
    plt.plot(x_smooth,y_smooth, marker='none', linestyle='-', linewidth=5, color=cor)
    plt.plot(indices, vetor, marker='o', markersize = 14,linestyle='none', color=cor)
    plt.xticks(indices, fontsize=25)
    plt.yticks(fontsize=24)
    # Configurações dos eixos e grid
    plt.xlabel('Time (weeks)', fontsize=29)
    plt.ylabel(r'{}'.format(nome2), fontsize=30)
    plt.grid(color='w', linestyle='-', linewidth=1)
    
    fig.subplots_adjust(left=0.15,bottom=0.12,right= 0.99,top=0.99)
    # Adiciona legendas ao lado de cada ponto do gráfico
    # legendas = ['pre-pregnancy', '8 weeks', '16 weeks', '24 weeks']
    # for i, txt in enumerate(legendas):
    #     plt.annotate(txt, (indices[i], vetor[i]), textcoords="offset points", xytext=(5,-10), ha='center', fontsize=18)
    
    # Salva o gráfico como imagem PNG
    name = nome + '.png'
    plt.savefig(name, format='png')
    plt.close(fig)  # Fecha a figura após salvá-la para liberar memória


semanas = [0, 8, 16, 24]
freq = [65.00, 68.00, 72.00, 73.00]
q_in = [70.00, 86.67, 98.33, 95.00]
SVR = [1376.00, 969.00, 926.00, 930.00]

plotarGrafico(freq, semanas, 'frequencia', r'Heart Rate (bpm)', 'b')
plotarGrafico(q_in, semanas, 'q_in', r'Blood Flow  (cm$^3$/s)', 'r')
plotarGrafico(SVR, semanas, 'SVR', r'SVR (d.s/cm$^5$)', '#32CD32')