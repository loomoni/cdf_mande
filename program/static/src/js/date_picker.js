odoo.define('program.date_picker', function (require) {
    "use strict";

    var core = require('web.core');
    var field_registry = require('web.field_registry');
    var AbstractField = require('web.AbstractField');

    var MonthYearPicker = AbstractField.extend({
        template: 'MonthYearPicker',
        supportedFieldTypes: ['char'],
        events: {
            'change input': '_onChange',
        },

        start: function () {
            this.$input = this.$el.find('input');
            this.$input.datepicker({
                format: "mm/yyyy",
                minViewMode: "months",
                autoclose: true
            });
        },

        _onChange: function (event) {
            this._setValue(event.target.value);
        }
    });

    field_registry.add('date_picker', MonthYearPicker);
});
