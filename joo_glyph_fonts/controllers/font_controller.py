from odoo import http
from odoo.http import request

from ..models.res_config_settings import DEFAULT_FONT_KEY


class FontController(http.Controller):
    """Controller for retrieving the configured web font for the joo_glyph_fonts module.

    This endpoint is called by font_loader.js to dynamically set the
    --joo-font-dynamic CSS variable for elements using the 'data-joo-font'
    attribute.
    """

    @http.route("/joo_glyph_fonts/font", type="jsonrpc", auth="user")
    def get_font(self):
        """Return the configured font key stored in ir.config_parameter.

        Only authenticated users can access this value as part of system
        configuration.
        """
        return (
            request.env["ir.config_parameter"]
            .sudo()
            .get_param("joo_glyph_fonts.font", DEFAULT_FONT_KEY)
        )
