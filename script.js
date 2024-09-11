function toggleSection(sectionId) {
  const section = document.getElementById(sectionId);
  if (section.classList.contains("hidden")) {
    section.classList.remove("hidden");
  } else {
    section.classList.add("hidden");
  }
}

function openModal(src) {
  const modal = document.getElementById("myModal");
  const modalImg = document.getElementById("modalImg");
  modalImg.src = src; // Set the clicked image source to the modal image
  modal.style.display = "flex"; // Show the modal
}

function closeModal() {
  const modal = document.getElementById("myModal");
  modal.style.display = "none"; // Hide the modal when close button is clicked
}
document
  .getElementById("contact-form")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(this);
    const data = {};

    formData.forEach((value, key) => {
      data[key] = value;
    });

    fetch("https://api.fatalerror.live/members", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        const responseMessage = document.getElementById("response-message");
        responseMessage.innerText = "Data submitted successfully!";
        responseMessage.className = "success"; // Apply success class
        console.log("Success:", data);
      })
      .catch((error) => {
        const responseMessage = document.getElementById("response-message");
        responseMessage.innerText = "Error submitting data.";
        responseMessage.className = "error"; // Apply error class
        console.error("Error:", error);
      });
  });
