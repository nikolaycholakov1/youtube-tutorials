let priorityList = document.querySelectorAll(".task-priority");

// priorityList.forEach((task) => {
//   if (task.textContent === "Priority: High") {
//     task.style.color = "red";
//     console.log(task);
//   } else if (task.textContent === "Priority: Medium") {
//     task.style.color = "yellow";
//     console.log(task);
//   }
//   if (task.textContent === "Priority: Low") {
//     task.style.color = "green";
//     console.log(task);
//   }
// });

for (var i = 0; i < priorityList.length; i++) {
  // Access each element using elements[i]
  var textContent = priorityList[i].textContent;
  if (textContent === "Priority: High") {
    priorityList[i].style.color = "red";
  } else if (textContent === "Priority: Medium") {
    priorityList[i].style.color = "yellow";
  }
  if (textContent === "Priority: Low") {
    priorityList[i].style.color = "green";
  }
}
