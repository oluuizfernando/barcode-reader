from pyzbar.pyzbar import decode
from pdf2image import convert_from_path
import os

def digitable_line(line):
    #https://www.bb.com.br/docs/pub/emp/mpe/dwn/PadraoCodigoBarras.pdf
    def module10(num):
        sum = 0
        weight = 2
        for c in reversed(num):
            parcial = int(c) * weight
            if parcial > 9:
                s = str(parcial)
                parcial = int(s[0]) + int(s[1])
            sum += parcial
            if weight == 2:
                weight = 1
            else:
                weight = 2
            
        rest10 = sum % 10
        if rest10 == 0:
            module10 = 0
        else:
            module10 = 10 - rest10
        return module10
    
    def create(line):
        line_dv = "%s%s" % (line, module10(line))
        return "%s.%s" % (line_dv[0:5], line_dv[5:])
    
    return " ".join([create(line[0:4] + line[19:24]),
                     create(line[24:34]),
                     create(line[34:44]),
                     line[4],
                     line[5:19]])

def BarcodeReader(pdf_path):
    img = convert_from_path(pdf_path, 500)[0]
    detected_bar_codes = decode(img)

    if detected_bar_codes == False:
        return False
    else:
        for barcode in detected_bar_codes:
            if barcode.data != "" and barcode.type == 'I25':
                return barcode.data.decode('utf-8')

if __name__ == '__main__':
    pdfs = [i for i in os.listdir() if '.pdf' in i]
    
    #returns a list of instances in Pillow
    img = convert_from_path(pdfs[0], 500)[0]
    #500 its the max resolution
    decode(img)[0].data.decode('utf-8')
    decode(img)[0].type