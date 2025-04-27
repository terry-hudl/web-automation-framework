from pathlib import Path
from textwrap import dedent
import re
import time

from behave.model import Scenario, Step
from drivers.webdriver_factory import WebDriverFactory

SCREENSHOT_DIR = Path("reports/screenshots")

def _safe_name(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "_", text)

def before_scenario(context, scenario: Scenario):
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    context.driver = WebDriverFactory.get_driver()

    for fmt in context._runner.formatters:
        if getattr(fmt, "name", None) == "html-pretty":
            context.embed = fmt.embed
            break
    else:
        context.embed = lambda *a, **k: None

    context.scenario = scenario


def after_step(context, step: Step):
    if step.status.name.lower() in {"skipped", "untested"}:
        return

    scenario_part = _safe_name(context.scenario.name)
    step_part = _safe_name(step.name)
    status_part = step.status.name.lower()
    unique = f"L{context.scenario.line}_{int(time.time() * 1_000)}"
    filename = f"{scenario_part}__{step_part}__{status_part}__{unique}.png"
    filepath = SCREENSHOT_DIR / filename

    context.driver.save_screenshot(str(filepath))
    context.embed(
        mime_type="image/png",
        data=str(filepath),
        caption=f"Screenshot ({status_part}): {step.keyword} {step.name}",
    )

    details = dedent(
        f"""\
        Step:    {step.keyword}{step.name}
        Status:  {status_part}
        URL:     {context.driver.current_url}
        Title:   {context.driver.title}
        """
    ).rstrip()

    context.embed(
        mime_type="text/markdown",
        data=details,
        caption="Step details",
    )

def after_scenario(context, scenario: Scenario):
    context.driver.quit()
