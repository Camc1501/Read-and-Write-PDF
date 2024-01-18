import PyPDF2

def fuec_by_hotel(filename,hoteles):
    pdf_file = open(filename, 'rb')
    read_pdf = PyPDF2.PdfReader(pdf_file)

    print(len(read_pdf.pages))

    
    dict_hotels ={hotel:[] for hotel in hoteles}
    

    for page in range(len(read_pdf.pages)):
        page_content = read_pdf.pages[page].extract_text()
        
        for hotel in hoteles:
            if hotel in page_content:
                dict_hotels[hotel].append(page)

    print(dict_hotels)

    for hotel in dict_hotels:
        writer = PyPDF2.PdfWriter()
        print(f'Hotel->{hotel}')
        for page in dict_hotels[hotel]:
            
            print(f'escribiendo pagina {page}')
            writer.add_page(read_pdf.pages[page])
        
        output_filename= f'D:\Escritorio\FUEC\salida\FUEC LZM 215 {hotel}.pdf'
        with open(output_filename, 'wb') as output:
            writer.write(output)

#*Fuecs AGL
fuec_by_hotel('D:\Escritorio\FUEC\FUEC LZM 215 AGL Vans Hoteles y Empresas.pdf',
         ['AC HOTEL BOGOTA ZONA T','BH 93','BH USAQUEN','BOGOTA PLAZA','FUNDACION SANTA FE','LADRILLERA','MARRIOTT','NOVOTEL'])

#*Fuecs El Sol
fuec_by_hotel('D:\Escritorio\FUEC\FUEC LZM 215 TDS Hoteles, Empresas y Geopark.pdf',['AGL VANS','DANN CARLTON'])