document.addEventListener("DOMContentLoaded", function() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function(e) {
            e.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 50,
                    behavior: "smooth"
                });
            }
        });
    });

    // Search functionality feedback
    const searchForm = document.querySelector("form[action*='blog']");
    if (searchForm) {
        searchForm.addEventListener("submit", function(event) {
            const searchInput = this.querySelector("input[name='q']");
            if (searchInput.value.trim() === "") {
                event.preventDefault();
                alert("Please enter a search term!");
            }
        });
    }
});
