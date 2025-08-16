// Toggle nav on mobile
const toggleBtn = document.getElementById('nav-toggle');
const navLinks = document.getElementById('nav-links');

toggleBtn.addEventListener('click', () => {
  navLinks.classList.toggle('show');
});

// Handle contact form submit
const form = document.getElementById('contact-form');
const formMsg = document.getElementById('form-msg');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  formMsg.textContent = "Thanks! We'll get back to you shortly.";
  form.reset();
});


document.addEventListener("DOMContentLoaded", () => {
  const trigger = document.getElementById("login-trigger");
  const container = document.getElementById("form-container");
  const card = document.getElementById("form-card");
  const flipBtns = document.querySelectorAll(".flip-btn");

  trigger.addEventListener("mouseenter", () => {
    container.classList.add("show-form");
  });

  container.addEventListener("mouseleave", () => {
    container.classList.remove("show-form");
  });

  flipBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      card.style.transform = card.style.transform === "rotateY(180deg)" ? "rotateY(0deg)" : "rotateY(180deg)";
    });
  });
});
