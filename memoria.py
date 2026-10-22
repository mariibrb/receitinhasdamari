"""Marcações da despensa, compartilhadas e com validade curta."""

from __future__ import annotations

import json
import threading
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from dados import ITENS, chave_item

HORAS = 4
DURACAO = timedelta(hours=HORAS)
ARQUIVO = Path(__file__).resolve().parent / "data" / "despensa.json"
_IDS = {item["id"] for item in ITENS}
_TRAVA = threading.Lock()


def _fuso():
    try:
        return ZoneInfo("America/Sao_Paulo")
    except Exception:
        return datetime.now().astimezone().tzinfo


def _agora() -> datetime:
    return datetime.now(timezone.utc)


def _parse(valor: str) -> datetime | None:
    try:
        momento = datetime.fromisoformat(valor)
    except ValueError:
        return None
    if momento.tzinfo is None:
        momento = momento.replace(tzinfo=timezone.utc)
    return momento.astimezone(timezone.utc)


def _ler() -> dict[str, str]:
    if not ARQUIVO.is_file():
        return {}
    try:
        bruto = json.loads(ARQUIVO.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if not isinstance(bruto, dict):
        return {}
    return {str(chave): str(valor) for chave, valor in bruto.items()}


def _gravar(bruto: dict[str, str]) -> None:
    ARQUIVO.parent.mkdir(parents=True, exist_ok=True)
    temporario = ARQUIVO.with_suffix(".tmp")
    temporario.write_text(json.dumps(bruto, ensure_ascii=False, indent=2), encoding="utf-8")
    temporario.replace(ARQUIVO)


def _vivos(bruto: dict[str, str], agora: datetime) -> dict[str, datetime]:
    vivos = {}
    for item_id, texto in bruto.items():
        if item_id not in _IDS:
            continue
        momento = _parse(texto)
        if momento is None:
            continue
        if agora - momento < DURACAO:
            vivos[item_id] = momento
    return vivos


def carregar() -> dict[str, datetime]:
    with _TRAVA:
        agora = _agora()
        bruto = _ler()
        vivos = _vivos(bruto, agora)
        limpo = {item_id: momento.isoformat() for item_id, momento in vivos.items()}
        if limpo != bruto:
            _gravar(limpo)
        return vivos


def definir(ids: list[str], valor: bool) -> None:
    with _TRAVA:
        agora = _agora()
        vivos = _vivos(_ler(), agora)
        for item_id in ids:
            if item_id not in _IDS:
                continue
            if valor:
                vivos[item_id] = agora
            else:
                vivos.pop(item_id, None)
        _gravar({item_id: momento.isoformat() for item_id, momento in vivos.items()})


def aplicar(estado: dict) -> dict[str, datetime]:
    vivos = carregar()
    for item in ITENS:
        estado[chave_item(item["id"])] = item["id"] in vivos
    return vivos


def proxima_saida(vivos: dict[str, datetime]) -> datetime | None:
    if not vivos:
        return None
    return min(vivos.values()) + DURACAO


def hora_local(momento: datetime) -> str:
    return momento.astimezone(_fuso()).strftime("%H:%M")
