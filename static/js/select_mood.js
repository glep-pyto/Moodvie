document.addEventListener('DOMContentLoaded', () => { // Wait for the DOM to be fully loaded
    const moodInput = document.getElementById('selected-mood'); // Get the hidden input field where the selected mood will be stored
    const form = document.querySelector('form'); // Get the form element

    form.addEventListener('submit', (event) => { // Add an event listener for form submission
        if (!moodInput.value) { // If no mood has been selected
            event.preventDefault(); // Prevent the form from being submitted
            alert('Please select a mood before getting recommendations.'); // Alert the user to select a mood
        }
    });

    document.querySelectorAll('.emoji-button').forEach(button => { //Find all the emoji buttons and add a click event listener to each
        button.addEventListener('click', () => { // When an emoji button is clicked
            moodInput.value = button.dataset.mood; // Save the selected mood to the hidden input field so that the form knows which mood was selected
            button.classList.add('selected'); //highlight the selected button
            document.querySelectorAll('.emoji-button').forEach(b => { // Find all emoji buttons again
                if (b !== button) b.classList.remove('selected'); // Remove the 'selected' class from all buttons except the one that was just clicked
            });
        });
    });
});


