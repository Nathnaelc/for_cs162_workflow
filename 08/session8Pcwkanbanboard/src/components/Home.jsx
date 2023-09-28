import React from "react";
import TaskColumn from "./TaskColumn";
import { tasks } from "../data";

export default function HomePage() {
  return (
    <div className="home-page">
      <TaskColumn title="To Do" tasks={tasks.toDo} />
      <TaskColumn title="In Progress" tasks={tasks.inProgress} />
      <TaskColumn title="In Review" tasks={tasks.inReview} />
      <TaskColumn title="Done" tasks={tasks.done} />
    </div>
  );
}
