odoo.define('demo_html.NavDropdown', function (require) {
"use strict";

const Widget = require('web.Widget');
const SystrayMenu = require('web.SystrayMenu');

const NavDropdown = Widget.extend({
    template: "demo_html.NavDropdown",
    events: {
        'click .dropdown-item': '_itemClick'
    },
    _itemClick: function (e) {
       alert($(e.target).text());
    }
});

SystrayMenu.Items.push(NavDropdown);

});
