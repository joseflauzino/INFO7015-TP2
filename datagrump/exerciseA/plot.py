import os
import sys
import matplotlib.pyplot as plot
from matplotlib import colors as mcolors

def make_plot(data):
	x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 220, 240, 280, 300, 350]
	fig = plot.figure(figsize=(15,5))
	axes = fig.add_subplot(111)
	axes.bar(x, data, width=1, edgecolor='White', alpha=0.8, color='#086A87')
	axes.set_xlabel("Tamanho da Janela de Congestionamento")
	plot.axis((0,360,0,14.0))
	axes.set_ylabel("Potencia (Taxa de Transferencia / Atraso")
	plot.savefig("plot.png")

def make_plot_zoom(data_zoom):
	x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40]
	fig = plot.figure(figsize=(15,5))
	
	axes = fig.add_subplot(111)
	axes.bar(x, data_zoom, width=0.8, edgecolor='White', alpha=0.6, color='#086A87')
	for i in range(len(x)):
		axes.text(x[i] + 0.0, data_zoom[i] + 0.2, truncate(data_zoom[i], 2), fontsize=7, color='#0B3861')
	
	axes.set_xlabel("Tamanho da Janela de Congestionamento")
	plot.axis((0,35,0,14.0))
	axes.set_ylabel("Potencia (Taxa de Transferencia / Atraso)")
	plot.savefig("plot_zoom.png")

def make_plot_best(data_best):
	x = [10, 11, 12, 13, 14, 15]
	fig = plot.figure(figsize=(15,5))
	
	axes = fig.add_subplot(111)
	axes.bar(x, data_best, width=0.8, edgecolor='White', alpha=0.6, color='#086A87')
	for i in range(len(x)):
		axes.text(x[i] + 0.25, data_best[i] - 0.1, truncate(data_best[i], 2), fontsize=16, color='w')
	
	axes.set_xlabel("Tamanho da Janela de Congestionamento")
	plot.axis((9,16,12,13.0))
	axes.set_ylabel("Potencia Mediana")
	plot.savefig("plot_best.png")

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '%.12f' % f
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def read_all_file():
	data = []
	f = open('output.txt', 'r')
	texto = f.readlines()
	for linha in texto :
	    teste = linha.split(" ")
	    p = round((float(teste[0]) / float(teste[1]))*1000,4)
	    potency = float("{0:.4f}".format(p))
	    data.append(potency)
	f.close()
	return data

def read_zoom_file():
	data = []
	f = open('output.txt', 'r')
	text = f.readlines()
	i = 1
	for line in text :
		if i <= 22:
			part = line.split(" ")
			p = round((float(part[0]) / float(part[1]))*1000,4)
			potency = float("{0:.4f}".format(p))
			data.append(potency)
		i = i+1
	f.close()
	return data

def read_best_file():
	data = []
	for j in range(1,31):
		file_best = 'best/best%s.txt' % j
		batery = []
		f = open(file_best, 'r')
		text = f.readlines()
		for line in text:
			part = line.split(" ")
			p = round((float(part[0]) / float(part[1]))*1000,4)
			potency = float("{0:.4f}".format(p))
			batery.append(potency)
		data.append(batery)
		f.close()
	return data

def median_best(data):
	aux = []
	sorted_aux = []
	final_data = []	
	wnd=0
	for wnd in range(16):
		for line in data:	
			aux.append(line[wnd])
		sorted_aux = sorted(aux)
		final_data.append(sorted_aux[4])
		del aux[:]
		del sorted_aux[:]
	return final_data

def main():
	data = read_all_file()
	data_zoom = read_zoom_file()
	data_best = read_best_file()
	data_best = median_best(data_best)

	make_plot_best(data_best)
	make_plot(data)
	make_plot_zoom(data_zoom)

if __name__ == "__main__":
	main()
