document.addEventListener("DOMContentLoaded", function() {
    
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


        
        if (localStorage.getItem('theme') === 'dark') {
            document.body.classList.add('dark-mode');
        }

       
        const darkModeToggle = document.getElementById('darkModeToggle');

        darkModeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-mode');
            if (document.body.classList.contains('dark-mode')) {
                localStorage.setItem('theme', 'dark');
                darkModeToggle.textContent = '🌞'; 
            } else {
                localStorage.setItem('theme', 'light');
                darkModeToggle.textContent = '🌓'; 
            }
        });
    
    


