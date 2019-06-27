from django.forms.widgets import Widget, Select
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.utils.dates import MONTHS
import datetime
import re
from input_data.models import PenjualanModel
from django.core.exceptions import ObjectDoesNotExist

RE_DATE = re.compile(r'(\d{4})-(\d\d?)-(\d\d?)$')


class MonthYearWidget(Widget):
    template_name = 'month-year-widget.html'
    month_none_value = (0, _('Month'))
  
    month_field = '%s_month'
  
    
    def __init__(self, attrs=None):
        self.attrs = attrs or {}
        #pemanggilan tahun dari databaset

    def render(self, name, value, attrs=None, renderer=None):
        try:
             month_val = value.month
        except AttributeError:
            month_val = 1
            
            if isinstance(value, str):
                match = RE_DATE.match(value)
                if match:
                    year_val, month_val, day_val = [int(v) for v in match.groups()]
        attrs.update(self.attrs)
        id_ = 'id_%s' % name
        month_choices = list(MONTHS.items())
        month_choices.append(self.month_none_value)
        month_choices = sorted(month_choices)
        local_attrs = self.build_attrs(attrs)
        s = Select(choices=month_choices)
        select_html_month = s.render(self.month_field % name, month_val, local_attrs)
        return render_to_string(self.template_name, {"month":select_html_month  })

    def id_for_label(self, id_):
        return '%s_month' % id_

    id_for_label = classmethod(id_for_label)

    def value_from_datadict(self, data, files, name):
        m = data.get(self.month_field % name)
        if  m == "0":
            return None
        if  m:
            return '%s-%s-%s' % (1, m, 1)
        return data.get(name, None)