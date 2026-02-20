import csv

with open('alumnos3.csv', 'wt') as escrito:
    csv_writer = csv.writer(escrito, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Nombre', 'Edad', 'Curso'])
    csv_writer.writerow(['David', '21','DAW'])
    csv_writer.writerow(['Pedro', '2','DAW'])
    csv_writer.writerow(['Paco', '12','DAW'])
