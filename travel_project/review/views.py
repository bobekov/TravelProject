from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max, Min
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from travel_project.review.forms import AddReview
from travel_project.review.models import Review


class DetailsReview(ListView):
    model = Review
    template_name = 'review/details-review.html'

    def get_queryset(self):
        filter_type = self.request.GET.get('filter', None)

        if filter_type == 'lowest':
            min_rating = Review.objects.aggregate(min_rating=Min('rating'))['min_rating']
            return Review.objects.filter(rating=min_rating)
        elif filter_type == 'highest':
            max_rating = Review.objects.aggregate(max_rating=Max('rating'))['max_rating']
            return Review.objects.filter(rating=max_rating)
        else:
            return Review.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.get_queryset()
        return context


class AddNewReview(LoginRequiredMixin, CreateView):
    model = Review
    form_class = AddReview
    template_name = 'review/add-review.html'
    success_url = reverse_lazy('details-review')

    def form_valid(self, form):
        form.instance.user = self.request.user

        if form.instance.destination is None:
            form.instance.destination = None

        response = super().form_valid(form)
        return response


class EditReview(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = AddReview
    template_name = 'review/edit-review.html'
    success_url = reverse_lazy('details-review')

    def get_object(self, queryset=None):
        return get_object_or_404(Review, pk=self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        return response


class DeleteReview(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'review/delete-review.html'
    success_url = reverse_lazy('details-review')

    def get_object(self, queryset=None):
        return get_object_or_404(Review, pk=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        confirmation = request.POST.get('confirmation')
        if confirmation == 'Yes':
            self.get_object().delete()
            return redirect(self.success_url)
        else:
            return redirect('details-review')

