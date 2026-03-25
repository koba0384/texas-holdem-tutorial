import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="NEON HOLD'EM", page_icon="🃏", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
  .block-container {padding-top: 1rem; padding-bottom: 0.5rem;}
  [data-testid="stHeader"] {display:none;}
  #MainMenu {visibility:hidden;}
  footer {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

HTML = r'''
<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>NEON HOLD'EM</title>
<style>
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; background: transparent; }
  body {
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    color: #eef4ff;
    background:
      radial-gradient(circle at top, rgba(24, 70, 120, 0.24), transparent 28%),
      radial-gradient(circle at bottom, rgba(0, 255, 180, 0.10), transparent 24%),
      linear-gradient(180deg, #08121f 0%, #050b14 100%);
  }
  .nh-root {
    min-height: 100vh;
    padding: max(12px, env(safe-area-inset-top)) 12px calc(12px + env(safe-area-inset-bottom));
  }
  .nh-shell { max-width: 1400px; margin: 0 auto; }
  .nh-header {
    display: flex; align-items: center; justify-content: space-between; gap: 16px;
    margin-bottom: 16px; flex-wrap: wrap;
  }
  .nh-title-wrap h1 { margin: 0; font-size: 28px; letter-spacing: 0.06em; }
  .nh-title-wrap p { margin: 4px 0 0; color: #9db0cc; font-size: 14px; }
  .nh-top-actions { display: flex; gap: 10px; flex-wrap: wrap; }
  .nh-btn {
    appearance: none; border: 1px solid rgba(160, 198, 255, 0.22);
    background: linear-gradient(180deg, rgba(28, 47, 74, 0.95), rgba(11, 18, 29, 0.95));
    color: #eef4ff; border-radius: 14px; padding: 12px 16px; cursor: pointer;
    transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease, opacity 180ms ease;
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.22); font-weight: 600;
  }
  .nh-btn:hover:not(:disabled) {
    transform: translateY(-1px); border-color: rgba(120, 242, 218, 0.48);
    box-shadow: 0 0 0 1px rgba(120, 242, 218, 0.12), 0 12px 24px rgba(0, 0, 0, 0.26);
  }
  .nh-btn:disabled { opacity: 0.4; cursor: not-allowed; }
  .nh-btn.primary {
    background: linear-gradient(180deg, rgba(17, 103, 81, 0.95), rgba(9, 53, 42, 0.95));
    border-color: rgba(100, 255, 220, 0.28);
  }
  .nh-btn.warn {
    background: linear-gradient(180deg, rgba(106, 40, 58, 0.95), rgba(59, 17, 29, 0.95));
    border-color: rgba(255, 142, 175, 0.25);
  }
  .nh-layout { display: grid; grid-template-columns: minmax(0, 1.55fr) minmax(320px, 420px); gap: 16px; align-items: start; }
  .nh-stage-panel, .nh-side-panel {
    background: linear-gradient(180deg, rgba(11, 21, 35, 0.9), rgba(7, 13, 24, 0.92));
    border: 1px solid rgba(133, 170, 221, 0.14); border-radius: 24px; overflow: hidden;
    box-shadow: 0 18px 36px rgba(0, 0, 0, 0.28); backdrop-filter: blur(12px);
  }
  .nh-stage-panel { padding: 16px; }
  .nh-stage-top { display: flex; justify-content: space-between; gap: 12px; margin-bottom: 12px; flex-wrap: wrap; }
  .nh-status-strip { display: flex; gap: 10px; flex-wrap: wrap; }
  .nh-pill {
    border-radius: 999px; padding: 8px 12px; font-size: 12px; letter-spacing: 0.04em;
    background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.08); color: #c6d7f1;
  }
  .nh-pill.active { background: rgba(87, 241, 209, 0.12); color: #9bffe8; border-color: rgba(87, 241, 209, 0.3); }
  .nh-table {
    position: relative; min-height: 720px; border-radius: 32px; overflow: hidden;
    background: radial-gradient(circle at center, rgba(17, 84, 69, 0.55), rgba(4, 33, 32, 0.92) 65%), linear-gradient(180deg, #0d352c 0%, #0a241e 100%);
    border: 1px solid rgba(116, 183, 152, 0.18);
    box-shadow: inset 0 0 0 12px rgba(74, 36, 18, 0.68), inset 0 0 0 16px rgba(146, 93, 59, 0.24), 0 22px 36px rgba(0, 0, 0, 0.35);
  }
  .nh-table::before {
    content: ""; position: absolute; inset: 16px; border-radius: 999px;
    border: 1px solid rgba(200, 255, 235, 0.08); pointer-events: none;
  }
  .nh-center {
    position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%);
    display: flex; flex-direction: column; align-items: center; gap: 18px; z-index: 2; width: min(520px, 86%);
  }
  .nh-community { display: flex; gap: 12px; align-items: center; justify-content: center; min-height: 120px; flex-wrap: wrap; }
  .nh-pot {
    min-width: 220px; text-align: center; border-radius: 22px; padding: 14px 20px;
    background: rgba(9, 16, 27, 0.62); border: 1px solid rgba(255, 214, 112, 0.16);
    box-shadow: 0 0 0 1px rgba(255, 214, 112, 0.05), 0 10px 24px rgba(0, 0, 0, 0.28); animation: nh-pop 300ms ease;
  }
  .nh-pot-label { color: #f6d57f; font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; }
  .nh-pot-value { font-size: 36px; font-weight: 800; margin-top: 4px; color: #fff3b6; }
  .nh-winner-banner {
    width: 100%; text-align: center; border-radius: 18px; padding: 12px 16px;
    background: linear-gradient(180deg, rgba(78, 34, 100, 0.72), rgba(27, 15, 46, 0.82));
    border: 1px solid rgba(196, 131, 255, 0.18); color: #f5ddff; animation: nh-pop 320ms ease;
    box-shadow: 0 14px 28px rgba(0, 0, 0, 0.28);
  }
  .nh-seat {
    position: absolute; width: 260px; padding: 12px; border-radius: 22px;
    background: linear-gradient(180deg, rgba(8, 15, 27, 0.82), rgba(7, 12, 22, 0.68));
    border: 1px solid rgba(155, 190, 240, 0.08);
    transition: transform 220ms ease, box-shadow 220ms ease, border-color 220ms ease, opacity 220ms ease;
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.22);
  }
  .nh-seat.active { transform: translateY(-2px) scale(1.015); border-color: rgba(92, 255, 225, 0.34); box-shadow: 0 0 0 1px rgba(92,255,225,0.08), 0 0 30px rgba(92,255,225,0.14); }
  .nh-seat.folded { opacity: 0.46; filter: saturate(0.5); }
  .nh-seat.seat-0 { left: 50%; bottom: 18px; transform: translateX(-50%); }
  .nh-seat.seat-1 { left: 18px; top: 50%; transform: translateY(-50%); }
  .nh-seat.seat-2 { left: 50%; top: 18px; transform: translateX(-50%); }
  .nh-seat.seat-3 { right: 18px; top: 50%; transform: translateY(-50%); }
  .nh-seat.active.seat-0 { transform: translateX(-50%) translateY(-2px) scale(1.015); }
  .nh-seat.active.seat-1 { transform: translateY(-50%) translateY(-2px) scale(1.015); }
  .nh-seat.active.seat-2 { transform: translateX(-50%) translateY(-2px) scale(1.015); }
  .nh-seat.active.seat-3 { transform: translateY(-50%) translateY(-2px) scale(1.015); }
  .nh-seat-head { display: flex; align-items: center; justify-content: space-between; gap: 8px; }
  .nh-player-name { font-size: 14px; font-weight: 800; letter-spacing: 0.04em; }
  .nh-player-style { color: #91a4c2; font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; }
  .nh-role-badges { display: flex; gap: 6px; flex-wrap: wrap; justify-content: flex-end; }
  .nh-role-badge {
    min-width: 34px; text-align: center; border-radius: 999px; padding: 4px 8px;
    background: rgba(255, 255, 255, 0.06); color: #d7e7ff; font-size: 11px; border: 1px solid rgba(255, 255, 255, 0.09);
  }
  .nh-stack-row { display: flex; justify-content: space-between; gap: 10px; margin-top: 10px; font-size: 13px; color: #cbdaf0; }
  .nh-pressure-bar { margin-top: 10px; height: 8px; border-radius: 999px; background: rgba(255,255,255,0.06); overflow: hidden; }
  .nh-pressure-fill { height: 100%; border-radius: inherit; background: linear-gradient(90deg, #6cf5de, #a688ff); transition: width 260ms ease; }
  .nh-cards { display: flex; gap: 10px; margin-top: 12px; align-items: center; min-height: 88px; }
  .nh-card {
    width: 68px; height: 96px; border-radius: 14px; background: linear-gradient(180deg, #ffffff 0%, #e9eef9 100%);
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.25); border: 1px solid rgba(255,255,255,0.34); position: relative;
    color: #0b1220; overflow: hidden; animation: nh-deal-in 360ms ease both;
  }
  .nh-card.small { width: 58px; height: 82px; }
  .nh-card.slot { background: rgba(255,255,255,0.04); border: 1px dashed rgba(255,255,255,0.12); box-shadow: none; }
  .nh-card.back { background: linear-gradient(180deg, #0e2a56 0%, #09162f 100%); border: 1px solid rgba(124,186,255,0.18); }
  .nh-card.glow { box-shadow: 0 0 0 1px rgba(255,255,255,0.22), 0 0 28px rgba(123,255,221,0.26), 0 12px 24px rgba(0,0,0,0.28); }
  .nh-card-back-pattern {
    position: absolute; inset: 7px; border-radius: 10px; border: 1px solid rgba(128,186,255,0.24);
    background: radial-gradient(circle at 30% 25%, rgba(123, 197, 255, 0.18), transparent 24%), radial-gradient(circle at 70% 75%, rgba(123,255,232,0.16), transparent 26%), repeating-linear-gradient(45deg, rgba(255,255,255,0.03) 0, rgba(255,255,255,0.03) 5px, rgba(255,255,255,0.01) 5px, rgba(255,255,255,0.01) 10px);
  }
  .nh-card-corner { position: absolute; left: 8px; top: 6px; font-weight: 800; font-size: 15px; }
  .nh-card-corner.bottom { left: auto; top: auto; right: 8px; bottom: 6px; transform: rotate(180deg); }
  .nh-card-suit { position: absolute; inset: 0; display: grid; place-items: center; font-size: 32px; font-weight: 700; }
  .red { color: #c32445; } .black { color: #121826; }
  .nh-best-hand { margin-top: 8px; min-height: 20px; color: #a7ffe8; font-size: 12px; font-weight: 700; letter-spacing: 0.02em; }
  .nh-action-badge {
    position: absolute; right: 12px; bottom: 12px; border-radius: 999px; padding: 7px 10px;
    background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255,255,255,0.14);
    color: #f6fbff; font-size: 11px; letter-spacing: 0.06em; animation: nh-float 680ms ease both; pointer-events: none;
  }
  .nh-control-panel { margin-top: 14px; display: grid; grid-template-columns: 1fr; gap: 12px; }
  .nh-info-card, .nh-action-panel {
    border-radius: 20px; padding: 14px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
  }
  .nh-info-card h3, .nh-action-panel h3 { margin: 0 0 8px; font-size: 14px; letter-spacing: 0.05em; color: #dbe9ff; }
  .nh-phase-copy { color: #abc1dd; line-height: 1.6; font-size: 14px; }
  .nh-action-grid { display: grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap: 8px; margin-top: 10px; }
  .nh-raise-presets { display: grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap: 8px; margin-top: 10px; }
  .nh-preset {
    border-radius: 12px; padding: 10px 8px; text-align: center; background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08); color: #dce8fb; cursor: pointer; transition: transform 180ms ease, border-color 180ms ease, background 180ms ease; font-size: 12px; font-weight: 700;
  }
  .nh-preset:hover { transform: translateY(-1px); border-color: rgba(132,246,224,0.24); }
  .nh-preset.selected { background: rgba(108,245,222,0.12); border-color: rgba(108,245,222,0.3); color: #9fffee; }
  .nh-preset:disabled { opacity: .4; cursor: not-allowed; }
  .nh-action-summary { margin-top: 10px; color: #c8d7ef; font-size: 13px; display: flex; justify-content: space-between; gap: 10px; flex-wrap: wrap; }
  .nh-side-panel { padding: 14px; }
  .nh-side-panel-head { display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-bottom: 12px; }
  .nh-side-panel-close {
    appearance: none; border: 1px solid rgba(160, 198, 255, 0.16);
    background: rgba(255,255,255,0.05); color: #dce9ff; border-radius: 12px;
    padding: 9px 12px; cursor: pointer; font-weight: 700; white-space: nowrap;
  }
  .nh-side-panel-close:hover { border-color: rgba(120, 242, 218, 0.3); }
  .nh-tabs { display: flex; gap: 8px; margin-bottom: 12px; }
  .nh-tab {
    flex: 1; border-radius: 14px; padding: 11px 12px; text-align: center; cursor: pointer;
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); color: #cfe0f8; font-weight: 700;
    transition: background 180ms ease, border-color 180ms ease, transform 180ms ease;
  }
  .nh-tab.active { background: rgba(99,226,255,0.12); border-color: rgba(99,226,255,0.22); color: #bff6ff; }
  .nh-side-content { max-height: 820px; overflow: auto; padding-right: 6px; }
  .nh-log-item, .nh-rule-card {
    border-radius: 16px; padding: 12px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.06); margin-bottom: 10px;
  }
  .nh-log-item { color: #d9e7fb; line-height: 1.5; font-size: 13px; }
  .nh-rule-card h4 { margin: 0 0 8px; font-size: 14px; color: #eff6ff; }
  .nh-rule-card p, .nh-rule-card li { color: #abc1dd; font-size: 13px; line-height: 1.65; margin: 0; }
  .nh-rule-card ul { margin: 0; padding-left: 18px; }
  .nh-rule-ranks { display: grid; gap: 8px; }
  .nh-rank-row {
    display: flex; justify-content: space-between; gap: 10px; padding: 8px 10px; border-radius: 12px;
    background: rgba(255,255,255,0.03); color: #d7e5fa; font-size: 13px;
  }
  .nh-footer-note { margin-top: 8px; color: #7e93b2; font-size: 12px; line-height: 1.6; }
  @keyframes nh-pop { from { opacity: 0; transform: scale(0.96); } to { opacity: 1; transform: scale(1); } }
  @keyframes nh-deal-in { from { opacity: 0; transform: translateY(10px) scale(0.94); } to { opacity: 1; transform: translateY(0) scale(1); } }
  @keyframes nh-float { 0% { opacity: 0; transform: translateY(8px) scale(0.96); } 20% { opacity: 1; } 100% { opacity: 1; transform: translateY(0) scale(1); } }
  @media (max-width: 1180px) { .nh-layout { grid-template-columns: 1fr; } .nh-side-content { max-height: none; } }
  @media (max-width: 860px) {
    .nh-root { padding: 8px 8px calc(10px + env(safe-area-inset-bottom)); }
    .nh-header { margin-bottom: 10px; }
    .nh-title-wrap h1 { font-size: 22px; }
    .nh-title-wrap p { font-size: 12px; }
    .nh-top-actions { width: 100%; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .nh-btn { padding: 11px 12px; font-size: 14px; }
    .nh-stage-panel { padding: 10px; border-radius: 20px; }
    .nh-stage-top { gap: 8px; margin-bottom: 10px; }
    .nh-status-strip { gap: 6px; }
    .nh-pill { padding: 6px 10px; font-size: 11px; }

    .nh-table {
      min-height: 700px;
      border-radius: 24px;
      box-shadow: inset 0 0 0 8px rgba(74, 36, 18, 0.68), inset 0 0 0 11px rgba(146, 93, 59, 0.20), 0 18px 30px rgba(0, 0, 0, 0.34);
    }
    .nh-table::before { inset: 10px; }
    .nh-center { top: 46%; width: min(92%, 360px); gap: 10px; }
    .nh-community { gap: 6px; min-height: 84px; }
    .nh-card { width: 54px; height: 76px; border-radius: 12px; }
    .nh-card.small { width: 46px; height: 64px; border-radius: 10px; }
    .nh-card-corner { font-size: 12px; left: 6px; top: 5px; }
    .nh-card-corner.bottom { right: 6px; bottom: 5px; }
    .nh-card-suit { font-size: 24px; }
    .nh-pot { min-width: 150px; padding: 10px 14px; border-radius: 18px; }
    .nh-pot-value { font-size: 28px; }
    .nh-winner-banner { padding: 10px 12px; font-size: 13px; }

    .nh-seat { padding: 10px; width: auto; border-radius: 16px; }
    .nh-seat-head { gap: 6px; align-items: flex-start; }
    .nh-player-name { font-size: 12px; }
    .nh-player-style { display: none; }
    .nh-role-badges { gap: 4px; }
    .nh-role-badge { min-width: 28px; font-size: 10px; padding: 3px 6px; }
    .nh-stack-row { margin-top: 8px; gap: 6px; font-size: 11px; }
    .nh-pressure-bar { margin-top: 8px; height: 6px; }
    .nh-cards { gap: 8px; margin-top: 8px; min-height: 64px; }
    .nh-best-hand { margin-top: 6px; min-height: 14px; font-size: 10px; }
    .nh-action-badge { right: 8px; bottom: 8px; font-size: 10px; padding: 5px 8px; }

    .nh-seat.seat-2 { left: 10px; right: 10px; top: 10px; transform: none; width: auto; }
    .nh-seat.seat-1 { left: 10px; top: 120px; transform: none; width: calc(50% - 15px); }
    .nh-seat.seat-3 { right: 10px; top: 120px; transform: none; width: calc(50% - 15px); }
    .nh-seat.seat-0 { left: 10px; right: 10px; bottom: 10px; transform: none; width: auto; }

    .nh-seat.active.seat-0 { transform: scale(1.01); }
    .nh-seat.active.seat-1 { transform: scale(1.01); transform-origin: left center; }
    .nh-seat.active.seat-2 { transform: scale(1.01); }
    .nh-seat.active.seat-3 { transform: scale(1.01); transform-origin: right center; }

    .nh-control-panel { margin-top: 10px; gap: 10px; }
    .nh-info-card, .nh-action-panel { padding: 12px; border-radius: 16px; }
    .nh-info-card h3, .nh-action-panel h3 { font-size: 13px; margin-bottom: 6px; }
    .nh-phase-copy, .nh-action-summary, .nh-footer-note { font-size: 12px; line-height: 1.55; }
    .nh-action-grid, .nh-raise-presets { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .nh-preset { padding: 9px 8px; }

    .nh-side-panel {
      position: sticky;
      bottom: calc(8px + env(safe-area-inset-bottom));
      z-index: 30;
      max-height: 58px;
      padding: 10px;
      border-radius: 18px;
      overflow: hidden;
      transition: max-height 220ms ease, box-shadow 220ms ease, border-color 220ms ease;
    }
    .nh-side-panel.open {
      max-height: min(56vh, 420px);
      border-color: rgba(132, 246, 224, 0.18);
      box-shadow: 0 18px 36px rgba(0, 0, 0, 0.36);
    }
    .nh-side-panel-head { margin-bottom: 0; }
    .nh-side-panel.open .nh-side-panel-head { margin-bottom: 10px; }
    .nh-side-panel:not(.open) .nh-side-content { display: none; }
    .nh-side-panel-close { padding: 8px 10px; font-size: 12px; }
    .nh-tabs { margin-bottom: 0; }
    .nh-side-panel.open .nh-tabs { margin-bottom: 10px; }
    .nh-side-content { max-height: calc(min(56vh, 420px) - 86px); padding-right: 2px; }
    .nh-rule-card, .nh-log-item { padding: 10px; margin-bottom: 8px; }
    .nh-rule-card p, .nh-rule-card li, .nh-log-item, .nh-rank-row { font-size: 12px; }
  }
</style>
</head>
<body>
<div id="app"></div>
<script>
const PLAYER_COUNT = 4;
const STARTING_STACK = 1000;
const SMALL_BLIND = 10;
const BIG_BLIND = 20;
const SUITS = ["♠", "♥", "♦", "♣"];
const RANKS = [
  { label: "2", value: 2 }, { label: "3", value: 3 }, { label: "4", value: 4 },
  { label: "5", value: 5 }, { label: "6", value: 6 }, { label: "7", value: 7 },
  { label: "8", value: 8 }, { label: "9", value: 9 }, { label: "10", value: 10 },
  { label: "J", value: 11 }, { label: "Q", value: 12 }, { label: "K", value: 13 }, { label: "A", value: 14 },
];

function clamp(value, min, max) { return Math.max(min, Math.min(max, value)); }
function pushLog(log, text) { return [{ id: `${Date.now()}-${Math.random()}`, text }, ...log].slice(0, 18); }
function streetLabel(street) {
  switch (street) {
    case "preflop": return "Pre-Flop";
    case "flop": return "Flop";
    case "turn": return "Turn";
    case "river": return "River";
    case "showdown": return "Showdown";
    default: return "Idle";
  }
}
function currentStreetGuide(street) {
  switch (street) {
    case "preflop": return "各プレイヤーに2枚の手札が配られた直後。SB/BBのあとに最初のベッティングが始まる。";
    case "flop": return "場に3枚公開。ここから手札2枚とコミュニティカードを組み合わせて5枚役を作る。";
    case "turn": return "4枚目のコミュニティカード公開。レンジ差が出やすく、サイズ勝負も強くなる。";
    case "river": return "最後の5枚目公開。これ以上カードは増えないので、最終ベットかショーダウン。";
    case "showdown": return "残ったプレイヤーが手札を見せ合い、最良の5枚役で勝敗判定。";
    default: return "新しいハンドを開始してください。";
  }
}
function createBasePlayers() {
  return [
    { id: 0, seat: 0, name: "YOU", isHuman: true, style: "hero" },
    { id: 1, seat: 1, name: "AI-1", isHuman: false, style: "tight" },
    { id: 2, seat: 2, name: "AI-2", isHuman: false, style: "aggressive" },
    { id: 3, seat: 3, name: "AI-3", isHuman: false, style: "tricky" },
  ].map((p) => ({ ...p, stack: STARTING_STACK, hand: [], folded: false, allIn: false, lastAction: "", lastActionAt: 0, pressure: 0 }));
}
function createEmptyGame() {
  return {
    dealer: 0, smallBlind: 1, bigBlind: 2, handNo: 0, street: "idle", deck: [], community: [],
    players: createBasePlayers(), streetBets: Array(PLAYER_COUNT).fill(0), totalBets: Array(PLAYER_COUNT).fill(0),
    currentBet: 0, minRaise: BIG_BLIND, pot: 0, currentPlayer: -1, pending: [], waitingAdvance: false,
    winnerText: "", showdownSummary: [], log: [], panelTab: "rules", selectedRaiseTarget: BIG_BLIND,
    sidePanelOpen: !window.matchMedia("(max-width: 860px)").matches,
  };
}
function createDeck() {
  const deck = [];
  for (const suit of SUITS) for (const rank of RANKS) deck.push({ id: `${rank.label}${suit}`, rank: rank.value, label: rank.label, suit, color: (suit === "♥" || suit === "♦") ? "red" : "black" });
  return deck;
}
function shuffle(array) {
  const deck = [...array];
  for (let i = deck.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [deck[i], deck[j]] = [deck[j], deck[i]];
  }
  return deck;
}
function drawCards(deck, count) {
  const cards = [];
  for (let i = 0; i < count; i++) {
    const c = deck.pop();
    if (c) cards.push(c);
  }
  return cards;
}
function nextSeat(from, players, predicate = () => true) {
  for (let step = 1; step <= players.length; step++) {
    const idx = (from + step) % players.length;
    if (predicate(players[idx], idx)) return idx;
  }
  return from;
}
function actionEligible(player) { return !player.folded && !player.allIn && player.stack > 0; }
function aliveIndexes(players) { return players.map((p, i) => (!p.folded ? i : -1)).filter((i) => i !== -1); }
function compareScores(a, b) {
  const len = Math.max(a.length, b.length);
  for (let i = 0; i < len; i++) {
    const av = a[i] ?? 0; const bv = b[i] ?? 0;
    if (av > bv) return 1; if (av < bv) return -1;
  }
  return 0;
}
function getStraightHigh(ranks) {
  const unique = [...new Set(ranks)].sort((a, b) => b - a);
  if (unique.includes(14)) unique.push(1);
  let run = 1, best = 0;
  for (let i = 1; i < unique.length; i++) {
    if (unique[i] === unique[i - 1] - 1) {
      run += 1; if (run >= 5) best = Math.max(best, unique[i - 4]);
    } else if (unique[i] !== unique[i - 1]) run = 1;
  }
  return best;
}
function evaluate5(cards) {
  const ranks = cards.map((c) => c.rank).sort((a, b) => b - a);
  const suits = cards.map((c) => c.suit);
  const isFlush = suits.every((s) => s === suits[0]);
  const straightHigh = getStraightHigh(ranks);
  const counts = new Map();
  for (const r of ranks) counts.set(r, (counts.get(r) || 0) + 1);
  const groups = [...counts.entries()].sort((a, b) => (b[1] !== a[1] ? b[1] - a[1] : b[0] - a[0]));
  if (isFlush && straightHigh) return { score: [8, straightHigh], name: straightHigh === 14 ? "ロイヤルストレートフラッシュ" : "ストレートフラッシュ" };
  if (groups[0][1] === 4) return { score: [7, groups[0][0], groups.find((g) => g[1] === 1)[0]], name: "フォーカード" };
  if (groups[0][1] === 3 && groups[1] && groups[1][1] >= 2) return { score: [6, groups[0][0], groups[1][0]], name: "フルハウス" };
  if (isFlush) return { score: [5, ...ranks], name: "フラッシュ" };
  if (straightHigh) return { score: [4, straightHigh], name: "ストレート" };
  if (groups[0][1] === 3) {
    const kickers = groups.filter((g) => g[1] === 1).map((g) => g[0]).sort((a, b) => b - a);
    return { score: [3, groups[0][0], ...kickers], name: "スリーカード" };
  }
  if (groups[0][1] === 2 && groups[1] && groups[1][1] === 2) {
    const pairRanks = [groups[0][0], groups[1][0]].sort((a, b) => b - a);
    const kicker = groups.find((g) => g[1] === 1)[0];
    return { score: [2, pairRanks[0], pairRanks[1], kicker], name: "ツーペア" };
  }
  if (groups[0][1] === 2) {
    const kickers = groups.filter((g) => g[1] === 1).map((g) => g[0]).sort((a, b) => b - a);
    return { score: [1, groups[0][0], ...kickers], name: "ワンペア" };
  }
  return { score: [0, ...ranks], name: "ハイカード" };
}
function bestOfSeven(cards) {
  let best = null;
  for (let a = 0; a < cards.length - 4; a++) for (let b = a + 1; b < cards.length - 3; b++) for (let c = b + 1; c < cards.length - 2; c++) for (let d = c + 1; d < cards.length - 1; d++) for (let e = d + 1; e < cards.length; e++) {
    const hand = [cards[a], cards[b], cards[c], cards[d], cards[e]];
    const evaluated = evaluate5(hand);
    if (!best || compareScores(evaluated.score, best.score) > 0) best = { ...evaluated, cards: hand };
  }
  return best;
}
function estimatePreflopStrength(hand) {
  const [a, b] = [...hand].sort((x, y) => y.rank - x.rank);
  let score = 0.12 + (a.rank + b.rank) / 38;
  if (a.rank === b.rank) score += 0.34 + a.rank / 40;
  if (a.suit === b.suit) score += 0.08;
  if (Math.abs(a.rank - b.rank) === 1) score += 0.06;
  if (a.rank >= 11 && b.rank >= 10) score += 0.06;
  if (a.rank === 14 || b.rank === 14) score += 0.04;
  return clamp(score, 0.05, 0.98);
}
function estimateStrength(game, idx) {
  const player = game.players[idx];
  if (game.community.length === 0) return estimatePreflopStrength(player.hand);
  const best = bestOfSeven([...player.hand, ...game.community]);
  const categoryPart = best.score[0] / 8;
  const holePart = Math.max(player.hand[0].rank, player.hand[1].rank) / 16;
  return clamp(categoryPart * 0.82 + holePart * 0.18, 0.05, 0.99);
}
function decideAiAction(game, idx) {
  const player = game.players[idx];
  const toCall = Math.max(0, game.currentBet - game.streetBets[idx]);
  const strength = estimateStrength(game, idx);
  const potOdds = toCall / Math.max(1, game.pot + toCall);
  const styleMods = { tight: { fold: 0.12, raise: -0.08 }, aggressive: { fold: -0.06, raise: 0.16 }, tricky: { fold: -0.01, raise: 0.08 } };
  const mod = styleMods[player.style] || { fold: 0, raise: 0 };
  let foldChance = 0.16 + potOdds * 0.5 - strength * 0.46 + mod.fold;
  let raiseChance = 0.12 + strength * 0.4 - potOdds * 0.16 + mod.raise;
  if (toCall === 0) foldChance = 0;
  if (strength > 0.8) raiseChance += 0.12;
  if (strength < 0.34 && toCall > BIG_BLIND * 2) foldChance += 0.16;
  if (player.pressure > 60) raiseChance += 0.06;
  foldChance = clamp(foldChance, 0, 0.8);
  raiseChance = clamp(raiseChance, 0.04, 0.8);
  if (toCall > player.stack * 0.55 && strength < 0.55) return { type: "fold" };
  const r = Math.random();
  if (toCall > 0 && r < foldChance) return { type: "fold" };
  if (r > 1 - raiseChance && player.stack > toCall + BIG_BLIND) {
    const minTarget = game.currentBet === 0 ? BIG_BLIND : game.currentBet + game.minRaise;
    const bonusUnits = player.style === "aggressive" ? 3 + Math.floor(Math.random() * 3) : player.style === "tricky" ? 2 + Math.floor(Math.random() * 3) : 1 + Math.floor(Math.random() * 2);
    const desired = Math.max(minTarget, game.currentBet + BIG_BLIND * bonusUnits);
    const maxTarget = game.streetBets[idx] + player.stack;
    return { type: "raise", targetTotal: Math.min(desired, maxTarget) };
  }
  return { type: "call" };
}
function postForcedBet(players, streetBets, totalBets, idx, amount, label) {
  const current = players[idx];
  const paid = Math.min(amount, current.stack);
  const nextStack = current.stack - paid;
  players[idx] = { ...current, stack: nextStack, allIn: nextStack === 0, lastAction: label, lastActionAt: Date.now() };
  streetBets[idx] += paid; totalBets[idx] += paid; return paid;
}
function setPlayerAction(player, action, pressureDelta = 0) {
  return { ...player, lastAction: action, lastActionAt: Date.now(), pressure: clamp((player.pressure || 0) + pressureDelta, 0, 100) };
}
function dealNewHand(prev, keepDealer = true) {
  let players = prev.players.map((p) => ({ ...p, hand: [], folded: false, allIn: false, lastAction: "", lastActionAt: 0, pressure: Math.max(0, p.pressure - 8) }));
  if (players.some((p) => p.stack <= 0)) players = players.map((p) => ({ ...p, stack: STARTING_STACK }));
  const deck = shuffle(createDeck());
  for (let round = 0; round < 2; round++) for (let seat = 0; seat < PLAYER_COUNT; seat++) players[seat].hand.push(deck.pop());
  const dealer = keepDealer ? prev.dealer : (prev.dealer + 1) % PLAYER_COUNT;
  const smallBlind = nextSeat(dealer, players, (p) => p.stack > 0);
  const bigBlind = nextSeat(smallBlind, players, (p) => p.stack > 0);
  const currentPlayer = nextSeat(bigBlind, players, (p) => actionEligible(p));
  const streetBets = Array(PLAYER_COUNT).fill(0), totalBets = Array(PLAYER_COUNT).fill(0);
  let pot = 0;
  pot += postForcedBet(players, streetBets, totalBets, smallBlind, SMALL_BLIND, "SB");
  pot += postForcedBet(players, streetBets, totalBets, bigBlind, BIG_BLIND, "BB");
  const pending = players.map((p, i) => (actionEligible(p) ? i : -1)).filter((i) => i !== -1);
  const next = { ...prev, dealer, smallBlind, bigBlind, handNo: prev.handNo + 1, street: "preflop", deck, community: [], players, streetBets, totalBets, currentBet: streetBets[bigBlind], minRaise: BIG_BLIND, pot, currentPlayer, pending, waitingAdvance: false, winnerText: "", showdownSummary: [], log: [], selectedRaiseTarget: BIG_BLIND };
  next.log = pushLog(next.log, `Hand #${next.handNo} 開始`);
  next.log = pushLog(next.log, `${players[smallBlind].name} が SB ${streetBets[smallBlind]}`);
  next.log = pushLog(next.log, `${players[bigBlind].name} が BB ${streetBets[bigBlind]}`);
  return next;
}
function finalizeAfterAction(next, actor) {
  const alive = aliveIndexes(next.players);
  if (alive.length === 1) {
    const winner = alive[0];
    next.players[winner] = setPlayerAction({ ...next.players[winner], stack: next.players[winner].stack + next.pot }, "WIN", 10);
    next.street = "showdown"; next.currentPlayer = -1; next.pending = []; next.waitingAdvance = false;
    next.winnerText = `${next.players[winner].name} が ${next.pot} を獲得`;
    next.log = pushLog(next.log, next.winnerText);
    next.showdownSummary = [{ pot: next.pot, winners: [winner], handName: "フォールド勝ち" }];
    return next;
  }
  next.pending = next.pending.filter((i) => i !== actor && actionEligible(next.players[i]));
  if (next.pending.length === 0) {
    next.currentPlayer = -1; next.waitingAdvance = true; return next;
  }
  next.currentPlayer = nextSeat(actor, next.players, (_, i) => next.pending.includes(i));
  next.waitingAdvance = false;
  return next;
}
function applyAction(prev, actor, type, targetTotal = 0) {
  if (prev.street === "showdown" || prev.waitingAdvance) return prev;
  if (prev.currentPlayer !== actor) return prev;
  const next = structuredClone(prev);
  const player = next.players[actor];
  if (!player || player.folded || player.allIn) return prev;
  const playerStreetBet = next.streetBets[actor];
  const toCall = Math.max(0, next.currentBet - playerStreetBet);
  if (type === "fold") {
    next.players[actor] = setPlayerAction({ ...player, folded: true }, "FOLD", -8);
    next.log = pushLog(next.log, `${player.name} がフォールド`);
    return finalizeAfterAction(next, actor);
  }
  if (type === "call") {
    const paid = Math.min(toCall, player.stack);
    const nextStack = player.stack - paid;
    const nextStreetBet = playerStreetBet + paid;
    next.players[actor] = setPlayerAction({ ...player, stack: nextStack, allIn: nextStack === 0 }, toCall === 0 ? "CHECK" : nextStack === 0 && paid < toCall ? "ALL-IN" : "CALL", 2);
    next.streetBets[actor] = nextStreetBet; next.totalBets[actor] += paid; next.pot += paid;
    if (toCall === 0) next.log = pushLog(next.log, `${player.name} がチェック`);
    else if (nextStack === 0 && paid < toCall) next.log = pushLog(next.log, `${player.name} がオールイン ${paid}`);
    else next.log = pushLog(next.log, `${player.name} がコール ${paid}`);
    return finalizeAfterAction(next, actor);
  }
  if (type === "raise") {
    const minTarget = next.currentBet === 0 ? BIG_BLIND : next.currentBet + next.minRaise;
    const desiredTarget = Math.max(minTarget, targetTotal || minTarget);
    const maxTarget = playerStreetBet + player.stack;
    const finalTarget = Math.min(desiredTarget, maxTarget);
    if (finalTarget <= next.currentBet) return applyAction(prev, actor, "call");
    const addAmount = finalTarget - playerStreetBet;
    const nextStack = player.stack - addAmount;
    const oldCurrentBet = next.currentBet;
    next.players = next.players.map((p, i) => i === actor ? setPlayerAction({ ...p, stack: nextStack, allIn: nextStack === 0 }, oldCurrentBet === 0 ? "BET" : "RAISE", 14) : { ...p, pressure: clamp((p.pressure || 0) - 2, 0, 100) });
    next.streetBets[actor] = finalTarget; next.totalBets[actor] += addAmount; next.pot += addAmount; next.currentBet = finalTarget; next.minRaise = Math.max(BIG_BLIND, finalTarget - oldCurrentBet);
    next.pending = next.players.map((p, i) => (i !== actor && actionEligible(p) ? i : -1)).filter((i) => i !== -1);
    next.log = pushLog(next.log, `${player.name} が ${oldCurrentBet === 0 ? "ベット" : "レイズ"} ${finalTarget}`);
    return finalizeAfterAction(next, actor);
  }
  return prev;
}
function startStreet(prev, newStreet, drawCount) {
  const next = structuredClone(prev);
  next.street = newStreet; next.community = [...next.community, ...drawCards(next.deck, drawCount)]; next.streetBets = Array(PLAYER_COUNT).fill(0); next.currentBet = 0; next.minRaise = BIG_BLIND; next.players = next.players.map((p) => ({ ...p, lastAction: "" }));
  next.pending = next.players.map((p, i) => (actionEligible(p) ? i : -1)).filter((i) => i !== -1);
  next.log = pushLog(next.log, `${streetLabel(newStreet)} へ`);
  if (next.pending.length === 0) { next.currentPlayer = -1; next.waitingAdvance = true; next.log = pushLog(next.log, `全員オールインのため自動進行`); return next; }
  next.currentPlayer = nextSeat(next.dealer, next.players, (_, i) => next.pending.includes(i)); next.waitingAdvance = false; return next;
}
function distributeSidePots(game) {
  const remaining = [...game.totalBets], payouts = Array(PLAYER_COUNT).fill(0), summary = [];
  while (remaining.some((v) => v > 0)) {
    const layer = Math.min(...remaining.filter((v) => v > 0));
    const contributors = remaining.map((v, i) => (v > 0 ? i : -1)).filter((i) => i !== -1);
    const potSize = layer * contributors.length;
    const eligible = contributors.filter((i) => !game.players[i].folded);
    contributors.forEach((i) => { remaining[i] -= layer; });
    if (!eligible.length) continue;
    const ranked = eligible.map((i) => ({ i, best: bestOfSeven([...game.players[i].hand, ...game.community]) }));
    ranked.sort((a, b) => compareScores(b.best.score, a.best.score));
    const bestScore = ranked[0].best.score;
    const winners = ranked.filter((r) => compareScores(r.best.score, bestScore) === 0).map((r) => r.i);
    const share = Math.floor(potSize / winners.length);
    let remainder = potSize % winners.length;
    winners.forEach((winner) => { payouts[winner] += share + (remainder > 0 ? 1 : 0); if (remainder > 0) remainder -= 1; });
    summary.push({ pot: potSize, winners, handName: ranked[0].best.name });
  }
  return { payouts, summary };
}
function resolveShowdown(prev) {
  const next = structuredClone(prev);
  const { payouts, summary } = distributeSidePots(next);
  next.players = next.players.map((p, i) => (payouts[i] > 0 ? setPlayerAction({ ...p, stack: p.stack + payouts[i] }, "WIN", 8) : p));
  next.street = "showdown"; next.currentPlayer = -1; next.pending = []; next.waitingAdvance = false; next.showdownSummary = summary;
  const major = payouts.map((chips, i) => ({ i, chips })).filter((x) => x.chips > 0).sort((a, b) => b.chips - a.chips);
  next.winnerText = major.length === 1 ? `${next.players[major[0].i].name} が ${major[0].chips} を獲得` : major.map((x) => `${next.players[x.i].name} ${x.chips}`).join(" / ");
  next.log = pushLog(next.log, "ショーダウン");
  summary.forEach((s, idx) => { const names = s.winners.map((i) => next.players[i].name).join(" / "); next.log = pushLog(next.log, `Pot ${idx + 1}: ${names} が ${s.pot} (${s.handName})`); });
  return next;
}
function advanceStreet(prev) {
  if (prev.street === "showdown" || prev.street === "idle") return prev;
  if (prev.street === "preflop") return startStreet(prev, "flop", 3);
  if (prev.street === "flop") return startStreet(prev, "turn", 1);
  if (prev.street === "turn") return startStreet(prev, "river", 1);
  if (prev.street === "river") return resolveShowdown(prev);
  return prev;
}
function roleBadge(game, idx) {
  const badges = [];
  if (idx === game.dealer) badges.push("D");
  if (idx === game.smallBlind) badges.push("SB");
  if (idx === game.bigBlind) badges.push("BB");
  return badges;
}
function esc(s) { return String(s).replace(/[&<>"']/g, (m) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m])); }
function cardHTML(card, { hidden = false, small = false, glow = false } = {}) {
  if (!card && !hidden) return `<div class="nh-card ${small ? 'small' : ''} slot"></div>`;
  return `<div class="nh-card ${small ? 'small' : ''} ${hidden ? 'back' : ''} ${glow ? 'glow' : ''}">${hidden ? `<div class="nh-card-back-pattern"></div>` : `<div class="nh-card-corner ${card.color}">${esc(card.label)}</div><div class="nh-card-suit ${card.color}">${esc(card.suit)}</div><div class="nh-card-corner bottom ${card.color}">${esc(card.label)}</div>`}</div>`;
}

let game = dealNewHand(createEmptyGame(), true);
let timers = { ai: null, advance: null };
const app = document.getElementById('app');

function clearTimers() { if (timers.ai) clearTimeout(timers.ai); if (timers.advance) clearTimeout(timers.advance); timers.ai = null; timers.advance = null; }
function recomputeSelectedRaiseTarget() {
  const hero = game.players[0];
  const heroMaxTarget = game.streetBets[0] + hero.stack;
  const minRaiseTarget = game.currentBet === 0 ? BIG_BLIND : game.currentBet + game.minRaise;
  game.selectedRaiseTarget = Math.min(heroMaxTarget, Math.max(minRaiseTarget, BIG_BLIND));
}
function maybeSchedule() {
  if (timers.advance) { clearTimeout(timers.advance); timers.advance = null; }
  if (timers.ai) { clearTimeout(timers.ai); timers.ai = null; }
  if (game.waitingAdvance) {
    timers.advance = setTimeout(() => { game = advanceStreet(game); recomputeSelectedRaiseTarget(); render(); }, game.street === 'river' ? 1200 : 900);
    return;
  }
  const actor = game.players[game.currentPlayer];
  if (!actor || actor.isHuman || actor.folded || actor.allIn || game.street === 'showdown') return;
  timers.ai = setTimeout(() => {
    const decision = decideAiAction(game, game.currentPlayer);
    game = applyAction(game, game.currentPlayer, decision.type, decision.targetTotal || 0);
    recomputeSelectedRaiseTarget();
    render();
  }, 700 + Math.random() * 500);
}
function onAction(type, targetTotal = 0) { game = applyAction(game, 0, type, targetTotal); recomputeSelectedRaiseTarget(); render(); }
function setPanelTab(tab) { game.panelTab = tab; if (window.matchMedia('(max-width: 860px)').matches) game.sidePanelOpen = true; render(); }
function setPanelOpen(open) { game.sidePanelOpen = open; render(); }
function newHand(keepDealer = false) { game = dealNewHand(game, keepDealer); recomputeSelectedRaiseTarget(); render(); }

function render() {
  clearTimers();
  const hero = game.players[0];
  const isMyTurn = game.currentPlayer === 0 && game.street !== 'showdown' && !game.waitingAdvance && !hero.folded && !hero.allIn;
  const toCall = Math.max(0, game.currentBet - game.streetBets[0]);
  const heroMaxTarget = game.streetBets[0] + hero.stack;
  const minRaiseTarget = game.currentBet === 0 ? BIG_BLIND : game.currentBet + game.minRaise;
  const halfPotTarget = Math.max(minRaiseTarget, game.currentBet + Math.max(BIG_BLIND, Math.floor(game.pot / 2)));
  const potTarget = Math.max(minRaiseTarget, game.currentBet + game.pot);
  const allInTarget = heroMaxTarget;
  const showdownHands = {};
  if (game.street === 'showdown') game.players.forEach((p, i) => { if (!p.folded) showdownHands[i] = bestOfSeven([...p.hand, ...game.community]); });
  const phaseText = currentStreetGuide(game.street);
  app.innerHTML = `
  <div class="nh-root">
    <div class="nh-shell">
      <div class="nh-header">
        <div class="nh-title-wrap">
          <h1>NEON HOLD'EM</h1>
          <p>4人卓 / Texas Hold'em inspired / Streamlit MVP</p>
        </div>
        <div class="nh-top-actions">
          <button class="nh-btn primary" data-act="new-hand">新しいハンド</button>
          <button class="nh-btn" data-act="toggle-panel">${game.sidePanelOpen ? 'パネルを閉じる' : 'ルール / ログ'}</button>
        </div>
      </div>
      <div class="nh-layout">
        <section class="nh-stage-panel">
          <div class="nh-stage-top">
            <div class="nh-status-strip">
              <div class="nh-pill">Hand #${game.handNo}</div>
              <div class="nh-pill active">${streetLabel(game.street)}</div>
              <div class="nh-pill">${game.currentPlayer >= 0 ? `${esc(game.players[game.currentPlayer].name)} の番` : '進行中'}</div>
            </div>
            <div class="nh-status-strip">
              <div class="nh-pill">Current Bet: ${game.currentBet}</div>
              <div class="nh-pill">Min Raise: ${game.minRaise}</div>
              <div class="nh-pill">To Call: ${toCall}</div>
            </div>
          </div>
          <div class="nh-table">
            <div class="nh-center">
              <div class="nh-community">
                ${Array.from({ length: 5 }).map((_, index) => cardHTML(game.community[index], { small: false, glow: game.street === 'showdown' })).join('')}
              </div>
              <div class="nh-pot"><div class="nh-pot-label">Pot</div><div class="nh-pot-value">${game.pot}</div></div>
              ${game.winnerText ? `<div class="nh-winner-banner">${esc(game.winnerText)}</div>` : ''}
              ${game.street === 'showdown' ? `<button class="nh-btn primary" data-act="next-hand">次のハンドへ</button>` : ''}
            </div>
            ${game.players.map((player, idx) => {
              const badges = roleBadge(game, idx);
              const showCards = player.isHuman || game.street === 'showdown' || player.folded;
              const best = showdownHands[idx];
              const bestText = game.street === 'showdown' && best ? best.name : '';
              return `<div class="nh-seat seat-${idx} ${game.currentPlayer === idx && !game.waitingAdvance ? 'active' : ''} ${player.folded ? 'folded' : ''}">
                <div class="nh-seat-head">
                  <div><div class="nh-player-name">${esc(player.name)}</div><div class="nh-player-style">${esc(player.style)}</div></div>
                  <div class="nh-role-badges">${badges.map((badge) => `<div class="nh-role-badge">${esc(badge)}</div>`).join('')}</div>
                </div>
                <div class="nh-stack-row"><span>Stack: ${player.stack}</span><span>Street Bet: ${game.streetBets[idx]}</span></div>
                <div class="nh-pressure-bar"><div class="nh-pressure-fill" style="width:${player.pressure}%"></div></div>
                <div class="nh-cards">${cardHTML(player.hand[0], { hidden: !showCards, small: true, glow: game.street === 'showdown' && !player.folded })}${cardHTML(player.hand[1], { hidden: !showCards, small: true, glow: game.street === 'showdown' && !player.folded })}</div>
                <div class="nh-best-hand">${player.folded ? 'Folded' : esc(bestText)}${player.allIn && game.street !== 'showdown' ? ' / ALL-IN' : ''}</div>
                ${player.lastAction ? `<div class="nh-action-badge">${esc(player.lastAction)}</div>` : ''}
              </div>`;
            }).join('')}
          </div>
          <div class="nh-control-panel">
            <div class="nh-info-card">
              <h3>いま何が起きているか</h3>
              <div class="nh-phase-copy">${esc(phaseText)}</div>
            </div>
            <div class="nh-action-panel">
              <h3>アクション</h3>
              <div class="nh-action-summary">
                <span>${isMyTurn ? 'あなたのターンです' : '相手のターンです'}</span>
                <span>あなたの手札: ${hero.hand.map((c) => `${c.label}${c.suit}`).join(' ')}</span>
              </div>
              <div class="nh-action-grid">
                <button class="nh-btn warn" ${!isMyTurn ? 'disabled' : ''} data-act="fold">Fold</button>
                <button class="nh-btn" ${!isMyTurn ? 'disabled' : ''} data-act="call">${toCall === 0 ? 'Check' : `Call ${toCall}`}</button>
                <button class="nh-btn" ${(!isMyTurn || hero.stack <= 0) ? 'disabled' : ''} data-act="min">Min</button>
                <button class="nh-btn primary" ${(!isMyTurn || hero.stack <= 0) ? 'disabled' : ''} data-act="raise">${game.currentBet === 0 ? 'Bet' : 'Raise'} ${game.selectedRaiseTarget}</button>
              </div>
              <div class="nh-raise-presets">
                ${[
                  { key: 'min', label: 'Min', value: Math.min(heroMaxTarget, minRaiseTarget) },
                  { key: 'half', label: '1/2 Pot', value: Math.min(heroMaxTarget, halfPotTarget) },
                  { key: 'pot', label: 'Pot', value: Math.min(heroMaxTarget, potTarget) },
                  { key: 'jam', label: 'All-In', value: allInTarget },
                ].map((preset) => `<button class="nh-preset ${game.selectedRaiseTarget === preset.value ? 'selected' : ''}" ${(!isMyTurn || hero.stack <= 0) ? 'disabled' : ''} data-raise="${preset.value}">${preset.label}<br>${preset.value}</button>`).join('')}
              </div>
              <div class="nh-footer-note">このデモは 4人卓を保つために誰かが bust したら自動でスタックを戻します。サイドポットは対応済みですが、オッドチップの厳密配分は簡略化しています。</div>
            </div>
          </div>
        </section>
        <aside class="nh-side-panel ${game.sidePanelOpen ? 'open' : ''}">
          <div class="nh-side-panel-head">
            <div class="nh-tabs">
              <button class="nh-tab ${game.panelTab === 'rules' ? 'active' : ''}" data-tab="rules">ルール</button>
              <button class="nh-tab ${game.panelTab === 'log' ? 'active' : ''}" data-tab="log">ログ</button>
            </div>
            <button class="nh-side-panel-close" data-act="toggle-panel">${game.sidePanelOpen ? '閉じる' : '開く'}</button>
          </div>
          <div class="nh-side-content">
            ${game.panelTab === 'log' ? game.log.map((entry) => `<div class="nh-log-item">${esc(entry.text)}</div>`).join('') : `
              <div class="nh-rule-card"><h4>目的</h4><p>テキサスホールデムは、自分のホールカード2枚と場のコミュニティカード5枚を組み合わせて、最も強い5枚役を作るゲームです。役の強さだけでなく、ベットで相手を降ろしてポットを取ることもできます。</p></div>
              <div class="nh-rule-card"><h4>1ハンドの流れ</h4><ul><li>Dealer の左隣が SB、その左隣が BB を置く</li><li>全員に2枚ずつ手札が配られる</li><li>Pre-Flop のベット</li><li>Flop で3枚公開 → ベット</li><li>Turn で1枚公開 → ベット</li><li>River で1枚公開 → ベット</li><li>複数人残れば Showdown</li></ul></div>
              <div class="nh-rule-card"><h4>アクションの意味</h4><ul><li>Check: まだ誰も賭けていないときに何も払わず続行</li><li>Call: 現在のベット額に合わせる</li><li>Raise / Bet: さらに大きく賭ける</li><li>Fold: ハンドを降りる</li></ul></div>
              <div class="nh-rule-card"><h4>いまのフェーズ</h4><p>${esc(phaseText)}</p></div>
              <div class="nh-rule-card"><h4>役の強さ</h4><div class="nh-rule-ranks">${[
                ['ストレートフラッシュ', '同じスートで連続5枚'], ['フォーカード', '同ランク4枚'], ['フルハウス', 'スリーカード + ワンペア'], ['フラッシュ', '同じスート5枚'], ['ストレート', '連続5枚'], ['スリーカード', '同ランク3枚'], ['ツーペア', 'ペア2組'], ['ワンペア', 'ペア1組'], ['ハイカード', 'どれも揃わない'],
              ].map(([name, desc]) => `<div class="nh-rank-row"><span>${name}</span><span>${desc}</span></div>`).join('')}</div></div>
              <div class="nh-rule-card"><h4>読み方のコツ</h4><ul><li>強い手だけでなく、相手に強く見せるベットも重要</li><li>Flop 以降は場のカードと自分の2枚の相性を見る</li><li>同じ役ならキッカーで勝敗が決まることがある</li><li>A は高いストレートにも低いストレートにも使われる</li></ul></div>`}
          </div>
        </aside>
      </div>
    </div>
  </div>`;

  app.querySelectorAll('[data-tab]').forEach((el) => el.addEventListener('click', () => setPanelTab(el.getAttribute('data-tab'))));
  app.querySelector('[data-act="new-hand"]').addEventListener('click', () => newHand(false));
  app.querySelectorAll('[data-act="toggle-panel"]').forEach((el) => el.addEventListener('click', () => setPanelOpen(!game.sidePanelOpen)));
  const nextBtn = app.querySelector('[data-act="next-hand"]'); if (nextBtn) nextBtn.addEventListener('click', () => newHand(false));
  const foldBtn = app.querySelector('[data-act="fold"]'); if (foldBtn) foldBtn.addEventListener('click', () => onAction('fold'));
  const callBtn = app.querySelector('[data-act="call"]'); if (callBtn) callBtn.addEventListener('click', () => onAction('call'));
  const minBtn = app.querySelector('[data-act="min"]'); if (minBtn) minBtn.addEventListener('click', () => { game.selectedRaiseTarget = Math.min(heroMaxTarget, minRaiseTarget); render(); });
  const raiseBtn = app.querySelector('[data-act="raise"]'); if (raiseBtn) raiseBtn.addEventListener('click', () => onAction('raise', game.selectedRaiseTarget));
  app.querySelectorAll('[data-raise]').forEach((el) => el.addEventListener('click', () => { game.selectedRaiseTarget = Number(el.getAttribute('data-raise')); render(); }));
  maybeSchedule();
}

recomputeSelectedRaiseTarget();
render();
</script>
</body>
</html>
'''

st.title("NEON HOLD'EM")
st.caption("iPhone 向けに縦長を圧縮したコンパクト版")

components.html(HTML, height=980, scrolling=True)

with st.expander("デプロイ手順メモ", expanded=False):
    st.markdown(
        """
1. このリポジトリを GitHub に push
2. Streamlit Community Cloud で GitHub を接続
3. リポジトリを選び、`app.py` をエントリーポイントに指定
4. Deploy を押す

必要ファイルは `app.py` と `requirements.txt` だけです。
"""
    )
