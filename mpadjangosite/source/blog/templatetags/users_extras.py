from django import template
from source.blog.forms import SearchForm


register = template.Library()


@register.inclusion_tag('block/navbar.html')
def show_navbar_with_search_form(request, tag_slug=None):
    if 'search' in request.GET:
        form = SearchForm(request.GET)
    else:
        form = SearchForm()
        if 'tag' in request.get_full_path():
            form.fields['search'].widget.attrs['placeholder'] = 'Поиск по тэгам'
        else:
            form.fields['search'].widget.attrs['placeholder'] = 'Глобальный поиск'
    context = {
        'form': form,
        'request': request,
        'tag_slug': tag_slug
    }
    return context
