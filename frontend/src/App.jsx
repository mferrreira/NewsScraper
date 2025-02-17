// src/App.jsx
import React, { useState, useEffect } from 'react'
import SearchBar from './components/SearchBar'
import NewsCard from './components/NewsCard'

const App = () => {
  const [news, setNews] = useState([])
  const [filteredNews, setFilteredNews] = useState([])

  const [shuffledNews, setShuffledNews] = useState([]);


  useEffect(() => {
    fetch('http://localhost:5000/api/news')
      .then(response => response.json())
      .then(data => {
        setNews(data)
        setFilteredNews(data)
      }).then(data => console.log())
  }, [])

  const handleSearch = (query) => {
    const filtered = news.filter(
      (item) => 
        item.title.toLowerCase().includes(query.toLowerCase()) ||
        item.description.toLowerCase().includes(query.toLowerCase())
    )
    setFilteredNews(filtered)
  }

  useEffect(() => {
    // Função para embaralhar a lista de notícias
    const shuffleArray = (array) => {
      const shuffled = [...array];
      for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
      }
      return shuffled;
    };

    // Atualiza a lista de notícias embaralhadas
    setShuffledNews(shuffleArray(news));
  }, [news]);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-10 text-black">Notícias</h1>
      <SearchBar onSearch={handleSearch} />

      <div className="comuns-2 sm:columns-3 lg:columns-4 gap-4 mt-30">

      {filteredNews.length === 0 ? (
        <p>Nenhuma notícia encontrada.</p>
      ) : (

        shuffledNews.map((item, index) => (
          <NewsCard
            key={index}
            title={item.title}
            description={item.description}
            url={item.url}
            imageUrl={item.image_url}
            source={item.source}  // Passando a fonte para o componente
          />
        ))
      )}
      </div>
    </div>

  )
}

export default App
