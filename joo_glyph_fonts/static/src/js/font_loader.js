/** @odoo-module **/

import { rpc } from "@web/core/network/rpc";

/**
 * Default font key fallback matching backend settings.
 */
const DEFAULT_FONT_KEY = "dwpiexmincho";

/**
 * Font mapping configuration.
 * Maps backend selection/key values to exact CSS @font-face family names.
 */
const FONT_MAP = {
    dwpiexmincho: "DWPIexMincho",
    dwpimincho: "DWPIMincho",
    ipamjm: "IPAmjMincho",
};

/**
 * Fetches the active font configuration from the backend
 * and sets the CSS variable `--joo-font-dynamic` on `:root`.
 */
async function loadAndApplyFont() {
    try {
        const fontKey = await rpc("/joo_glyph_fonts/font");
        const fontFamily = FONT_MAP[fontKey] || FONT_MAP[DEFAULT_FONT_KEY];

        if (!FONT_MAP[fontKey]) {
            console.warn(
                `[joo_glyph_fonts] Unknown font key '${fontKey}'. Falling back to default ('${DEFAULT_FONT_KEY}').`
            );
        }

        // Apply active font family globally via CSS variable
        document.documentElement.style.setProperty(
            "--joo-font-dynamic",
            `"${fontFamily}"`
        );

        console.debug(`[joo_glyph_fonts] Global dynamic font applied: ${fontFamily}`);
    } catch (err) {
        console.error(
            "[joo_glyph_fonts] Failed to fetch font configuration from server:",
            err
        );
    }
}

// Execute immediately upon module load
loadAndApplyFont();
