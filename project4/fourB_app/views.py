from django.http import FileResponse
from reportlab.pdfgen import canvas
from fourA_app.models import Project
from django.shortcuts import render
import csv
from io import StringIO, BytesIO

def home(request):
	return render(request,'downloadlist.html')

def generate_csv_file():
    buffer = StringIO()
    writer = csv.writer(buffer)
    projects = Project.objects.all()
    writer.writerow(['Name', 'USN', 'Project','Languages','Duration'])
    for project in projects:
        writer.writerow([project.name, project.usn, project.proj,project.lang,project.duration])
    buffer.seek(0)
    csv_bytes = BytesIO(buffer.getvalue().encode('utf-8'))
    return csv_bytes

def generate_csv(request):
    buffer = generate_csv_file()
    response = FileResponse(buffer, as_attachment=True, filename='project_list.csv')
    return response

def generate_pdf(request):
    response = FileResponse(generate_pdf_file(), as_attachment=True, filename='project_list.pdf')
    return response

def generate_pdf_file():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    projects = Project.objects.all()
    p.drawString(100, 750, "Project List")
    y = 700
    number=0
    for project in projects:
        number+=1
        p.drawString(100, y, f" {number}. Name : {project.name}")
        p.drawString(100, y - 20, f"     USN : {project.usn}")
        p.drawString(100, y - 40, f"     Project : {project.proj}")
        p.drawString(100, y - 60, f"     Languages : {project.lang}")
        p.drawString(100, y - 80, f"     Duration : {project.duration}")
        y -= 100
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer
