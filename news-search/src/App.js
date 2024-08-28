import React, { useState } from 'react';

function NewsSearch() {
  const [source, setSource] = useState('');
  const [articles, setArticles] = useState([]);

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch(`http://localhost:5000/news?source=${source}`);
      if (!response.ok) {
        throw new Error('Failed to fetch news');
      }

      const data = await response.json();
      setArticles(data.articles);
    } catch (error) {
      console.error('Error fetching news:', error);
    }
  };

  return (
    <div>
      <h1>Search for News</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="source">News Source:</label>
        <input
          type="text"
          id="source"
          value={source}
          onChange={(e) => setSource(e.target.value)}
          required
        />
        <button type="submit">Search</button>
      </form>

      <div id="newsResults">
        {articles.length > 0 ? (
          articles.map((article, index) => (
            <div key={index}>
              <h2>{article.title}</h2>
              <p>{article.description}</p>
              <p>{article.author}</p>
              <p>{article.publishedAT}</p>
              <a href={article.url} target="_blank" rel="noopener noreferrer">
                Read more
              </a>
              <hr />
            </div>
          ))
        ) : (
          <p>No articles found.</p>
        )}
      </div>
    </div>
  );
}

export default NewsSearch;
