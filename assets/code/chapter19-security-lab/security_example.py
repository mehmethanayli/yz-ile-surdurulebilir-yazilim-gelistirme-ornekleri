"""Local teaching boundaries, not an authentication or web application layer.

Actor and Task represent trusted server-side records, never request-body data.
SQLite is an in-memory teaching database, not the target PostgreSQL system.
"""
from dataclasses import dataclass, replace
from html import escape
import sqlite3


@dataclass(frozen=True)
class Actor:
    identifier: str
    active: bool


@dataclass(frozen=True)
class Task:
    identifier: str
    owner_id: str
    status: str = "open"


def may_access_task(actor: Actor | None, task: Task) -> bool:
    return (actor is not None and actor.active is True
            and actor.identifier == task.owner_id)


def complete_task(actor: Actor | None, task: Task) -> Task:
    if not may_access_task(actor, task):
        raise PermissionError("Task access denied")
    if task.status not in {"open", "completed"}:
        raise ValueError("Invalid task state")
    return replace(task, status="completed")


def find_own_tasks(connection: sqlite3.Connection, actor: Actor | None,
                   title: str) -> list[tuple[str, str]]:
    if actor is None or actor.active is not True:
        raise PermissionError("Task access denied")
    return connection.execute(
        "SELECT id, title FROM tasks WHERE owner_id = ? AND title = ? ORDER BY id",
        (actor.identifier, title),
    ).fetchall()


def render_note_text(note: str) -> str:
    """Only text inside this fixed HTML element; not JS, CSS or URL encoding."""
    return "<p>" + escape(note, quote=True) + "</p>"
