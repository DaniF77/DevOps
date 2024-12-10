from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    notes = Note.objects.all()
    return render(request, 'myapp/note_list.html', {'notes': notes})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'myapp/note_form.html', {'form': form})

def note_edit(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'myapp/note_form.html', {'form': form})

def note_delete(request, pk):
    note = Note.objects.get(pk=pk)
    note.delete()
    return redirect('note_list')
