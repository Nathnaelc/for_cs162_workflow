import React from "react";
import TaskCard from "./TaskCard";
import "./TaskColumn.css";

export default function TaskColumn({ title, tasks }) {
  return (
    <div className="kanban-column">
      <h2>{title}</h2>
      {tasks.map((task, index) => (
        <TaskCard key={index} task={task} />
      ))}
    </div>
  );
}
