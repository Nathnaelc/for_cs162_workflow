import React, { useState } from "react";
import { addNewTask, tasks } from "../data.js";

export default function NewTask() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [taskType, setTaskType] = useState("toDo");

  const handleSubmit = (e) => {
    e.preventDefault();
    const newTask = { title, description };
    addNewTask(newTask, taskType, tasks); // Use tasks here
    setTitle("");
    setDescription("");
    setTaskType("toDo");
    console.log("New task added", newTask);
  };

  return (
    <div className="new-task">
      <h1>Add New Task</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="title">Title</label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="description">Description</label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          ></textarea>
        </div>
        <div>
          <label htmlFor="taskType">Task Type</label>
          <select
            id="taskType"
            value={taskType}
            onChange={(e) => setTaskType(e.target.value)}
          >
            <option value="toDo">To Do</option>
            <option value="inProgress">In Progress</option>
            <option value="inReview">In Review</option>
            <option value="done">Done</option>
          </select>
        </div>
        <button type="submit">Add Task</button>
      </form>
    </div>
  );
}
