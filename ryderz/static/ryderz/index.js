// Function to execute when DOM content is fully loaded
document.addEventListener("DOMContentLoaded", function () {
  // Get each button element by its ID
  var tutorButton = document.getElementById("Tutor_Button");
  var studentButton = document.getElementById("Student_Button");

  // Add event listener for tutorButton
  tutorButton.addEventListener("click", function () {
    // Change the button's background color to gold
    tutorButton.style.backgroundColor = "#EFBC4E";
    // Reset the background color of studentButton
    studentButton.style.backgroundColor = "";
    // Set the value of the hidden input field
    document.getElementById("id_type").value = "Tutor";
  });

  // Add event listener for studentButton
  studentButton.addEventListener("click", function () {
    // Change the button's background color to gold
    studentButton.style.backgroundColor = "#EFBC4E";
    // Reset the background color of tutorButton
    tutorButton.style.backgroundColor = "";
    // Set the value of the hidden input field
    document.getElementById("id_type").value = "Student";
  });

  document
    .getElementById("Signup_Button")
    .addEventListener("click", function () {
      window.location.href = "http://127.0.0.1:8000/ryderz/signup";
    });
});
