
document.getElementById('commentForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(this); // Gather form data

    fetch(this.action, { // Use the form's action URL
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}' // Include CSRF token for security
        }
    })
    .then(response => {
        if (response.ok) {
            return response.json(); // Parse the JSON response
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        console.log(data); // Handle the success response (e.g., show a success message)
        // Optionally, you can clear the input fields after submission
        document.getElementById('id_sender_rate').value = ''; // Reset rating dropdown
        document.getElementById('id_sender_message').value = ''; // Reset message input
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
});

