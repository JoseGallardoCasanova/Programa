from tkinter import *
from fpdf import FPDF

ventana = Tk()
ventana.title("Control Pacientes")

#Funciones


class PDF(FPDF):
        
    

    def header(self):
        titulo = "Centro Odontologico Merced"
        self.image('Merced.png', 10, 8, 33)
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, titulo, 1, 0, 'C')
        self.ln(20)





def generarPDF():

    paciente = text_paciente.get()
    doctor = text_doctor.get()
    rut = text_rut.get()
    hora = text_hora.get()
    fecha = text_fecha.get()
     

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font("Arial", "B", 12)
    
    pdf.cell(200, 10, "Estimado/a " + paciente + " Rut: " + rut, ln=15, align="C")
    pdf.cell(200, 10, "Su cita ha sido agendada para el día " + fecha + " con el siguiente detalle: ", ln=16, align="C")
    pdf.cell(200, 10, "Fecha: " + fecha, ln=17, align="C")
    pdf.cell(200, 10, "Hora" + hora, ln=18, align="C")
    pdf.cell(200, 10, "Doctor(a) " + doctor, ln=19, align="C")
    pdf.cell(200, 10, "Sucursal: Centro Odontologico Merced", ln=20, align="C")
    pdf.cell(200, 10, "Motivo: Urgencia Dental", ln=21, align="C")
    

    pdf.output(paciente + ".pdf", "F")  




#Datos entrada paciente, rut,  fecha, hora y  doctor
text_paciente = Entry(ventana, font= ("Arial 10"), width=50)
text_paciente.grid(row = 0, column = 1, columnspan = 4, padx = 10, pady = 20)
label_paciente = Label(ventana, text = "Nombre Paciente", width = 20, height = 2, font = "Arial 10")
label_paciente.grid(row = 0, column = 0 , padx = 10, pady = 20)

text_rut = Entry(ventana, font= ("Arial 10"), width=50)
text_rut.grid(row = 1, column = 1, columnspan = 4, padx = 10, pady = 20)
label_rut = Label(ventana, text = "Rut paciente", width = 20, height = 2, font = "Arial 10")
label_rut.grid(row = 1, column = 0 , padx = 10, pady = 20)

text_fecha = Entry(ventana, font= ("Arial 10"), width=50)
text_fecha.grid(row = 2, column = 1, columnspan = 4, padx = 10, pady = 20)
label_fecha = Label(ventana, text = "Fecha", width = 20, height = 2, font = "Arial 10")
label_fecha.grid(row = 2, column = 0 , padx = 10, pady = 20)

text_hora = Entry(ventana, font= ("Arial 10"), width=50)
text_hora.grid(row = 3, column = 1, columnspan = 4, padx = 10, pady = 20)
label_hora = Label(ventana, text = "Hora ", width = 20, height = 2, font = "Arial 10")
label_hora.grid(row = 3, column = 0 , padx = 10, pady = 20)

text_doctor = Entry(ventana, font= ("Arial 10"), width=50)
text_doctor.grid(row = 4, column = 1, columnspan = 4, padx = 10, pady = 20)
label_doctor = Label(ventana, text = "Nombre Doctor", width = 20, height = 2, font = "Arial 10")
label_doctor.grid(row = 4, column = 0 , padx = 10, pady = 20)

boton = Button(ventana, text="Generar PDF", width=70, height= 5, command = lambda: generarPDF())
boton.grid(row = 5, column = 0, columnspan= 5, padx = 10, pady = 20)




ventana.mainloop()