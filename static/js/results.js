document.getElementById("more-button")?.addEventListener("click", function () { // find the "Show More" button and click it if it exists (example: if there are more than 5 movies)
    document.querySelectorAll(".movie-card").forEach(card => card.style.display = "block"); // Show all movie cards
    this.style.display = "none"; // Hide the "Show More" button after clicking
});