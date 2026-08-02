const state = { catalog: null, indicatorId: "P01-POP-TOTAL", geoArea: "01", period: "all" };
const $ = (id) => document.getElementById(id);
const format = (value) => new Intl.NumberFormat("es-MX").format(value);

async function load() {
  const response = await fetch("../data/synthetic/catalog.json");
  state.catalog = await response.json();
  const indicator = $("indicator");
  state.catalog.indicators.forEach((item) => indicator.add(new Option(item.indicator_name, item.indicator_id)));
  state.catalog.geographies.forEach((item) => $("geography").add(new Option(item.geo_name, item.geo_area)));
  const periods = [...new Set(state.catalog.indicators.flatMap((item) => item.observations.map((row) => row.time_period)))].sort();
  periods.forEach((period) => $("period").add(new Option(period, period)));
  indicator.value = state.indicatorId;
  $("geography").value = state.geoArea;
  indicator.addEventListener("change", (event) => { state.indicatorId = event.target.value; render(); });
  $("geography").addEventListener("change", (event) => { state.geoArea = event.target.value; render(); });
  $("period").addEventListener("change", (event) => { state.period = event.target.value; render(); });
  render();
}

function observations() {
  return state.catalog.indicators.find((item) => item.indicator_id === state.indicatorId).observations
    .filter((item) => item.geo_area === state.geoArea)
    .filter((item) => state.period === "all" || Number(item.time_period) <= Number(state.period));
}

function render() {
  const rows = observations();
  if (!rows.length) return;
  const latest = rows.at(-1);
  const previous = rows.at(-2);
  const change = previous ? ((latest.value - previous.value) / previous.value) * 100 : null;
  $("latest-value").textContent = format(latest.value);
  $("latest-period").textContent = latest.time_period;
  $("change-value").textContent = change === null ? "--" : `${change >= 0 ? "+" : ""}${change.toFixed(2)}%`;
  $("observation-count").textContent = rows.length;
  $("series-note").textContent = `${rows[0].time_period}–${latest.time_period}`;
  const max = Math.max(...rows.map((item) => item.value));
  $("chart").innerHTML = rows.map((item) => `<div class="bar" style="height:${(item.value / max) * 230}px"><b>${item.time_period}</b></div>`).join("");
  const rankingRows = state.catalog.indicators.find((item) => item.indicator_id === state.indicatorId).observations.filter((item) => item.time_period === latest.time_period).sort((a, b) => b.value - a.value);
  $("ranking-title").textContent = `Ranking ${latest.time_period}`;
  $("ranking").innerHTML = rankingRows.map((item) => `<li><span>${state.catalog.geographies.find((geo) => geo.geo_area === item.geo_area).geo_name}</span><strong>${format(item.value)}</strong></li>`).join("");
}

load().catch((error) => { document.querySelector("main").innerHTML += `<p role="alert">No se pudo cargar el fixture: ${error.message}</p>`; });
