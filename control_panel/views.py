from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext

#Vista que muestra la pagina principal del System 
def controlPanel(request):

	return render_to_response('control_panel/control_panel.html',
                              context_instance=RequestContext(request))