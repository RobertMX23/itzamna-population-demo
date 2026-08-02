import { expect, test } from "@playwright/test";

test.describe("INEGI population dashboard", () => {
  test("loads the analytical regions and controls", async ({ page }) => {
    await page.goto("/dashboard/");

    await expect(page.locator("main.shell")).toBeVisible();
    await expect(page.locator(".toolbar")).toBeVisible();
    await expect(page.locator(".metrics")).toBeVisible();
    await expect(page.locator(".grid")).toBeVisible();
    await expect(page.locator(".metrics article")).toHaveCount(3);
    await expect(page.locator(".panel")).toHaveCount(2);
    await expect(page.locator("#period")).toBeVisible();
  });

  test("preserves the compact spacing contract", async ({ page }) => {
    await page.goto("/dashboard/");

    const values = await page.locator(".metrics article, .panel").evaluateAll((elements) =>
      elements.map((element) => {
        const style = getComputedStyle(element);
        return {
          minHeight: style.minHeight,
          padding: style.padding,
        };
      }),
    );

    expect(values.slice(0, 3).every((value) => value.minHeight === "104px")).toBe(true);
    expect(values.slice(0, 3).every((value) => value.padding === "16px 20px")).toBe(true);
    const expectedPanelHeight = (page.viewportSize()?.width ?? 0) <= 760 ? "0px" : "330px";
    expect(values.slice(3).every((value) => value.minHeight === expectedPanelHeight)).toBe(true);
    expect(values.slice(3).every((value) => value.padding === "16px")).toBe(true);
  });

  test("does not overflow on desktop or mobile", async ({ page }) => {
    await page.goto("/dashboard/");
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
    expect(overflow).toBe(false);
  });

  test("filters the analytical window by period", async ({ page }) => {
    await page.goto("/dashboard/");
    await page.locator("#period").selectOption("2018");
    await expect(page.locator("#latest-period")).toHaveText("2018");
    await expect(page.locator("#ranking-title")).toHaveText("Ranking 2018");
    await expect(page.locator("#observation-count")).toHaveText("3");
  });
});
