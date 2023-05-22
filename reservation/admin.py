from django import forms
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ArtisteType, Show, Location, Locality, Type, ArtistTypeShow, Representation, Artist, RepresentationUser, Role, RoleUser


class RepresentationInline(admin.StackedInline):
    model = Representation
    extra = 1


class ShowAdminForm(forms.ModelForm):
    representations = forms.ModelMultipleChoiceField(
        queryset=Representation.objects.none(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Show
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ShowAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Show has already been created, so populate existing representations
            self.fields['representations'].queryset = Representation.objects.filter(show_id=self.instance.pk)

    def save(self, commit=True):
        show = super(ShowAdminForm, self).save(commit=commit)
        if commit:
            # Assign the show ID to selected representations
            representations = self.cleaned_data['representations']
            for representation in representations:
                representation.show = show
                representation.save()
        return show


@admin.register(Show)
class ShowAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = ShowAdminForm
    list_display = ('id', 'slug', 'title', 'description', 'poster_url', 'location_id', 'bookable', 'price', 'created_at', 'display_representations')
    inlines = [RepresentationInline]

    def display_representations(self, obj):
        representations = Representation.objects.filter(show_id=obj.id) 
        return ', '.join(str(r) for r in representations)

    display_representations.short_description = 'Representations'


@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'slug', 'designation')


@admin.register(Locality)
class LocalityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'postal_code', 'locality')


@admin.register(Type)
class TypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'type')


@admin.register(ArtistTypeShow)
class ArtistTypeShowAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('artiste_type_id', 'show_id')


@admin.register(Representation)
class RepresentationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('show_id', 'when', 'location_id')


@admin.register(RepresentationUser)
class RepresentationUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('representation_id', 'user_id', 'places')

@admin.register(Artist)
class Artist(ImportExportModelAdmin, admin.ModelAdmin):
    list_display= ('firstname', 'lastname')


admin.site.register(Role)
admin.site.register(RoleUser)


@admin.register(ArtisteType)
class ArtisteType(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('artist_id', 'type_id')