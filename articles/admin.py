from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleTags, Tags


class ArticleTagsInLineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                counter += 1
                continue
        if counter > 1:
            raise ValidationError('Нужно выбрать только один основной раздел')
        return super().clean()


class AricleTagsInline(admin.TabularInline):
    model = ArticleTags
    formset = ArticleTagsInLineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [AricleTagsInline]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass