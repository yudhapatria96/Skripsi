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
    year_none_value = (0, _('Year'))
    month_field = '%s_month'
    year_field = '%s_year'
    
    def __init__(self, attrs=None):
        self.attrs = attrs or {}
        #pemanggilan tahun dari databaset
        try:
            years= PenjualanModel.objects.all().order_by('tahun_transaksi')
            if len(years) != 0:
                year_int = years[len(years) - 1].tahun_transaksi
                year_str = str(year_int)
                year_date = datetime.datetime.strptime(year_str, "%Y").date()
                this_year = year_date.year
            else:
                this_year = 2000
        # untuk ganti range tahun
        except ObjectDoesNotExist:
            this_year = 2015
        self.years = range(this_year + 1, this_year + 11)
        super(MonthYearWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None, renderer=None):
        try:
            year_val, month_val = value.year, value.month
        except AttributeError:
            year_val = month_val = None
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
        year_choices = [(i, i) for i in reversed(self.years)]
        year_choices.insert(0, self.year_none_value)
        local_attrs['id'] = self.year_field % id_
        s = Select(choices=year_choices)
        select_html_year = s.render(self.year_field % name, year_val, local_attrs)
        return render_to_string(self.template_name, {"month":select_html_month, "year":select_html_year  })

    def id_for_label(self, id_):
        return '%s_month' % id_

    id_for_label = classmethod(id_for_label)

    def value_from_datadict(self, data, files, name):
        y = data.get(self.year_field % name)
        m = data.get(self.month_field % name)
        if y == m == "0":
            return None
        if y and m:
            return '%s-%s-%s' % (y, m, 1)
        return data.get(name, None)