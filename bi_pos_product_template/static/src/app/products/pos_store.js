/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { producttemplatepopup } from "@bi_pos_product_template/app/products/producttemplatepopup"

patch(PosStore.prototype, {
    async _processData(loadedData) {
        await super._processData(loadedData);
        let self = this;
        self.product_templates = loadedData['product.template'] || [];
        self.db.product_template_by_id = {};
        this.db.product_tmpl_id = [];
        self.db.add_product_templates(self.product_templates);
    },
    async addProductToCurrentOrder(product, options = {}) {
      
        var self = this;
        const products = event.detail;
        var product_variant = "";
        var alternative_product = "";
        if(self.env.services.pos.config.allow_product_variants){
            var prod_template = this.db.product_template_by_id[product.product_tmpl_id];
            var product_template = prod_template ? prod_template : product;
            var prod_list = [];
            if (product_template.product_variant_count > 1){
                    product_template.product_variant_ids.forEach((prod) => {
                        prod_list.push(self.env.services.pos.db.get_product_by_id(prod));
                    });
                    product_variant = prod_list;
                    await this.env.services.pos.popup.add(producttemplatepopup, {'variant_ids':product_variant, 'alternative_prod':alternative_product});
                } else if(product.to_weight && this.env.services.pos.config.iface_electronic_scale){
                    this.pos.showScreen('scale',{product: product});
                }else{
                    //this.env.services.pos.get_order().add_product(product,options)
                    super.addProductToCurrentOrder(...arguments);
                }      
        }else{
            super.addProductToCurrentOrder(...arguments);
        }
            
    },    
});