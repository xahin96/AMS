from django.shortcuts import render, HttpResponseRedirect
from django.forms import formset_factory
from django.urls import reverse, reverse_lazy
from django.views import View
from django.http import HttpResponse
from AMSApp.forms import ApprovalRequestForm, IPInformationForm
from AMSApp.models import ApprovalRequest, IPInformation


class Dashboard(View):

    def get(self, request):
        total_request = ApprovalRequest.objects.count()
        all_requests = ApprovalRequest.objects.all()
        context = {
            'title': 'Dashboard',
            'total_request': total_request,
            'all_requests': all_requests
        }
        return render(request, 'AMSApp/dashboard.html', context=context)

    def post(self, request):
        return HttpResponse('Post')


# class CreateRequest(View):
#     form_class = ApprovalRequestForm
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         context = {'title': 'Create New Request', 'form': form}
#         return render(request, 'AMSApp/create_request.html', context=context)
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('AMSApp:dashboard'))
#         context = {'title': 'Create New Request', 'form': form}
#         return render(request, 'AMSApp/create_request.html', context)


def create_request(request):
    ip_information_FormSet = formset_factory(IPInformationForm)

    if request.method == 'POST':

        form = ApprovalRequestForm(request.POST, prefix='form')
        ip_required = form['ip_required'].value()
        if form.is_valid():
            approval_request = form.save()

        form_ip_information = IPInformationForm(request.POST, ip_required=ip_required, instance=None, prefix='form_ip_information')
        if form_ip_information.is_valid():
            fii = form_ip_information.save(commit=False)
            fii.approval_request = approval_request
            fii.save()

            return HttpResponseRedirect(reverse('AMSApp:dashboard'))

        context = {'title': 'Create New Request', 'form': form, 'form_ip_information': form_ip_information}
        return render(request, 'AMSApp/create_request.html', context)

    else:

        form = ApprovalRequestForm(prefix='form')

        ii_formset = ip_information_FormSet(prefix='form_ip_information')
        # form_ip_information = IPInformationForm(prefix='form_ip_information')
        context = {'title': 'Create New Request', 'form': form, 'form_ip_information': ii_formset}
        return render(request, 'AMSApp/create_request.html', context=context)
