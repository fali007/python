import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import pandas as pd

def pdf_gen():
	data=pd.read_csv('survey.csv')
	data=data[['Name','Roll Number','Name of Guest 1','Name of Guest 2','Username']]
# name=data[['Name']]
# roll=data[['Roll Number']]
# guest=data[['Name of Guest 1','Name of Guest 2']]


	for i in range(0,len(data)):
		filename=data.loc[i]['Roll Number']+'.pdf'
		doc = SimpleDocTemplate(filename,pagesize=letter,
                        	rightMargin=72,leftMargin=72,
                        	topMargin=72,bottomMargin=18)
		Story=[]
		logo = "logo.png"
		insti_name = "NITC Convocation"
		year = '2k16 - 2k20'
 
		formatted_time = time.ctime()
		full_name = data.loc[i]['Name']
		address_parts = data.loc[i]['Roll Number']
 
		im = Image(logo, 3*inch, 2*inch)
		Story.append(im)
 
		styles=getSampleStyleSheet()
		styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
		ptext = '<font size=12>%s</font>' % formatted_time
 
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
 
		ptext = '<font size=12>%s</font>' % full_name
		Story.append(Paragraph(ptext, styles["Normal"]))       
	
		ptext = '<font size=12>%s</font>' % address_parts
		Story.append(Paragraph(ptext, styles["Normal"]))   
 
		Story.append(Spacer(1, 12))
		ptext = '<font size=12>Dear %s:</font>' % full_name
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
 
		ptext = '<font size=12>We would like to welcome you and %s, %s to %s  %s </font>' % (data.loc[i]['Name of Guest 1'],data.loc[i]['Name of Guest 2'],insti_name,year)
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))
 
 
		ptext = '<font size=12>Thank you</font>'
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))
		ptext = '<font size=12>Sincerely,</font>'
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		ptext = '<font size=12>Director</font>'
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		doc.build(Story)
