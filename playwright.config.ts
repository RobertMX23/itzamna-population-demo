import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./tests/e2e",
  outputDir: process.env.CI
    ? "test-results"
    : "C:/Users/Rober/AppData/Local/Temp/itzamna-playwright-results",
  timeout: 30_000,
  fullyParallel: true,
  reporter: "line",
  use: {
    baseURL: "http://127.0.0.1:4173",
    trace: "retain-on-failure",
    screenshot: "only-on-failure",
  },
  webServer: {
    command: "python -m http.server 4173",
    url: "http://127.0.0.1:4173/dashboard/",
    reuseExistingServer: false,
    timeout: 30_000,
  },
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"] } },
    { name: "mobile", use: { ...devices["Pixel 5"] } },
  ],
});
