from __future__ import annotations

import io

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import streamlit as st
from CoolProp.CoolProp import PropsSI
from matplotlib.lines import Line2D

REFRIGERANT = "R404A"
CYCLE_MODE = "T_evap-T_cond-eta"


def to_kelvin(temperature_value: float, unit: str) -> float:
    return temperature_value if unit == "K" else temperature_value + 273.15


def from_kelvin(temperature_k: float, unit: str) -> float:
    return temperature_k if unit == "K" else temperature_k - 273.15


def to_pascal(pressure_value: float, unit: str) -> float:
    return pressure_value if unit == "Pa" else pressure_value * 1e5


def from_pascal(pressure_pa: float, unit: str) -> float:
    return pressure_pa if unit == "Pa" else pressure_pa / 1e5


def convert_temperature_array_for_display(temperature_k: np.ndarray, unit: str) -> np.ndarray:
    if unit == "K":
        return temperature_k
    return temperature_k - 273.15


def convert_temperature_for_display(temperature_k: float, unit: str) -> float:
    return float(temperature_k if unit == "K" else temperature_k - 273.15)


def figure_to_bytes(figure: plt.Figure, output_format: str, dpi: int) -> bytes:
    buffer = io.BytesIO()
    save_kwargs = {"format": output_format, "bbox_inches": "tight"}
    if output_format.lower() == "png":
        save_kwargs["dpi"] = dpi
    figure.savefig(buffer, **save_kwargs)
    buffer.seek(0)
    return buffer.getvalue()


@st.cache_data(show_spinner=False)
def fluid_limits(fluid: str) -> dict[str, float]:
    t_triple = PropsSI("Ttriple", fluid)
    t_critical = PropsSI("Tcrit", fluid)
    p_critical = PropsSI("Pcrit", fluid)
    p_triple = PropsSI("P", "T", t_triple + 1e-3, "Q", 0, fluid)
    return {
        "Ttriple": t_triple,
        "Tcrit": t_critical,
        "Ptriple": p_triple,
        "Pcrit": p_critical,
    }


@st.cache_data(show_spinner=False)
def saturation_dome(
    fluid: str,
    points: int = 320,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    limits = fluid_limits(fluid)
    pressure_min = max(1.0e4, limits["Ptriple"] * 1.002)
    pressure_max = limits["Pcrit"] * 0.998
    pressure_values = np.linspace(pressure_min, pressure_max, points)

    p_valid = []
    t_liquid = []
    s_liquid = []
    t_vapor = []
    s_vapor = []

    for pressure in pressure_values:
        try:
            t_l = PropsSI("T", "P", float(pressure), "Q", 0, fluid)
            s_l = PropsSI("S", "P", float(pressure), "Q", 0, fluid) / 1000.0
            t_v = PropsSI("T", "P", float(pressure), "Q", 1, fluid)
            s_v = PropsSI("S", "P", float(pressure), "Q", 1, fluid) / 1000.0
        except ValueError:
            continue

        if not (np.isfinite(t_l) and np.isfinite(s_l) and np.isfinite(t_v) and np.isfinite(s_v)):
            continue

        p_valid.append(float(pressure))
        t_liquid.append(float(t_l))
        s_liquid.append(float(s_l))
        t_vapor.append(float(t_v))
        s_vapor.append(float(s_v))

    return (
        np.array(p_valid),
        np.array(t_liquid),
        np.array(s_liquid),
        np.array(t_vapor),
        np.array(s_vapor),
    )


def sidebar_slider_number(
    label: str,
    key: str,
    min_value: float,
    max_value: float,
    default: float,
    step: float,
    number_format: str,
    unit_label: str,
    help_text: str,
) -> float:
    value_key = f"{key}_value"
    slider_key = f"{key}_slider"
    number_key = f"{key}_number"

    if value_key not in st.session_state:
        initial = float(default)
        st.session_state[value_key] = initial
        st.session_state[slider_key] = initial
        st.session_state[number_key] = initial

    def update_from_slider() -> None:
        current = float(st.session_state[slider_key])
        st.session_state[number_key] = current
        st.session_state[value_key] = current

    def update_from_number() -> None:
        current = float(st.session_state[number_key])
        current = max(min_value, min(max_value, current))
        st.session_state[number_key] = current
        st.session_state[slider_key] = current
        st.session_state[value_key] = current

    st.slider(
        f"{label} [{unit_label}] slider",
        min_value=float(min_value),
        max_value=float(max_value),
        step=float(step),
        key=slider_key,
        on_change=update_from_slider,
        help=help_text,
    )
    st.number_input(
        f"{label} [{unit_label}] number",
        min_value=float(min_value),
        max_value=float(max_value),
        step=float(step),
        key=number_key,
        on_change=update_from_number,
        format=number_format,
        help=help_text,
    )

    return float(st.session_state[value_key])


def state_from_pair(
    pair_key_1: str,
    pair_value_1: float,
    pair_key_2: str,
    pair_value_2: float,
    fluid: str,
) -> dict[str, float]:
    state = {
        "T": PropsSI("T", pair_key_1, pair_value_1, pair_key_2, pair_value_2, fluid),
        "P": PropsSI("P", pair_key_1, pair_value_1, pair_key_2, pair_value_2, fluid),
        "H": PropsSI("H", pair_key_1, pair_value_1, pair_key_2, pair_value_2, fluid),
        "S": PropsSI("S", pair_key_1, pair_value_1, pair_key_2, pair_value_2, fluid),
        "D": PropsSI("D", pair_key_1, pair_value_1, pair_key_2, pair_value_2, fluid),
        "U": PropsSI("U", pair_key_1, pair_value_1, pair_key_2, pair_value_2, fluid),
    }

    try:
        state["Q"] = PropsSI("Q", pair_key_1, pair_value_1, pair_key_2, pair_value_2, fluid)
    except ValueError:
        state["Q"] = float("nan")

    return state


def solve_state(
    mode: str,
    temperature_input: float,
    pressure_input: float,
    quality_input: float,
    enthalpy_input_kjkg: float,
    temperature_unit: str,
    pressure_unit: str,
    fluid: str,
) -> dict[str, float]:
    limits = fluid_limits(fluid)
    temperature_k = to_kelvin(temperature_input, temperature_unit)
    pressure_pa = to_pascal(pressure_input, pressure_unit)
    enthalpy_jkg = enthalpy_input_kjkg * 1000.0

    if mode in ("T-P", "T-Q") and temperature_k < limits["Ttriple"]:
        raise ValueError(
            "Out of range: temperature is below the triple-point temperature for R404A."
        )

    if mode == "T-Q" and temperature_k >= limits["Tcrit"]:
        raise ValueError(
            "Out of range: quality is undefined at or above the critical temperature."
        )

    if mode == "T-P":
        return state_from_pair("T", temperature_k, "P", pressure_pa, fluid)

    if mode == "T-Q":
        return state_from_pair("T", temperature_k, "Q", quality_input, fluid)

    return state_from_pair("P", pressure_pa, "H", enthalpy_jkg, fluid)


def saturation_state_from_temperature_with_fallback(
    temperature_k: float,
    quality: float,
    fluid: str,
) -> tuple[dict[str, float], bool]:
    try:
        return state_from_pair("T", temperature_k, "Q", quality, fluid), False
    except ValueError:
        saturation_pressure = PropsSI("P", "T", temperature_k, "Q", quality, fluid)
        return state_from_pair("P", saturation_pressure, "Q", quality, fluid), True


def cycle_states_from_temperatures(
    evaporation_temperature_input: float,
    condensation_temperature_input: float,
    temperature_unit: str,
    isentropic_efficiency: float,
    fluid: str,
) -> dict[str, object]:
    limits = fluid_limits(fluid)
    evaporation_temperature_k = to_kelvin(evaporation_temperature_input, temperature_unit)
    condensation_temperature_k = to_kelvin(condensation_temperature_input, temperature_unit)

    if evaporation_temperature_k < limits["Ttriple"]:
        raise ValueError(
            "Out of range: evaporation temperature is below the triple-point temperature."
        )
    if condensation_temperature_k < limits["Ttriple"]:
        raise ValueError(
            "Out of range: condensation temperature is below the triple-point temperature."
        )
    if evaporation_temperature_k >= limits["Tcrit"]:
        raise ValueError(
            "Out of range: evaporation saturation is undefined at or above critical temperature."
        )
    if condensation_temperature_k >= limits["Tcrit"]:
        raise ValueError(
            "Out of range: condensation saturation is undefined at or above critical temperature."
        )
    if condensation_temperature_k <= evaporation_temperature_k:
        raise ValueError(
            "Invalid cycle inputs: condensation temperature must be higher than evaporation temperature."
        )

    state_1, fallback_1 = saturation_state_from_temperature_with_fallback(
        evaporation_temperature_k,
        1.0,
        fluid,
    )
    state_3, fallback_3 = saturation_state_from_temperature_with_fallback(
        condensation_temperature_k,
        0.0,
        fluid,
    )

    evaporation_pressure_pa = state_1["P"]
    condensation_pressure_pa = state_3["P"]

    if condensation_pressure_pa <= evaporation_pressure_pa:
        raise ValueError(
            "Invalid cycle inputs: condensation pressure must be higher than evaporation pressure."
        )

    h_in = state_1["H"]
    h_isen = PropsSI("H", "P", condensation_pressure_pa, "S", state_1["S"], fluid)
    h_actual = h_in + (h_isen - h_in) / isentropic_efficiency
    state_2 = state_from_pair("P", condensation_pressure_pa, "H", h_actual, fluid)

    # Expansion valve model: isenthalpic throttling h4 = h3 to low-side pressure.
    state_4 = state_from_pair("P", evaporation_pressure_pa, "H", state_3["H"], fluid)

    return {
        "state_1": state_1,
        "state_2": state_2,
        "state_3": state_3,
        "state_4": state_4,
        "cycle_states": {1: state_1, 2: state_2, 3: state_3, 4: state_4},
        "h_in": h_in,
        "h_isen": h_isen,
        "h_actual": h_actual,
        "pressure_low": evaporation_pressure_pa,
        "pressure_high": condensation_pressure_pa,
        "fallback_used": bool(fallback_1 or fallback_3),
    }


def collect_input_warnings(
    mode: str,
    temperature_input: float,
    pressure_input: float,
    temperature_unit: str,
    pressure_unit: str,
    fluid: str,
    evaporation_temperature_input: float | None = None,
    condensation_temperature_input: float | None = None,
) -> list[str]:
    limits = fluid_limits(fluid)
    temperature_k = to_kelvin(temperature_input, temperature_unit)
    pressure_pa = to_pascal(pressure_input, pressure_unit)

    warnings: list[str] = []

    if mode in ("T-P", "T-Q"):
        if temperature_k < limits["Ttriple"]:
            warnings.append("Temperature is below the triple-point range.")
        if temperature_k > limits["Tcrit"]:
            warnings.append("Temperature is above the critical-point range.")

    if mode in ("T-P", "P-H") and pressure_pa < limits["Ptriple"]:
        warnings.append("Pressure is below the approximate triple-point pressure range.")

    if mode == CYCLE_MODE and evaporation_temperature_input is not None:
        evaporation_temperature_k = to_kelvin(evaporation_temperature_input, temperature_unit)
        if evaporation_temperature_k < limits["Ttriple"]:
            warnings.append("Evaporation temperature is below the triple-point range.")
        if evaporation_temperature_k >= limits["Tcrit"]:
            warnings.append(
                "Evaporation temperature is at/above critical temperature; saturated vapor is undefined."
            )

    if mode == CYCLE_MODE and condensation_temperature_input is not None:
        condensation_temperature_k = to_kelvin(condensation_temperature_input, temperature_unit)
        if condensation_temperature_k < limits["Ttriple"]:
            warnings.append("Condensation temperature is below the triple-point range.")
        if condensation_temperature_k >= limits["Tcrit"]:
            warnings.append(
                "Condensation temperature is at/above critical temperature; saturation pressure is undefined."
            )

    if (
        mode == CYCLE_MODE
        and evaporation_temperature_input is not None
        and condensation_temperature_input is not None
    ):
        evaporation_temperature_k = to_kelvin(evaporation_temperature_input, temperature_unit)
        condensation_temperature_k = to_kelvin(condensation_temperature_input, temperature_unit)
        if condensation_temperature_k <= evaporation_temperature_k:
            warnings.append("Condensation temperature should be higher than evaporation temperature.")

    return warnings


def make_ts_figure(
    fluid: str,
    current_state: dict[str, float] | None,
    temperature_unit: str,
    outlet_state: dict[str, float] | None,
) -> go.Figure:
    _, t_liq, s_liq, t_vap, s_vap = saturation_dome(fluid)
    t_liq_display = np.array([from_kelvin(t, temperature_unit) for t in t_liq])
    t_vap_display = np.array([from_kelvin(t, temperature_unit) for t in t_vap])

    figure = go.Figure()
    figure.add_trace(
        go.Scatter(
            x=s_liq,
            y=t_liq_display,
            mode="lines",
            name="Bubble line (Q=0)",
            line={"width": 2, "color": "#1f77b4"},
        )
    )
    figure.add_trace(
        go.Scatter(
            x=s_vap,
            y=t_vap_display,
            mode="lines",
            name="Dew line (Q=1)",
            line={"width": 2, "color": "#2ca02c"},
        )
    )

    if outlet_state is not None:
        figure.add_trace(
            go.Scatter(
                x=[outlet_state["S"] / 1000.0],
                y=[from_kelvin(outlet_state["T"], temperature_unit)],
                mode="markers",
                name="Outlet state (actual)",
                marker={"size": 10, "color": "#ff7f0e", "symbol": "diamond"},
            )
        )

    if current_state is not None:
        figure.add_trace(
            go.Scatter(
                x=[current_state["S"] / 1000.0],
                y=[from_kelvin(current_state["T"], temperature_unit)],
                mode="markers",
                name="Current state",
                marker={"size": 12, "color": "red"},
            )
        )

    figure.update_layout(
        title=f"T-s Diagram for {fluid}",
        xaxis_title="Entropy [kJ/kg-K]",
        yaxis_title=f"Temperature [{temperature_unit}]",
        margin={"l": 10, "r": 10, "t": 45, "b": 10},
        legend={"orientation": "h", "y": 1.03, "x": 0.01},
    )

    return figure


@st.cache_data(show_spinner=False)
def static_ts_isoline_data(fluid: str, temperature_unit: str) -> dict[str, object]:
    limits = fluid_limits(fluid)
    dome_pressure, t_liq, s_liq, t_vap, s_vap = saturation_dome(fluid, points=500)
    t_liq_display = convert_temperature_array_for_display(t_liq, temperature_unit)
    t_vap_display = convert_temperature_array_for_display(t_vap, temperature_unit)

    s_axis_min = max(0.6, float(min(np.nanmin(s_liq), np.nanmin(s_vap))) - 0.08)
    s_axis_max = float(max(np.nanmax(s_liq), np.nanmax(s_vap))) + 0.40
    s_grid_kj = np.linspace(s_axis_min, s_axis_max, 560)
    s_grid_j = s_grid_kj * 1000.0

    t_axis_min = convert_temperature_for_display(limits["Ttriple"] - 15.0, temperature_unit)
    t_axis_max = convert_temperature_for_display(limits["Tcrit"] + 90.0, temperature_unit)

    def local_relative_error(computed_value: float, reference_value: float) -> float:
        denominator = abs(reference_value)
        if denominator < 1e-14:
            return abs(computed_value - reference_value)
        return abs(computed_value - reference_value) / denominator

    def build_single_phase_isoline(property_key: str, property_value: float) -> dict[str, np.ndarray] | None:
        temperature_values_k = np.full_like(s_grid_j, np.nan, dtype=float)
        for index, entropy_value in enumerate(s_grid_j):
            try:
                computed_temperature = PropsSI(
                    "T", property_key, property_value, "S", float(entropy_value), fluid
                )
            except ValueError:
                continue

            if not np.isfinite(computed_temperature):
                continue

            try:
                verification_value = PropsSI(
                    property_key,
                    "T",
                    float(computed_temperature),
                    "S",
                    float(entropy_value),
                    fluid,
                )
            except ValueError:
                continue

            if not np.isfinite(verification_value):
                continue

            if local_relative_error(float(verification_value), float(property_value)) > 3.0e-3:
                continue

            temperature_values_k[index] = computed_temperature

        valid = np.isfinite(temperature_values_k)
        if np.count_nonzero(valid) < 12:
            return None

        return {
            "s": s_grid_kj[valid],
            "t": convert_temperature_array_for_display(temperature_values_k[valid], temperature_unit),
        }

    isobars: list[dict[str, object]] = []
    pressure_candidates_bar = [
        1.0,
        1.5,
        2.0,
        3.0,
        4.0,
        5.0,
        6.0,
        8.0,
        10.0,
        12.0,
        15.0,
        20.0,
        25.0,
        30.0,
        35.0,
        40.0,
    ]
    min_bar = limits["Ptriple"] / 1e5 * 1.02
    max_bar = max(12.0, min(40.0, limits["Pcrit"] / 1e5 * 2.2))
    for pressure_bar in pressure_candidates_bar:
        if not (min_bar <= pressure_bar <= max_bar):
            continue
        curve = build_single_phase_isoline("P", pressure_bar * 1e5)
        if curve is None:
            continue
        isobars.append({"label": f"{pressure_bar:g}", "s": curve["s"], "t": curve["t"]})

    isenthalps: list[dict[str, object]] = []
    enthalpy_candidates_kjkg = [
        280.0,
        300.0,
        320.0,
        340.0,
        360.0,
        380.0,
        400.0,
        420.0,
        440.0,
        460.0,
        480.0,
        500.0,
    ]
    for enthalpy_kjkg in enthalpy_candidates_kjkg:
        curve = build_single_phase_isoline("H", enthalpy_kjkg * 1000.0)
        if curve is None:
            continue
        isenthalps.append({"label": f"{enthalpy_kjkg:.0f}", "s": curve["s"], "t": curve["t"]})

    isochores: list[dict[str, object]] = []
    specific_volume_candidates = [0.005, 0.0075, 0.01, 0.015, 0.02, 0.03, 0.05, 0.08, 0.10]
    for specific_volume in specific_volume_candidates:
        density_value = 1.0 / specific_volume
        curve = build_single_phase_isoline("D", density_value)
        if curve is None:
            continue
        isochores.append({"label": f"{specific_volume:g}", "s": curve["s"], "t": curve["t"]})

    quality_lines: list[dict[str, object]] = []
    pressure_grid = np.linspace(max(1.0e4, limits["Ptriple"] * 1.002), limits["Pcrit"] * 0.998, 420)
    quality_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for quality_value in quality_values:
        entropy_points = []
        temperature_points = []
        pressure_points = []
        for saturation_pressure in pressure_grid:
            try:
                saturation_temperature = PropsSI(
                    "T", "P", float(saturation_pressure), "Q", quality_value, fluid
                )
                entropy_value = PropsSI(
                    "S", "P", float(saturation_pressure), "Q", quality_value, fluid
                ) / 1000.0
            except ValueError:
                continue
            if np.isfinite(entropy_value) and np.isfinite(saturation_temperature):
                entropy_points.append(float(entropy_value))
                temperature_points.append(
                    convert_temperature_for_display(float(saturation_temperature), temperature_unit)
                )
                pressure_points.append(float(saturation_pressure))

        if len(entropy_points) < 12:
            continue
        quality_lines.append(
            {
                "label": f"{quality_value:.1f}",
                "s": np.array(entropy_points),
                "t": np.array(temperature_points),
                "p": np.array(pressure_points),
            }
        )

    return {
        "dome_p": dome_pressure,
        "dome_t_liq": t_liq_display,
        "dome_t_vap": t_vap_display,
        "dome_liq_s": s_liq,
        "dome_vap_s": s_vap,
        "isobars": isobars,
        "isenthalps": isenthalps,
        "isochores": isochores,
        "quality_lines": quality_lines,
        "s_axis_min": s_axis_min,
        "s_axis_max": s_axis_max,
        "t_axis_min": t_axis_min,
        "t_axis_max": t_axis_max,
    }


def annotate_isoline(
    axis,
    entropy_values: np.ndarray,
    temperature_values: np.ndarray,
    label: str,
    color: str,
    label_position: float,
) -> None:
    if len(entropy_values) < 12 or len(temperature_values) < 12:
        return

    index = int((len(entropy_values) - 1) * label_position)
    index = max(1, min(len(entropy_values) - 2, index))

    x0 = float(entropy_values[index - 1])
    y0 = float(temperature_values[index - 1])
    x1 = float(entropy_values[index + 1])
    y1 = float(temperature_values[index + 1])
    rotation = np.degrees(np.arctan2(y1 - y0, x1 - x0)) if abs(x1 - x0) > 1e-12 else 90.0
    rotation = max(-65.0, min(65.0, rotation))

    axis.text(
        float(entropy_values[index]),
        float(temperature_values[index]),
        label,
        color=color,
        fontsize=8,
        rotation=rotation,
        ha="left",
        va="bottom",
        clip_on=True,
    )


def make_ts_figure_static(
    fluid: str,
    current_state: dict[str, float] | None,
    temperature_unit: str,
    pressure_unit: str,
    outlet_state: dict[str, float] | None,
    figure_width: float,
    figure_height: float,
    figure_dpi: int,
    cycle_states: dict[int, dict[str, float]] | None = None,
) -> plt.Figure:
    data = static_ts_isoline_data(fluid, temperature_unit)
    figure, axis = plt.subplots(figsize=(figure_width, figure_height), dpi=figure_dpi)

    figure.patch.set_facecolor("#e7e7e7")
    axis.set_facecolor("#f5f5f5")
    axis.grid(which="major", linestyle=(0, (4, 4)), linewidth=0.8, color="#5f5f5f", alpha=0.75)
    axis.grid(which="minor", linestyle=(0, (2, 4)), linewidth=0.5, color="#7a7a7a", alpha=0.35)
    axis.minorticks_on()

    for curve in data["isobars"]:
        entropy_values = np.asarray(curve["s"])
        temperature_values = np.asarray(curve["t"])
        axis.plot(entropy_values, temperature_values, color="#2f43b8", linewidth=1.0)
        annotate_isoline(
            axis,
            entropy_values,
            temperature_values,
            str(curve["label"]),
            "#2f43b8",
            label_position=0.90,
        )

    for curve in data["isenthalps"]:
        entropy_values = np.asarray(curve["s"])
        temperature_values = np.asarray(curve["t"])
        axis.plot(entropy_values, temperature_values, color="#228b22", linewidth=1.0)
        annotate_isoline(
            axis,
            entropy_values,
            temperature_values,
            str(curve["label"]),
            "#228b22",
            label_position=0.84,
        )

    for curve in data["isochores"]:
        entropy_values = np.asarray(curve["s"])
        temperature_values = np.asarray(curve["t"])
        axis.plot(entropy_values, temperature_values, color="#d62728", linewidth=0.9, alpha=0.85)

    for curve in data["quality_lines"]:
        entropy_values = np.asarray(curve["s"])
        temperature_values = np.asarray(curve["t"])
        axis.plot(
            entropy_values,
            temperature_values,
            color="#4f4f4f",
            linewidth=0.8,
            linestyle=(0, (4, 4)),
        )
        annotate_isoline(
            axis,
            entropy_values,
            temperature_values,
            str(curve["label"]),
            "#3f3f3f",
            label_position=0.55,
        )

    axis.plot(np.asarray(data["dome_liq_s"]), np.asarray(data["dome_t_liq"]), color="black", linewidth=1.8)
    axis.plot(np.asarray(data["dome_vap_s"]), np.asarray(data["dome_t_vap"]), color="black", linewidth=1.8)

    if cycle_states is None and outlet_state is not None:
        axis.scatter(
            [outlet_state["S"] / 1000.0],
            [convert_temperature_for_display(outlet_state["T"], temperature_unit)],
            s=52,
            color="#ff7f0e",
            marker="D",
            zorder=7,
        )

    if cycle_states is None and current_state is not None:
        axis.scatter(
            [current_state["S"] / 1000.0],
            [convert_temperature_for_display(current_state["T"], temperature_unit)],
            s=58,
            color="red",
            marker="o",
            zorder=8,
        )

    if cycle_states is not None:
        cycle_order = [1, 2, 3, 4, 1]
        segment_colors = ["#b10000", "#b10000", "#b10000", "#2f6db2"]

        for segment_index in range(4):
            state_start = cycle_states[cycle_order[segment_index]]
            state_end = cycle_states[cycle_order[segment_index + 1]]

            x_start = state_start["S"] / 1000.0
            y_start = convert_temperature_for_display(state_start["T"], temperature_unit)
            x_end = state_end["S"] / 1000.0
            y_end = convert_temperature_for_display(state_end["T"], temperature_unit)

            axis.plot(
                [x_start, x_end],
                [y_start, y_end],
                color=segment_colors[segment_index],
                linewidth=1.8,
                zorder=7,
            )

            arrow_from_x = x_start + 0.55 * (x_end - x_start)
            arrow_from_y = y_start + 0.55 * (y_end - y_start)
            arrow_to_x = x_start + 0.78 * (x_end - x_start)
            arrow_to_y = y_start + 0.78 * (y_end - y_start)
            axis.annotate(
                "",
                xy=(arrow_to_x, arrow_to_y),
                xytext=(arrow_from_x, arrow_from_y),
                arrowprops={"arrowstyle": "->", "lw": 1.4, "color": segment_colors[segment_index]},
                zorder=8,
            )

        label_offsets = {
            1: (6, 12),
            2: (10, 12),
            3: (10, -52),
            4: (-94, -48),
        }

        for state_id in (1, 2, 3, 4):
            state_data = cycle_states[state_id]
            state_x = state_data["S"] / 1000.0
            state_y = convert_temperature_for_display(state_data["T"], temperature_unit)

            axis.scatter(
                [state_x],
                [state_y],
                s=64,
                color="#f8f2bf",
                edgecolors="#1d1d1d",
                linewidths=0.9,
                zorder=9,
            )

            label_text = (
                f"State {state_id}"
                f"\nh={state_data['H'] / 1000.0:.1f} kJ/kg"
                f"\nT={state_y:.2f} {temperature_unit}"
                f"\nP={from_pascal(state_data['P'], pressure_unit):.3f} {pressure_unit}"
            )
            offset_x, offset_y = label_offsets[state_id]
            axis.annotate(
                label_text,
                (state_x, state_y),
                xytext=(offset_x, offset_y),
                textcoords="offset points",
                fontsize=8,
                ha="left",
                va="bottom",
                bbox={"boxstyle": "round,pad=0.2", "facecolor": "white", "edgecolor": "#9c9c9c", "alpha": 0.86},
                zorder=10,
            )

    axis.set_xlim(float(data["s_axis_min"]), float(data["s_axis_max"]))
    axis.set_ylim(float(data["t_axis_min"]), float(data["t_axis_max"]))
    axis.set_xlabel("Entropy (kJ/(kg K))", fontweight="bold")
    axis.set_ylabel(f"Temperature ({temperature_unit})", fontweight="bold")
    axis.set_title(
        f"Refrigerant Temperature-Entropy(T-s) Diagram - {fluid}",
        fontweight="bold",
        pad=14,
    )

    legend_handles = [
        Line2D([0], [0], color="#2f43b8", linewidth=1.2, label="Isobar, bar"),
        Line2D([0], [0], color="#228b22", linewidth=1.2, label="Isenthalp, kJ/kg"),
        Line2D([0], [0], color="#4f4f4f", linewidth=1.2, linestyle=(0, (4, 4)), label="Quality"),
        Line2D([0], [0], color="#d62728", linewidth=1.2, label="Isochor, m3/kg"),
    ]
    if cycle_states is None and current_state is not None:
        legend_handles.append(
            Line2D([0], [0], marker="o", color="none", markerfacecolor="red", markersize=7, label="Current state")
        )
    if cycle_states is None and outlet_state is not None:
        legend_handles.append(
            Line2D(
                [0],
                [0],
                marker="D",
                color="none",
                markerfacecolor="#ff7f0e",
                markersize=7,
                label="Outlet state",
            )
        )
    if cycle_states is not None:
        legend_handles.append(
            Line2D([0], [0], color="#b10000", linewidth=1.8, label="Cycle path 1-2-3-4")
        )

    axis.legend(
        handles=legend_handles,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.12),
        frameon=False,
        ncol=3,
        fontsize=9,
        handlelength=3.2,
    )

    figure.tight_layout()
    return figure


def relative_error(computed_value: float, reference_value: float) -> float:
    denominator = abs(reference_value)
    if denominator < 1e-14:
        return abs(computed_value - reference_value)
    return abs(computed_value - reference_value) / denominator


def summarize_errors(error_values: list[float], failed_count: int) -> dict[str, float | int]:
    if not error_values:
        return {
            "n": 0,
            "mean": float("nan"),
            "p95": float("nan"),
            "max": float("nan"),
            "failed": int(failed_count),
        }

    error_array = np.asarray(error_values, dtype=float)
    error_array = error_array[np.isfinite(error_array)]

    if error_array.size == 0:
        return {
            "n": 0,
            "mean": float("nan"),
            "p95": float("nan"),
            "max": float("nan"),
            "failed": int(failed_count),
        }

    return {
        "n": int(error_array.size),
        "mean": float(np.mean(error_array)),
        "p95": float(np.percentile(error_array, 95)),
        "max": float(np.max(error_array)),
        "failed": int(failed_count),
    }


def format_scientific(value: float) -> str:
    if not np.isfinite(value):
        return "nan"
    return f"{value:.3e}"


@st.cache_data(show_spinner=False)
def static_ts_accuracy_audit(
    fluid: str,
    temperature_unit: str,
    sample_stride: int = 1,
) -> dict[str, object]:
    sample_stride = max(1, int(sample_stride))
    data = static_ts_isoline_data(fluid, temperature_unit)

    thresholds = {
        "Isobars (P relative)": 5.0e-3,
        "Isenthalps (h relative)": 5.0e-3,
        "Isochores (D relative)": 1.0e-2,
        "Quality lines (Q absolute)": 5.0e-3,
        "Dome liquid (s absolute kJ/kg-K)": 1.0e-3,
        "Dome vapor (s absolute kJ/kg-K)": 1.0e-3,
    }

    isobar_errors: list[float] = []
    isobar_failed = 0
    for curve in data["isobars"]:
        target_pressure_pa = float(curve["label"]) * 1e5
        entropy_values = np.asarray(curve["s"], dtype=float)[::sample_stride]
        temperature_values = np.asarray(curve["t"], dtype=float)[::sample_stride]
        for entropy_kjkgk, temperature_display in zip(entropy_values, temperature_values):
            try:
                computed_pressure_pa = PropsSI(
                    "P",
                    "T",
                    to_kelvin(float(temperature_display), temperature_unit),
                    "S",
                    float(entropy_kjkgk) * 1000.0,
                    fluid,
                )
            except ValueError:
                isobar_failed += 1
                continue
            if not np.isfinite(computed_pressure_pa):
                isobar_failed += 1
                continue
            isobar_errors.append(relative_error(computed_pressure_pa, target_pressure_pa))

    isenthalp_errors: list[float] = []
    isenthalp_failed = 0
    for curve in data["isenthalps"]:
        target_enthalpy_jkg = float(curve["label"]) * 1000.0
        entropy_values = np.asarray(curve["s"], dtype=float)[::sample_stride]
        temperature_values = np.asarray(curve["t"], dtype=float)[::sample_stride]
        for entropy_kjkgk, temperature_display in zip(entropy_values, temperature_values):
            try:
                computed_enthalpy_jkg = PropsSI(
                    "H",
                    "T",
                    to_kelvin(float(temperature_display), temperature_unit),
                    "S",
                    float(entropy_kjkgk) * 1000.0,
                    fluid,
                )
            except ValueError:
                isenthalp_failed += 1
                continue
            if not np.isfinite(computed_enthalpy_jkg):
                isenthalp_failed += 1
                continue
            isenthalp_errors.append(relative_error(computed_enthalpy_jkg, target_enthalpy_jkg))

    isochore_errors: list[float] = []
    isochore_failed = 0
    for curve in data["isochores"]:
        target_specific_volume = float(curve["label"])
        target_density = 1.0 / target_specific_volume
        entropy_values = np.asarray(curve["s"], dtype=float)[::sample_stride]
        temperature_values = np.asarray(curve["t"], dtype=float)[::sample_stride]
        for entropy_kjkgk, temperature_display in zip(entropy_values, temperature_values):
            try:
                computed_density = PropsSI(
                    "D",
                    "T",
                    to_kelvin(float(temperature_display), temperature_unit),
                    "S",
                    float(entropy_kjkgk) * 1000.0,
                    fluid,
                )
            except ValueError:
                isochore_failed += 1
                continue
            if not np.isfinite(computed_density):
                isochore_failed += 1
                continue
            isochore_errors.append(relative_error(computed_density, target_density))

    quality_errors: list[float] = []
    quality_failed = 0
    for curve in data["quality_lines"]:
        target_quality = float(curve["label"])
        entropy_values = np.asarray(curve["s"], dtype=float)[::sample_stride]
        temperature_values = np.asarray(curve["t"], dtype=float)[::sample_stride]
        pressure_values = np.asarray(curve.get("p", []), dtype=float)[::sample_stride]

        if pressure_values.size == entropy_values.size:
            iterator = zip(entropy_values, pressure_values)
            for entropy_kjkgk, pressure_value in iterator:
                try:
                    computed_quality = PropsSI(
                        "Q",
                        "P",
                        float(pressure_value),
                        "S",
                        float(entropy_kjkgk) * 1000.0,
                        fluid,
                    )
                except ValueError:
                    quality_failed += 1
                    continue
                if not np.isfinite(computed_quality):
                    quality_failed += 1
                    continue
                quality_errors.append(abs(computed_quality - target_quality))
        else:
            for entropy_kjkgk, temperature_display in zip(entropy_values, temperature_values):
                try:
                    computed_quality = PropsSI(
                        "Q",
                        "T",
                        to_kelvin(float(temperature_display), temperature_unit),
                        "S",
                        float(entropy_kjkgk) * 1000.0,
                        fluid,
                    )
                except ValueError:
                    quality_failed += 1
                    continue
                if not np.isfinite(computed_quality):
                    quality_failed += 1
                    continue
                quality_errors.append(abs(computed_quality - target_quality))

    dome_liquid_errors: list[float] = []
    dome_liquid_failed = 0
    dome_vapor_errors: list[float] = []
    dome_vapor_failed = 0
    dome_pressures = np.asarray(data["dome_p"], dtype=float)[::sample_stride]
    dome_liquid = np.asarray(data["dome_liq_s"], dtype=float)[::sample_stride]
    dome_vapor = np.asarray(data["dome_vap_s"], dtype=float)[::sample_stride]
    for pressure_value, entropy_liquid, entropy_vapor in zip(dome_pressures, dome_liquid, dome_vapor):
        try:
            reference_liquid = PropsSI("S", "P", float(pressure_value), "Q", 0, fluid) / 1000.0
            dome_liquid_errors.append(abs(float(entropy_liquid) - reference_liquid))
        except ValueError:
            dome_liquid_failed += 1

        try:
            reference_vapor = PropsSI("S", "P", float(pressure_value), "Q", 1, fluid) / 1000.0
            dome_vapor_errors.append(abs(float(entropy_vapor) - reference_vapor))
        except ValueError:
            dome_vapor_failed += 1

    stats_map = {
        "Isobars (P relative)": summarize_errors(isobar_errors, isobar_failed),
        "Isenthalps (h relative)": summarize_errors(isenthalp_errors, isenthalp_failed),
        "Isochores (D relative)": summarize_errors(isochore_errors, isochore_failed),
        "Quality lines (Q absolute)": summarize_errors(quality_errors, quality_failed),
        "Dome liquid (s absolute kJ/kg-K)": summarize_errors(dome_liquid_errors, dome_liquid_failed),
        "Dome vapor (s absolute kJ/kg-K)": summarize_errors(dome_vapor_errors, dome_vapor_failed),
    }

    rows = []
    for family_name, threshold_value in thresholds.items():
        family_stats = stats_map[family_name]
        pass_flag = (
            family_stats["n"] > 0
            and family_stats["failed"] == 0
            and np.isfinite(family_stats["p95"])
            and family_stats["p95"] <= threshold_value
        )
        rows.append(
            {
                "family": family_name,
                "n": int(family_stats["n"]),
                "mean": float(family_stats["mean"]),
                "p95": float(family_stats["p95"]),
                "max": float(family_stats["max"]),
                "failed": int(family_stats["failed"]),
                "threshold_p95": float(threshold_value),
                "pass": bool(pass_flag),
            }
        )

    overall_pass = all(row["pass"] for row in rows)
    return {
        "rows": rows,
        "overall_pass": overall_pass,
        "unit": temperature_unit,
        "sample_stride": sample_stride,
    }


def validation_rows(fluid: str) -> tuple[list[dict[str, str]], float]:
    reference_tq = state_from_pair("T", 273.15, "Q", 1.0, fluid)
    reference_ph = state_from_pair("P", reference_tq["P"], "H", reference_tq["H"], fluid)

    rows: list[dict[str, str]] = []
    spec = [
        ("T", "T [K]", 1.0),
        ("P", "P [Pa]", 1.0),
        ("H", "h [kJ/kg]", 1.0 / 1000.0),
        ("S", "s [kJ/kg-K]", 1.0 / 1000.0),
        ("D", "D [kg/m^3]", 1.0),
        ("U", "u [kJ/kg]", 1.0 / 1000.0),
    ]

    for key, label, scale in spec:
        ref_value = reference_tq[key] * scale
        back_value = reference_ph[key] * scale
        absolute_error = abs(back_value - ref_value)
        rows.append(
            {
                "Property": label,
                "Reference (T-Q)": f"{ref_value:.6f}",
                "Back-calculated (P-H)": f"{back_value:.6f}",
                "Absolute error": f"{absolute_error:.3e}",
            }
        )

    max_abs_error = max(
        abs(reference_ph["T"] - reference_tq["T"]),
        abs(reference_ph["H"] - reference_tq["H"]),
        abs(reference_ph["S"] - reference_tq["S"]),
    )

    return rows, max_abs_error


def main() -> None:
    st.set_page_config(page_title="R404A T-s Tool", layout="wide")
    st.title("Interactive T-s Diagram and Enthalpy Calculator")
    st.caption(
        "Streamlit dashboard using CoolProp.PropsSI for refrigerant R404A state calculations."
    )

    limits = fluid_limits(REFRIGERANT)

    with st.sidebar:
        st.header("State Inputs")
        mode = st.radio("Input pair", ("T-P", "T-Q", "P-H", CYCLE_MODE), index=0)
        temperature_unit = st.selectbox("Temperature unit", ("C", "K"), index=0)
        pressure_unit = st.selectbox("Pressure unit", ("bar", "Pa"), index=0)
        diagram_mode = st.radio(
            "Diagram rendering",
            ("Static (High accuracy)", "Interactive (Plotly)"),
            index=0,
        )

        static_figure_width = 10.8
        static_figure_height = 7.4
        static_figure_dpi = 170
        if diagram_mode == "Static (High accuracy)":
            with st.expander("Static image settings", expanded=False):
                static_figure_width = st.number_input(
                    "Figure width [inch]",
                    min_value=6.0,
                    max_value=18.0,
                    value=static_figure_width,
                    step=0.2,
                    format="%.1f",
                )
                static_figure_height = st.number_input(
                    "Figure height [inch]",
                    min_value=4.0,
                    max_value=14.0,
                    value=static_figure_height,
                    step=0.2,
                    format="%.1f",
                )
                static_figure_dpi = int(
                    st.number_input(
                        "Export DPI",
                        min_value=96,
                        max_value=600,
                        value=static_figure_dpi,
                        step=10,
                    )
                )

        temperature_min = from_kelvin(limits["Ttriple"] - 30.0, temperature_unit)
        temperature_max = from_kelvin(limits["Tcrit"] + 30.0, temperature_unit)
        temperature_default = 0.0 if temperature_unit == "C" else 273.15
        temperature_step = 0.2

        pressure_min = from_pascal(max(1.0e4, limits["Ptriple"] * 0.5), pressure_unit)
        pressure_max = from_pascal(limits["Pcrit"] * 1.5, pressure_unit)
        pressure_default = from_pascal(
            min(max(8.0e5, limits["Ptriple"] * 2.0), limits["Pcrit"]), pressure_unit
        )
        pressure_step = 0.05 if pressure_unit == "bar" else 1000.0
        pressure_format = "%.3f" if pressure_unit == "bar" else "%.0f"

        evaporation_temperature_value: float | None = None
        condensation_temperature_value: float | None = None
        mass_flow_kg_min = 0.6
        temperature_value = temperature_default
        pressure_value = pressure_default
        quality_value = 0.5
        enthalpy_input = 300.0
        outlet_pressure_value = pressure_default

        efficiency_value = sidebar_slider_number(
            label="Isentropic efficiency",
            key="eta_is",
            min_value=0.1,
            max_value=1.0,
            default=0.8,
            step=0.01,
            number_format="%.3f",
            unit_label="-",
            help_text="Used in h_actual computation.",
        )

        if mode == CYCLE_MODE:
            evaporation_temperature_value = sidebar_slider_number(
                label="Evaporation temperature",
                key="evap_temperature",
                min_value=temperature_min,
                max_value=temperature_max,
                default=-10.0 if temperature_unit == "C" else 263.15,
                step=temperature_step,
                number_format="%.3f",
                unit_label=temperature_unit,
                help_text="Compressor inlet (evaporator outlet) is assumed saturated vapor at this temperature.",
            )
            condensation_temperature_value = sidebar_slider_number(
                label="Condensation temperature",
                key="cond_temperature",
                min_value=temperature_min,
                max_value=temperature_max,
                default=25.0 if temperature_unit == "C" else 298.15,
                step=temperature_step,
                number_format="%.3f",
                unit_label=temperature_unit,
                help_text="Condenser saturation pressure is taken from this temperature.",
            )
            mass_flow_kg_min = sidebar_slider_number(
                label="Mass flow",
                key="mass_flow",
                min_value=0.05,
                max_value=10.0,
                default=0.6,
                step=0.05,
                number_format="%.3f",
                unit_label="kg/min",
                help_text="Used for Qin, Qout, Win and COP rate calculations.",
            )
            st.caption(
                "Cycle assumptions: State 1 saturated vapor, State 3 saturated liquid, and valve is isenthalpic (h4=h3)."
            )
        else:
            temperature_value = sidebar_slider_number(
                label="Temperature",
                key="temperature",
                min_value=temperature_min,
                max_value=temperature_max,
                default=temperature_default,
                step=temperature_step,
                number_format="%.3f",
                unit_label=temperature_unit,
                help_text="Used in T-P and T-Q modes.",
            )
            pressure_value = sidebar_slider_number(
                label="Pressure",
                key="pressure",
                min_value=pressure_min,
                max_value=pressure_max,
                default=pressure_default,
                step=pressure_step,
                number_format=pressure_format,
                unit_label=pressure_unit,
                help_text="Used in T-P and P-H modes.",
            )
            quality_value = sidebar_slider_number(
                label="Quality",
                key="quality",
                min_value=0.0,
                max_value=1.0,
                default=0.5,
                step=0.01,
                number_format="%.3f",
                unit_label="-",
                help_text="Used in T-Q mode.",
            )
            enthalpy_input = sidebar_slider_number(
                label="Enthalpy (for P-H)",
                key="enthalpy",
                min_value=100.0,
                max_value=650.0,
                default=300.0,
                step=1.0,
                number_format="%.3f",
                unit_label="kJ/kg",
                help_text="Used only in P-H mode.",
            )
            outlet_pressure_value = sidebar_slider_number(
                label="Outlet pressure (for eta calc)",
                key="outlet_pressure",
                min_value=pressure_min,
                max_value=pressure_max,
                default=min(pressure_max, max(pressure_min, pressure_default * 1.4)),
                step=pressure_step,
                number_format=pressure_format,
                unit_label=pressure_unit,
                help_text="Target outlet pressure for isentropic/actual enthalpy estimate.",
            )

        st.markdown("---")
        st.caption(
            (
                "R404A limits: "
                f"T_triple={from_kelvin(limits['Ttriple'], temperature_unit):.2f} {temperature_unit}, "
                f"T_critical={from_kelvin(limits['Tcrit'], temperature_unit):.2f} {temperature_unit}"
            )
        )

    warnings = collect_input_warnings(
        mode=mode,
        temperature_input=temperature_value,
        pressure_input=pressure_value,
        temperature_unit=temperature_unit,
        pressure_unit=pressure_unit,
        fluid=REFRIGERANT,
        evaporation_temperature_input=evaporation_temperature_value,
        condensation_temperature_input=condensation_temperature_value,
    )
    for warning_text in warnings:
        st.warning(f"Out of range warning: {warning_text}")

    state: dict[str, float] | None = None
    state_error: str | None = None
    outlet_state: dict[str, float] | None = None
    h_in = None
    h_isen = None
    h_actual = None
    cycle_states: dict[int, dict[str, float]] | None = None
    cycle_fallback_used = False
    outlet_pressure_pa: float | None = None
    pressure_low_pa: float | None = None

    if mode == CYCLE_MODE:
        try:
            if evaporation_temperature_value is None or condensation_temperature_value is None:
                raise ValueError("Cycle inputs are not initialized.")
            cycle_report = cycle_states_from_temperatures(
                evaporation_temperature_input=evaporation_temperature_value,
                condensation_temperature_input=condensation_temperature_value,
                temperature_unit=temperature_unit,
                isentropic_efficiency=efficiency_value,
                fluid=REFRIGERANT,
            )
            state = cycle_report["state_1"]
            outlet_state = cycle_report["state_2"]
            cycle_states = cycle_report["cycle_states"]
            h_in = float(cycle_report["h_in"])
            h_isen = float(cycle_report["h_isen"])
            h_actual = float(cycle_report["h_actual"])
            pressure_low_pa = float(cycle_report["pressure_low"])
            outlet_pressure_pa = float(cycle_report["pressure_high"])
            cycle_fallback_used = bool(cycle_report["fallback_used"])
        except ValueError as exc:
            state_error = str(exc)
    else:
        try:
            state = solve_state(
                mode=mode,
                temperature_input=temperature_value,
                pressure_input=pressure_value,
                quality_input=quality_value,
                enthalpy_input_kjkg=enthalpy_input,
                temperature_unit=temperature_unit,
                pressure_unit=pressure_unit,
                fluid=REFRIGERANT,
            )
        except ValueError as exc:
            state_error = str(exc)

        if state is not None:
            outlet_pressure_pa = to_pascal(outlet_pressure_value, pressure_unit)
            try:
                h_in = state["H"]
                h_isen = PropsSI("H", "P", outlet_pressure_pa, "S", state["S"], REFRIGERANT)
                h_actual = h_in + (h_isen - h_in) / efficiency_value
                outlet_state = state_from_pair("P", outlet_pressure_pa, "H", h_actual, REFRIGERANT)
            except ValueError as exc:
                st.warning(f"Isentropic outlet calculation issue: {exc}")

    if mode == CYCLE_MODE and cycle_fallback_used:
        st.info(
            "Cycle saturation fallback engaged: simplified T-Q evaluation failed at least once, "
            "so pressure-based saturation evaluation was applied automatically."
        )

    if diagram_mode == "Static (High accuracy)":
        static_figure = make_ts_figure_static(
            fluid=REFRIGERANT,
            current_state=state,
            temperature_unit=temperature_unit,
            pressure_unit=pressure_unit,
            outlet_state=outlet_state,
            figure_width=static_figure_width,
            figure_height=static_figure_height,
            figure_dpi=static_figure_dpi,
            cycle_states=cycle_states if mode == CYCLE_MODE else None,
        )
        st.pyplot(static_figure, use_container_width=True)

        png_bytes = figure_to_bytes(static_figure, "png", static_figure_dpi)
        svg_bytes = figure_to_bytes(static_figure, "svg", static_figure_dpi)
        export_columns = st.columns(2)
        export_columns[0].download_button(
            "Download diagram PNG",
            data=png_bytes,
            file_name="r404a_ts_diagram.png",
            mime="image/png",
            use_container_width=True,
        )
        export_columns[1].download_button(
            "Download diagram SVG",
            data=svg_bytes,
            file_name="r404a_ts_diagram.svg",
            mime="image/svg+xml",
            use_container_width=True,
        )
        plt.close(static_figure)
    else:
        ts_figure = make_ts_figure(
            fluid=REFRIGERANT,
            current_state=state,
            temperature_unit=temperature_unit,
            outlet_state=outlet_state,
        )
        st.plotly_chart(ts_figure, use_container_width=True)

    if state_error is not None:
        st.error(state_error)
    elif state is not None:
        st.subheader("Calculated Thermodynamic Properties")
        prop_columns = st.columns(4)
        prop_columns[0].metric("Enthalpy h [kJ/kg]", f"{state['H'] / 1000.0:.3f}")
        prop_columns[1].metric("Entropy s [kJ/kg-K]", f"{state['S'] / 1000.0:.5f}")
        prop_columns[2].metric("Density D [kg/m^3]", f"{state['D']:.3f}")
        prop_columns[3].metric("Internal energy u [kJ/kg]", f"{state['U'] / 1000.0:.3f}")

        info_columns = st.columns(3)
        info_columns[0].metric(
            f"Temperature [{temperature_unit}]",
            f"{from_kelvin(state['T'], temperature_unit):.3f}",
        )
        info_columns[1].metric(
            f"Pressure [{pressure_unit}]",
            f"{from_pascal(state['P'], pressure_unit):.3f}",
        )
        if np.isnan(state["Q"]):
            info_columns[2].metric("Quality", "Not in 2-phase")
        else:
            info_columns[2].metric("Quality", f"{state['Q']:.4f}")

        if (
            mode == CYCLE_MODE
            and evaporation_temperature_value is not None
            and condensation_temperature_value is not None
            and outlet_pressure_pa is not None
        ):
            cycle_columns = st.columns(4)
            cycle_columns[0].metric(
                f"Evaporation temperature [{temperature_unit}]",
                f"{evaporation_temperature_value:.3f}",
            )
            cycle_columns[1].metric(
                f"Condensation temperature [{temperature_unit}]",
                f"{condensation_temperature_value:.3f}",
            )
            cycle_columns[2].metric(
                f"Evaporation pressure [{pressure_unit}]",
                f"{from_pascal(pressure_low_pa if pressure_low_pa is not None else state['P'], pressure_unit):.3f}",
            )
            cycle_columns[3].metric(
                f"Condensation pressure [{pressure_unit}]",
                f"{from_pascal(outlet_pressure_pa, pressure_unit):.3f}",
            )

        st.subheader("Isentropic Efficiency Enthalpy")
        st.latex(r"h_{actual} = h_{in} + \frac{h_{isen} - h_{in}}{\eta_{is}}")

        if h_in is not None and h_isen is not None and h_actual is not None:
            h_columns = st.columns(3)
            h_columns[0].metric("h_in [kJ/kg]", f"{h_in / 1000.0:.3f}")
            h_columns[1].metric("h_isen [kJ/kg]", f"{h_isen / 1000.0:.3f}")
            h_columns[2].metric("h_actual [kJ/kg]", f"{h_actual / 1000.0:.3f}")

        if mode == CYCLE_MODE and cycle_states is not None:
            st.subheader("Cycle Performance")
            h1 = cycle_states[1]["H"] / 1000.0
            h2 = cycle_states[2]["H"] / 1000.0
            h3 = cycle_states[3]["H"] / 1000.0
            h4 = cycle_states[4]["H"] / 1000.0

            q_in_specific = h1 - h4
            q_out_specific = h2 - h3
            w_in_specific = h2 - h1
            mass_flow_kg_s = mass_flow_kg_min / 60.0

            q_in_rate = mass_flow_kg_s * q_in_specific
            q_out_rate = mass_flow_kg_s * q_out_specific
            w_in_rate = mass_flow_kg_s * w_in_specific
            cop = q_in_specific / w_in_specific if abs(w_in_specific) > 1e-12 else float("nan")

            perf_columns = st.columns(4)
            perf_columns[0].metric("Qin [kW]", f"{q_in_rate:.3f}")
            perf_columns[1].metric("Qout [kW]", f"{q_out_rate:.3f}")
            perf_columns[2].metric("Win [kW]", f"{w_in_rate:.3f}")
            perf_columns[3].metric("COP [-]", f"{cop:.3f}" if np.isfinite(cop) else "Undefined")

            spec_columns = st.columns(4)
            spec_columns[0].metric("q_in specific [kJ/kg]", f"{q_in_specific:.3f}")
            spec_columns[1].metric("q_out specific [kJ/kg]", f"{q_out_specific:.3f}")
            spec_columns[2].metric("w_in specific [kJ/kg]", f"{w_in_specific:.3f}")
            spec_columns[3].metric("Mass flow [kg/min]", f"{mass_flow_kg_min:.3f}")

    st.subheader("Validation")
    st.write(
        "Reference point check: saturated vapor at 0 C for R404A (T=273.15 K, Q=1). "
        "The table compares direct T-Q values vs values recovered from P-H."
    )

    try:
        rows, max_abs_error = validation_rows(REFRIGERANT)
        st.table(rows)
        if max_abs_error < 1e-5:
            st.success("Validation passed: reference point closes within tight numerical tolerance.")
        else:
            st.warning(
                "Validation warning: numerical back-calculation error is higher than expected."
            )
    except ValueError as exc:
        st.error(f"Validation failed due to property range issue: {exc}")

    st.subheader("Accuracy Audit (Static Diagram Data)")
    st.write(
        "Runs an independent residual audit on the static R404A T-s dataset. "
        "Each plotted point is back-calculated with CoolProp and compared to the target isoline value."
    )

    audit_controls = st.columns([1.3, 1.2, 1.2])
    audit_stride = int(
        audit_controls[0].number_input(
            "Audit sampling stride",
            min_value=1,
            max_value=20,
            value=1,
            step=1,
            help="1 checks every plotted point. Larger stride speeds up the audit by sampling points.",
            key="audit_stride_number",
        )
    )
    run_audit = audit_controls[1].button(
        "Run Accuracy Audit",
        use_container_width=True,
        key="run_accuracy_audit_button",
    )
    clear_audit = audit_controls[2].button(
        "Clear Audit Result",
        use_container_width=True,
        key="clear_accuracy_audit_button",
    )

    if clear_audit:
        st.session_state.pop("accuracy_audit_report", None)

    if run_audit:
        with st.spinner("Computing residuals for isobars, isenthalps, quality, isochores, and dome..."):
            st.session_state["accuracy_audit_report"] = static_ts_accuracy_audit(
                fluid=REFRIGERANT,
                temperature_unit=temperature_unit,
                sample_stride=audit_stride,
            )

    audit_report = st.session_state.get("accuracy_audit_report")
    if audit_report is not None:
        if (
            audit_report["unit"] != temperature_unit
            or int(audit_report["sample_stride"]) != int(audit_stride)
        ):
            st.info(
                "Displayed audit was computed with "
                f"unit={audit_report['unit']} and stride={audit_report['sample_stride']}. "
                "Run the audit again to refresh for current settings."
            )

        table_rows = []
        for row in audit_report["rows"]:
            table_rows.append(
                {
                    "Family": row["family"],
                    "N": row["n"],
                    "Mean": format_scientific(row["mean"]),
                    "P95": format_scientific(row["p95"]),
                    "Max": format_scientific(row["max"]),
                    "Failed": row["failed"],
                    "P95 threshold": format_scientific(row["threshold_p95"]),
                    "Pass": "Yes" if row["pass"] else "No",
                }
            )

        st.table(table_rows)
        if audit_report["overall_pass"]:
            st.success(
                "Accuracy audit passed for all families against configured residual thresholds."
            )
        else:
            st.warning(
                "Accuracy audit found at least one family outside threshold or with failed points."
            )


if __name__ == "__main__":
    main()
