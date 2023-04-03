import PyPDF2

pdf=['1.pdf','2.pdf','3.pdf']#you can add many pdf with their correct name
merger=PyPDF2.PdfMerger()
for i in pdf:
  a=open(file,'rb')
  pdfread=PyPDF2.PdfReader(a)
  merger.append(pdfread)
a.close()
merger.write('merger.pdf')