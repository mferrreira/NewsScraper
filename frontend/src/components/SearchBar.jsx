// src/components/SearchBar.jsx
import React, { useState } from 'react'

const SearchBar = ({ onSearch }) => {
  const [query, setQuery] = useState('')

  const handleChange = (event) => {
    setQuery(event.target.value)
  }

  const handleSubmit = (event) => {
    event.preventDefault()
    onSearch(query)
  }

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <input
        type="text"
        value={query}
        onChange={handleChange}
        placeholder="Pesquisar notícias..."
        className="w-full p-2 bg-gray-400 rounded-lg text-white text-center"
      />
    </form>
  )
}

export default SearchBar
