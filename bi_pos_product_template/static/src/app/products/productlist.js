/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ProductsWidget } from "@point_of_sale/app/screens/product_screen/product_list/product_list";

patch(ProductsWidget.prototype, {
    get productsToDisplay() {
        let list = [];
        if (this.searchWord !== '') {
            list = this.env.services.pos.db.search_product_in_category(
                this.selectedCategoryId,
                this.searchWord
            ); 
        } else {
            if(this.env.services.pos.config.allow_product_variants){
                list = this.env.services.pos.db.get_product_by_category_variants(this.selectedCategoryId);
            }else{
                list = this.env.services.pos.db.get_product_by_category(this.selectedCategoryId);
            }
        }
        list = list.filter((product) => !this.getProductListToNotDisplay().includes(product.id));
        return list.sort(function (a, b) { return a.display_name.localeCompare(b.display_name) });
    }
    

});