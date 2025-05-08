const toggle_theme_btn = document.getElementById("toggle_theme");

toggle_theme_btn.addEventListener("click", () => {
    document.body.classList.toggle("dark-theme");
});