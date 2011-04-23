from schleich.catalogue.models import Animal, Species, Other, Relationship, Story
from django.contrib import admin

from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)
            output.append(u' <a href="/%s" target="_blank"><img src="/%s" alt="%s" width="200px"/></a> %s ' % \
                (image_url, image_url, file_name, _('Change:')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class AnimalInline(admin.StackedInline):
    model = Animal
    extra = 1

class SpeciesAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ['species_name', 'subspecies_name', 'scientific_name', 'status', 'global_home', 'primary_habitat']
    inlines = [AnimalInline]
    list_display = ('subspecies_name', 'species_name', 'status', 'global_home')
    list_filter = ['global_home', 'species_name', 'primary_habitat']
    search_fields = ['species_name', 'subspecies_name'] 

class RelationshipAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('first_animal', 'relationship', 'second_animal'),)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'description': ('This is entirely optional'),
            'fields': ('image', 'information')
        }),
    )
    list_display = ( '__unicode__', 'first_animal', 'second_animal')
    list_filter = ['relationship']
    search_fields = ['first_animal', 'second_animal', 'information',]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(RelationshipAdmin,self).formfield_for_dbfield(db_field, **kwargs)
 
class AnimalAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', 'species', 'age', 'gender', 'catalogue_number', 'year_made')
    list_filter = ['species', 'age', 'gender', 'year_made']
    search_fields = ['personality', 'name', 'posture', 'special_markings', 'other_information']   
    prepopulated_fields = {"slug": ("name", )}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(AnimalAdmin,self).formfield_for_dbfield(db_field, **kwargs)
    
class StoryAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title', 'desc')
    fields = ['title', 'desc', 'slug', 'story']
    prepopulated_fields = {"slug": ("title", )}    


class OtherAdmin(admin.ModelAdmin):
    fields = ['category', 'model_type', 'catalogue_number', 'year_made', 'name', 'gender', 'weight', 'height', 'global_home', 'status', 'scientific_name']
    list_display = ('model_type', 'category')


admin.site.register(Species, SpeciesAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Other, OtherAdmin)
admin.site.register(Relationship, RelationshipAdmin)
admin.site.register(Story, StoryAdmin)
