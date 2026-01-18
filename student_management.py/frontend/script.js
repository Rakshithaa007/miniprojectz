// API URL
const API_URL = "http://127.0.0.1:5000";

// Add student
function addStudent() {
  let name = document.getElementById("name").value;
  let roll = document.getElementById("roll").value;
  let dept = document.getElementById("dept").value;

  fetch(`${API_URL}/add`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: name,
      roll: roll,
      dept: dept,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      alert(data.message);
      loadStudents();
    });
}

// Load students
function loadStudents() {
  fetch(`${API_URL}/students`)
    .then((response) => response.json())
    .then((data) => {
      let table = document.getElementById("studentList");
      table.innerHTML = "";

      data.forEach((student) => {
        let row = table.insertRow();
        row.innerHTML = `
                    <td>${student.name}</td>
                    <td>${student.roll}</td>
                    <td>${student.dept}</td>
                    <td>
                        <button onclick="deleteStudent(${student.id})">
                            Delete
                        </button>
                    </td>
                `;
      });
    });
}

// Delete student
function deleteStudent(id) {
  fetch(`${API_URL}/delete/${id}`, {
    method: "DELETE",
  }).then(() => loadStudents());
}

// Load data when page opens
window.onload = loadStudents;
