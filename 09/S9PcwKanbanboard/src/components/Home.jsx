import React, { useState, useEffect } from "react";
import TaskColumn from "./TaskColumn";
import "./Home.css";
const BASE_URL = import.meta.env.VITE_BASE_URL;

export default function HomePage() {
  const [tasks, setTasks] = useState({
    toDo: [],
    inProgress: [],
    inReview: [],
    done: [],
  });

  useEffect(() => {
    // fetch tasks from Flask's API
    fetch(`${BASE_URL}/api/get_tasks`)
      .then((response) => response.json())
      .then((data) => setTasks(data))
      .catch((error) => console.error("Error fetching tasks:", error));
  }, []);

  return (
    <div className="home kanban-board">
      <TaskColumn title="To Do" tasks={tasks.toDo} />
      <TaskColumn title="In Progress" tasks={tasks.inProgress} />
      <TaskColumn title="In Review" tasks={tasks.inReview} />
      <TaskColumn title="Done" tasks={tasks.done} />
    </div>
  );
}
