import React from "react";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <div>
      <h1>Kanban Board React 1 S8</h1>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/new-task">New Task</Link>
      </nav>
    </div>
  );
}
