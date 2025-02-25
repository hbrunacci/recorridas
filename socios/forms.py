from crispy_forms.bootstrap import TabHolder, Tab, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, HTML
from django import forms
from django.utils.translation import ugettext_lazy as _
from image_cropping import ImageCropWidget

from cruds_adminlte import (DatePickerWidget,
                            TimePickerWidget,
                            DateTimePickerWidget,
                            ColorPickerWidget,
                            CKEditorWidget)

from .models import Comentarios, Domicilios, Socios, Filtro


class DomiciliosForm(forms.ModelForm):

    class Meta:
        model = Domicilios
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DomiciliosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Field('tipo', wrapper_class="col-md-4"),
            Field('calle', wrapper_class="col-md-4"),
            Field('numero', wrapper_class="col-md-4"),
            Field('piso', wrapper_class="col-md-4"),
            Field('departamento', wrapper_class="col-md-4"),
            Field('otro', wrapper_class="col-md-4"),
            Field('barrio', wrapper_class="col-md-4"),
            Field('ciudad', wrapper_class="col-md-4"),
            Field('partido', wrapper_class="col-md-4"),
            Field('provincia', wrapper_class="col-md-4"),
            Field('codigo_postal', wrapper_class="col-md-4"),

        )

        self.helper.layout.append(
            FormActions(
                HTML("""{% load i18n %}<a class="btn btn-danger"
                        href="{{ url_list }}">{% trans 'Volver' %}</a>"""),
            ))

class PadronFilterForm(forms.ModelForm):
    pass

class FiltrosWebForm(forms.ModelForm):
    class Meta:
        model = Filtro
        fields = '__all__'
        exclude = ['grupo', 'nombre_filtro', 'usuario',]
        widgets = {
            'fecha_nacimiento_desde': DatePickerWidget(attrs={'format': 'mm/dd/yyyy', 'icon': 'fa-calendar'}),
            'fecha_nacimiento_hasta': DatePickerWidget(attrs={'format': 'mm/dd/yyyy', 'icon': 'fa-calendar'}),
            'fecha_socio_desde': DatePickerWidget(attrs={'format': 'mm/dd/yyyy', 'icon': 'fa-calendar'}),
            'fecha_socio_hasta': DatePickerWidget(attrs={'format': 'mm/dd/yyyy', 'icon': 'fa-calendar'}),
        }

    def __init__(self, *args, **kwargs):
        super(FiltrosWebForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Field('categoria', wrapper_class="col-md-5"),
            Field('fecha_nacimiento_desde', wrapper_class="col-md-4"),
            Field('fecha_nacimiento_hasta', wrapper_class="col-md-4"),
            Field('fecha_socio_desde', wrapper_class="col-md-4"),
            Field('fecha_socio_hasta', wrapper_class="col-md-4"),
            Field('codigo_postal', wrapper_class="col-md-4"),
            Field('ciudad', wrapper_class="col-md-4"),
            Field('partido', wrapper_class="col-md-4"),
            Field('provincia', wrapper_class="col-md-4"),
        )



class FiltrosForm(forms.ModelForm):
    class Meta:
        model = Filtro
        fields = '__all__'
        widgets = {
            'fecha_nacimiento_desde': DatePickerWidget(attrs={'format': 'mm/dd/yyyy', 'icon': 'fa-calendar'}),
            'fecha_nacimiento_hasta': DatePickerWidget(attrs={'format': 'mm/dd/yyyy', 'icon': 'fa-calendar'}),
            'fecha_socio_desde': DatePickerWidget(attrs={'format': 'mm/dd/yyyy', 'icon': 'fa-calendar'}),
            'fecha_socio_hasta': DatePickerWidget(attrs={'format': 'mm/dd/yyyy', 'icon': 'fa-calendar'}),
        }

    def __init__(self, *args, **kwargs):
        super(FiltrosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Field('nombre_filtro',wrapper_class="col-md-4"),
            Field('usuario', wrapper_class="col-md-3"),
            Field('categoria', wrapper_class="col-md-5"),
            Field('fecha_nacimiento_desde', wrapper_class="col-md-4"),
            Field('fecha_nacimiento_hasta', wrapper_class="col-md-4"),
            Field('fecha_socio_desde', wrapper_class="col-md-4"),
            Field('fecha_socio_hasta', wrapper_class="col-md-4"),
            Field('codigo_postal', wrapper_class="col-md-4"),
            Field('ciudad', wrapper_class="col-md-4"),
            Field('partido', wrapper_class="col-md-4"),
            Field('provincia', wrapper_class="col-md-4"),
        )
        self.helper.layout.append(
            FormActions(
                Submit('submit', _('Submit'), css_class='btn btn-primary'),
                HTML("""{% load i18n %}<a class="btn btn-danger"
                         href="{{ url_delete }}">{% trans 'Delete' %}</a>"""),
            )
        )


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentarios
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Field('comentario', wrapper_class="col-md-12"),
            Field('nosocio', wrapper_class='col-md-3'),
            Field('fallecido', wrapper_class='col-md-3'),
        )

        self.helper.layout.append(
            FormActions(
                Submit('submit', _('Submit'), css_class='btn btn-primary'),
                HTML("""{% load i18n %}<a class="btn btn-danger"
                        href="{{ url_delete }}">{% trans 'Delete' %}</a>"""),
            )
        )



class SociosForm(forms.ModelForm):

    class Meta:
        model = Socios
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SociosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Field('nro_socio', wrapper_class="col-md-3"),
            Field('apellidos', wrapper_class="col-md-5"),
            Field('nombres', wrapper_class="col-md-4"),
            Field('tipo_documento', wrapper_class="col-md-4"),
            Field('numero_documento', wrapper_class="col-md-4"),
            Field('categoria', wrapper_class="col-md-4"),
            Field('fecha_nacimiento', wrapper_class="col-md-4"),
            Field('fecha_ingreso', wrapper_class="col-md-8"),
        )

        self.helper.layout.append(
            FormActions(
                HTML("""{% load i18n %}<a class="btn btn-danger"
                        href="{{ url_list }}">{% trans 'Volver' %}</a>"""),
            )
        )


