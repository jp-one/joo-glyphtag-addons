from odoo import fields, models

# Default font key used across Python models and controllers
DEFAULT_FONT_KEY = "dwpiexmincho"


class ResConfigSettings(models.TransientModel):
    """Configuration settings for joo_glyph_fonts module.

    Configures the primary dynamic font applied to elements with the
    'data-joo-font' attribute via the --joo-font-dynamic CSS variable.
    """

    _inherit = "res.config.settings"

    joo_font = fields.Selection(
        selection=[
            ("dwpiexmincho", "DWPI Extended Mincho"),
            ("dwpimincho", "DWPI Mincho"),
            ("ipamjm", "IPAmj Mincho"),
        ],
        string="Glyph Font",
        default=DEFAULT_FONT_KEY,
        config_parameter="joo_glyph_fonts.font",
        help="Select the default dynamic font applied to UI elements using the 'data-joo-font' attribute.",
    )
