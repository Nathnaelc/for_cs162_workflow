import React, { useState } from "react";
import axios from "axios";
import "./Newtask.css";
const BASE_URL = import.meta.env.VITE_BASE_URL;
console.log("BASE_URL", BASE_URL);

export default function NewTask() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [taskType, setTaskType] = useState("toDo");

  const handleSubmit = async (e) => {
    e.preventDefault();
    // create a new task object
    const newTask = { description, column: taskType };
    console.log("New task added", newTask);

    try {
      const response = await fetch(`${BASE_URL}/api/add_task`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newTask),
      });

      const data = await response.json();

      if (data.success) {
        console.log("Task added successfully", newTask);
        setTitle("");
        setDescription("");
        setTaskType("toDo");
      } else {
        console.log("Error adding task");
      }
    } catch (error) {
      console.log("Error adding task", error);
      console.log(error.response);
    }
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
