import inspect
from importlib import util

import pytest

if util.find_spec("playwright"):
    from playwright._impl._page import Page

from taipy.gui import Gui


@pytest.mark.extension
def test_metric_basic_width(page: Page, gui: Gui, helpers):
    page_md = """
<|100|metric|>
"""
    gui._set_frame(inspect.currentframe())
    gui.add_page(name="test", page=page_md)
    helpers.run_e2e(gui)
    page.goto("./test")
    page.wait_for_selector(".plot-container")
    events_list = page.locator("//*[@class='js-plotly-plot']//*[name()='svg'][2]//*[local-name()='text']")
    gauge_value = events_list.nth(0).text_content()
    assert gauge_value == "100"

@pytest.mark.extension
def test_metric_numeric_width(page: Page, gui: Gui, helpers):
    """Test that documents the bug with numeric width/height values"""
    page_md = """
<|100|metric|width=300|height=300|>
"""
    gui._set_frame(inspect.currentframe())
    gui.add_page(name="test", page=page_md)
    helpers.run_e2e(gui)
    page.goto("./test")
    page.wait_for_selector(".plot-container")
    
    plot = page.locator("//*[@class='js-plotly-plot']")
    width = plot.evaluate("el => el.style.width")
    
    # This assertion documents the current buggy behavior
    assert width == "100%", "Width is defaulting to 100% instead of using specified width"
    
@pytest.mark.extension
def test_metric_px_units(page: Page, gui: Gui, helpers):
    """Test that documents the bug with px width/height values"""
    page_md = """
<|100|metric|width=150px|height=300px|>
"""
    gui._set_frame(inspect.currentframe())
    gui.add_page(name="test", page=page_md)
    helpers.run_e2e(gui)
    page.goto("./test")
    page.wait_for_selector(".plot-container")
    
    plot = page.locator("//*[@class='js-plotly-plot']")
    width = plot.evaluate("el => el.style.width")
    
    # This assertion documents the current buggy behavior
    assert width == "100%", "Width is defaulting to 100% instead of using specified px units"