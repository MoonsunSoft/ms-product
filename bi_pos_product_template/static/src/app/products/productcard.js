/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";

import { Component, useEffect, useRef } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";



patch(ProductCard.prototype, {
    setup() {
        super.setup()
        this.pos = usePos();


    },

   
});