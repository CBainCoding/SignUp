from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EnquiryForm

# Create your views here.


@login_required
def submit_enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.user = request.user
            enquiry.save()
            return redirect('success')
    else:
        form = EnquiryForm()
    return render(request, 'enquiry.html', {'form': form})

    def enquiry_success(request):
        return render(request, 'success.html')