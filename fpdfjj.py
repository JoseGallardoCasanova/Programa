 self.image('Merced.png', 10, 8, 33)
            
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 12)
    
    pdf.cell(200, 10, "Estimado/a " + paciente + " Rut: " + rut, ln=15, align="C")
    pdf.cell(200, 10, "Su cita ha sido agendada para el día " + fecha + " con el siguiente detalle: ", ln=16, align="C")
    pdf.cell(200, 10, "Fecha: " + fecha, ln=17, align="C")
    pdf.cell(200, 10, "Hora" + hora, ln=18, align="C")
    pdf.cell(200, 10, "Doctor(a) " + doctor, ln=19, align="C")
    pdf.cell(200, 10, "Sucursal: Centro Odontologico Merced", ln=20, align="C")
    pdf.cell(200, 10, "Motivo: Urgencia Dental", ln=21, align="C")
    pdf.image("Merced.png", 80, 22, 15, 38, "png")


    pdf.output(paciente + ".pdf", "F")  