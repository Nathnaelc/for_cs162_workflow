export const addNewTask = (newTask, taskType, tasks) => {
  tasks[taskType].push(newTask);
};

export const tasks = {
  toDo: [
    { title: "Task 1", description: "Description 1" },
    { title: "Task 2", description: "Description 2" },
  ],
  inProgress: [{ title: "Task 3", description: "Description 3" }],
  inReview: [{ title: "Task 4", description: "Description 4" }],
  done: [{ title: "Task 5", description: "Description 5" }],
};
