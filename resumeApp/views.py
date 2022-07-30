from django.http import FileResponse

def resume(request):
    return FileResponse(open(
        'C:\\Users\\dcrash0veride\\PycharmProjects\\resume3.0\\gda\\resumeApp\\templates\\resume\\resume.pdf', 'rb'),
        as_attachment=False,content_type='application/pdf')