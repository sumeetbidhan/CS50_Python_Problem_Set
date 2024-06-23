from fpdf import FPDF, XPos, YPos

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, 'CS50 Shirtificate', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

def create_shirtificate(name):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    # Add the shirt image
    pdf.image('shirtificate.png', x=0, y=60, w=210)

    full_text = f"{name} took CS50"

    # Add the user's name
    pdf.set_font('Helvetica', 'B', 24)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=55, y=140, text=full_text)

    pdf.output('shirtificate.pdf')

def main():
    name = input("Name: ")
    create_shirtificate(name)

if __name__ == '__main__':
    main()
