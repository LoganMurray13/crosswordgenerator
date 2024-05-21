const postButton = document.getElementById('post_button');
        const jsonData = {name: 'Mike', greeting: 'Hello'}

        postButton.addEventListener('click', () => {
            fetch('{{ url_for("handle_post") }}', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json; charset=utf-8'
                },
                body: JSON.stringify(jsonData)
            })
                .then(response => response.json())
                .then(data => console.log('Success:', data))
                .catch((error) => {
                    console.error('Error:', error)
            });
        });
