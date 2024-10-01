// Fetch news when the button is clicked
document.getElementById('fetch-news').addEventListener('click', function() {
    const category = document.getElementById('category').value;
    const apiKey = 'f446cbb0c08f4b33b48317e568e702fb'; // Your News API key
    const url = `https://newsapi.org/v2/top-headlines?category=${category}&apiKey=${apiKey}`;

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const newsList = document.getElementById('news-list');
            newsList.innerHTML = ''; // Clear previous news
            if (data.articles && data.articles.length > 0) {
                data.articles.forEach(article => {
                    const newsItem = document.createElement('div');
                    newsItem.innerHTML = `
                        <h2>${article.title}</h2>
                        <p>${article.description || 'No description available'}</p>
                        <a href="${article.url}" target="_blank">Read full article</a>
                    `;
                    newsList.appendChild(newsItem);
                });
            } else {
                newsList.innerHTML = 'No related news found!';
            }
        })
        .catch(error => console.error('Error fetching the news:', error));
});

// Handle login form submission
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Dummy authentication for demonstration
    if (username === 'user' && password === 'pass') {
        alert('Login successful!');
        $('#loginModal').modal('hide'); // Close the modal
    } else {
        alert('Invalid username or password.');
    }
});





