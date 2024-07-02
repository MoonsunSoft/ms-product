/** @odoo-module */

import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";
import { ProductProduct } from "@bi_pos_product_template/app/products/productTemplateListWidget";
import { _t } from "@web/core/l10n/translation";
import { usePos } from "@point_of_sale/app/store/pos_hook";

export class producttemplatepopup extends AbstractAwaitablePopup {
    static components = {ProductProduct};;
    static template = "bi_pos_product_template.producttemplatepopup";
    static defaultProps = {
       confirmText: _t("Ok"),
        title: "",
        body: "",
    };

    /**
     * @param {Object} props
     * @param {string} props.startingValue
     */
    setup() {
        super.setup();
        this.pos = usePos();
    }

    async add_product_variant(ev){
        var options = await ev.getAddProductOptions();
        if(this.env.services.pos.config.allow_selected_close == "auto_close"){
            this.pos.addProductFromUi(ev,options);
            this.cancel();

        }else if(this.env.services.pos.config.allow_selected_close == "selected"){
            this.pos.addProductFromUi(ev,options);
        }
    }
}